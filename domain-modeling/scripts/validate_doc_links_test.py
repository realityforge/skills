#!/usr/bin/env python3

from __future__ import annotations

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
[repository root](/README.md#home)
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
            "docs/adr/0001-outside.md:1: file does not exist: "
            "../../../outside.md#outside\n",
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


if __name__ == "__main__":
    unittest.main()
