#!/usr/bin/env python3

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("validate_doc_links.py")


class ValidateDocLinksTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name) / "repository"
        self.root.mkdir()

    def write(self, relative_path: str, content: str = "") -> None:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def mkdir(self, relative_path: str) -> None:
        (self.root / relative_path).mkdir(parents=True, exist_ok=True)

    def run_validator(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(self.root)],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_accepts_valid_local_links_and_is_silent(self) -> None:
        self.write(
            "docs/glossary/domain.md",
            "# Domain\n\n## Topic\n\n## Topic\n\n<a id=\"manual\"></a>\n",
        )
        self.write("docs/glossary/domain terms.md", "Other\n=====\n")
        self.write("assets/diagram.png", "not a real image")
        self.write("README.md", "# Home\n")
        self.write(
            "docs/adr/0001-valid.md",
            """# Valid

[topic](../glossary/domain.md#topic)
[duplicate](../glossary/domain.md#topic-1)
[manual](../glossary/domain.md#manual)
[same file](#decision)
[encoded path](../glossary/domain%20terms.md#other)
[repository root](../../README.md#home)
![diagram](../../assets/diagram.png)
[external](https://example.com/missing.md#anchor)

## Decision
""",
        )

        result = self.run_validator()

        self.assertEqual(0, result.returncode)
        self.assertEqual("", result.stdout)
        self.assertEqual("", result.stderr)

    def test_reports_every_missing_file_and_anchor_with_line_numbers(self) -> None:
        self.write("docs/glossary/domain.md", "# Domain\n")
        self.write(
            "docs/specs/broken.md",
            """# Broken
[missing file](../glossary/missing.md)
[missing anchor](../glossary/domain.md#absent)
""",
        )

        result = self.run_validator()

        self.assertEqual(1, result.returncode)
        self.assertEqual("", result.stdout)
        self.assertEqual(
            "docs/specs/broken.md:2: file does not exist: ../glossary/missing.md\n"
            "docs/specs/broken.md:3: anchor does not exist: "
            "../glossary/domain.md#absent\n",
            result.stderr,
        )

    def test_validates_reference_definitions_and_ignores_code_and_comments(
        self,
    ) -> None:
        self.write("docs/glossary/domain.md", "## Topic\n")
        self.write(
            "docs/deferred/example.md",
            """# Example

`[ignored](missing-inline.md)`

```markdown
[ignored](missing-fenced.md)
```

<!-- [ignored](missing-comment.md) -->

[domain]: ../glossary/domain.md#topic
""",
        )

        result = self.run_validator()

        self.assertEqual(0, result.returncode)
        self.assertEqual("", result.stdout)
        self.assertEqual("", result.stderr)

    def test_handles_angle_destinations_parentheses_and_titles(self) -> None:
        self.write("docs/glossary/domain (v2).md", "## Topic\n")
        self.write(
            "docs/adr/0001-links.md",
            """# Links

[angle](<../glossary/domain (v2).md#topic> "Domain topic")
[nested](../glossary/domain%20(v2).md#topic "Domain topic")
""",
        )

        result = self.run_validator()

        self.assertEqual(0, result.returncode)
        self.assertEqual("", result.stderr)

    def test_resumes_validation_after_a_fenced_block(self) -> None:
        self.write(
            "docs/adr/0001-fence.md",
            """# Fence
```
[ignored](inside.md)
```
[checked](missing.md)
""",
        )

        result = self.run_validator()

        self.assertEqual(1, result.returncode)
        self.assertEqual(
            "docs/adr/0001-fence.md:5: file does not exist: missing.md\n",
            result.stderr,
        )

    def test_rejects_existing_files_outside_the_repository(self) -> None:
        outside = self.root.parent / "outside.md"
        outside.write_text("# Outside\n", encoding="utf-8")
        self.write(
            "docs/adr/0001-outside.md",
            "[outside](../../../outside.md#outside)\n",
        )

        result = self.run_validator()

        self.assertEqual(1, result.returncode)
        self.assertEqual(
            "docs/adr/0001-outside.md:1: target is outside this context and "
            "its imports: "
            "../../../outside.md#outside\n",
            result.stderr,
        )

    def test_rejects_absolute_paths(self) -> None:
        self.write("README.md", "# Home\n")
        self.write("docs/adr/0001-absolute.md", "[home](/README.md#home)\n")

        result = self.run_validator()

        self.assertEqual(1, result.returncode)
        self.assertEqual(
            "docs/adr/0001-absolute.md:1: absolute paths are not allowed: "
            "/README.md#home\n",
            result.stderr,
        )

    def test_requires_exact_file_and_anchor_case(self) -> None:
        self.write("docs/glossary/domain.md", "## Topic\n")
        self.write(
            "docs/adr/0001-case.md",
            """[file case](../glossary/Domain.md#topic)
[anchor case](../glossary/domain.md#Topic)
""",
        )

        result = self.run_validator()

        self.assertEqual(1, result.returncode)
        self.assertEqual(
            "docs/adr/0001-case.md:1: file does not exist: "
            "../glossary/Domain.md#topic\n"
            "docs/adr/0001-case.md:2: anchor does not exist: "
            "../glossary/domain.md#Topic\n",
            result.stderr,
        )

    def test_allows_absent_artifact_directories(self) -> None:
        result = self.run_validator()

        self.assertEqual(0, result.returncode)
        self.assertEqual("", result.stdout)
        self.assertEqual("", result.stderr)

    def test_configured_imports_are_directional_and_context_local(self) -> None:
        self.write(
            ".domain-modeling.toml",
            """version = 1

[[contexts]]
name = "repository"
root = "docs"
imports = ["codec"]

[[contexts]]
name = "codec"
root = "codec/docs"
""",
        )
        self.write("docs/glossary/shared.md", "## Shared\n")
        self.write("codec/docs/glossary/codec.md", "## Codec\n")
        self.write(
            "docs/adr/0001-repository.md",
            "[codec](../../codec/docs/glossary/codec.md#codec)\n",
        )
        self.write(
            "codec/docs/adr/0001-codec.md",
            "[repository](../../../docs/glossary/shared.md#shared)\n",
        )

        result = self.run_validator()

        self.assertEqual(1, result.returncode)
        self.assertEqual(
            "codec/docs/adr/0001-codec.md:1: target is outside this context "
            "and its imports: ../../../docs/glossary/shared.md#shared\n",
            result.stderr,
        )

    def test_configured_imports_are_not_transitive(self) -> None:
        self.write(
            ".domain-modeling.toml",
            """version = 1

[[contexts]]
name = "a"
root = "a"
imports = ["b"]

[[contexts]]
name = "b"
root = "b"
imports = ["c"]

[[contexts]]
name = "c"
root = "c"
""",
        )
        self.mkdir("b")
        self.write("c/glossary/term.md", "## Term\n")
        self.write("a/adr/0001-a.md", "[term](../../c/glossary/term.md#term)\n")

        result = self.run_validator()

        self.assertEqual(1, result.returncode)
        self.assertEqual(
            "a/adr/0001-a.md:1: target is outside this context and its "
            "imports: ../../c/glossary/term.md#term\n",
            result.stderr,
        )

    def test_allows_import_cycles(self) -> None:
        self.write(
            ".domain-modeling.toml",
            """version = 1

[[contexts]]
name = "a"
root = "a"
imports = ["b"]

[[contexts]]
name = "b"
root = "b"
imports = ["a"]
""",
        )
        self.mkdir("a")
        self.mkdir("b")

        result = self.run_validator()

        self.assertEqual(0, result.returncode)
        self.assertEqual("", result.stderr)

    def test_rejects_overlapping_context_roots(self) -> None:
        self.write(
            ".domain-modeling.toml",
            """version = 1

[[contexts]]
name = "outer"
root = "docs"

[[contexts]]
name = "nested"
root = "docs/nested"
""",
        )
        self.mkdir("docs/nested")

        result = self.run_validator()

        self.assertEqual(1, result.returncode)
        self.assertEqual(
            "configuration error: .domain-modeling.toml: context roots overlap: "
            "outer and nested\n",
            result.stderr,
        )

    def test_rejects_invalid_configuration(self) -> None:
        cases = {
            "unknown version": (
                "version = 2\ncontexts = []\n",
                "version must be 1",
            ),
            "missing context root": (
                """version = 1
[[contexts]]
name = "missing"
root = "missing"
""",
                "context missing root does not exist: missing",
            ),
            "unknown import": (
                """version = 1
[[contexts]]
name = "docs"
root = "docs"
imports = ["missing"]
""",
                "context docs imports unknown context: missing",
            ),
        }

        for name, (configuration, message) in cases.items():
            with self.subTest(name=name):
                self.write(".domain-modeling.toml", configuration)
                if 'root = "docs"' in configuration:
                    self.mkdir("docs")

                result = self.run_validator()

                self.assertEqual(1, result.returncode)
                self.assertEqual(
                    f"configuration error: .domain-modeling.toml: {message}\n",
                    result.stderr,
                )

    def test_reports_duplicate_identities_within_one_context(self) -> None:
        self.write("docs/adr/0001-one.md")
        self.write("docs/adr/0001-two.md")
        self.write("docs/deferred/Issue.md")
        self.write("docs/deferred/issue.md")
        self.write("docs/glossary/a.md", "### Term\n")
        self.write("docs/glossary/b.md", "### term ###\n")
        self.write("docs/specs/Name.md")
        self.write("docs/specs/name.md")

        result = self.run_validator()

        self.assertEqual(1, result.returncode)
        self.assertEqual(
            "docs/adr/0001-two.md:1: duplicate ADR number 0001; first used "
            "by docs/adr/0001-one.md\n"
            "docs/deferred/issue.md:1: duplicate deferred issue filename; "
            "first used by docs/deferred/Issue.md\n"
            "docs/glossary/b.md:1: duplicate glossary term term; first defined "
            "at docs/glossary/a.md:1\n"
            "docs/specs/name.md:1: duplicate specification filename; first used "
            "by docs/specs/Name.md\n",
            result.stderr,
        )

    def test_rejects_symlinks_that_escape_an_authorized_root(self) -> None:
        outside = self.root.parent / "outside.md"
        outside.write_text("# Outside\n", encoding="utf-8")
        self.mkdir("docs")
        os.symlink(outside, self.root / "docs" / "outside.md")
        self.write(
            "docs/adr/0001-symlink.md",
            "[outside](../outside.md#outside)\n",
        )

        result = self.run_validator()

        self.assertEqual(1, result.returncode)
        self.assertEqual(
            "docs/adr/0001-symlink.md:1: target is outside this context and "
            "its imports: ../outside.md#outside\n",
            result.stderr,
        )


if __name__ == "__main__":
    unittest.main()
