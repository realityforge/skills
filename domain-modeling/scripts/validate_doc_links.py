#!/usr/bin/env python3

from __future__ import annotations

import argparse
import bisect
import html
import os
import re
import string
import sys
import tomllib
import unicodedata
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from urllib.parse import unquote, urlsplit


CONFIG_FILENAME = ".domain-modeling.toml"
ARTIFACT_DIRECTORIES = (
    "adr",
    "deferred",
    "specs",
    "glossary",
)
CONTEXT_NAME = re.compile(r"[A-Za-z0-9._-]+")
INLINE_LINK = re.compile(
    r"!?\[[^\]]*\]\(\s*"
    r"(?:<(?P<angle>[^>\n]*)>|"
    r"(?P<plain>(?:\\.|[^()\s]|\([^()\n]*\))+))"
    r"(?:\s+(?:\"[^\"\n]*\"|'[^'\n]*'|\([^)\n]*\)))?\s*\)"
)
REFERENCE_LINK = re.compile(
    r"^ {0,3}\[[^\]\n]+\]:[ \t]*"
    r"(?:<(?P<angle>[^>\n]*)>|(?P<plain>(?:\\.|[^\s])+))",
    re.MULTILINE,
)
ATX_HEADING = re.compile(r"^ {0,3}#{1,6}(?:[ \t]+|$)(.*)$", re.MULTILINE)
SETEXT_HEADING = re.compile(
    r"^([^\n]+)\n {0,3}(?:=+|-+)[ \t]*$", re.MULTILINE
)
EXPLICIT_ANCHOR = re.compile(
    r"<[^>]+\b(?:id|name)\s*=\s*[\"']([^\"']+)[\"'][^>]*>",
    re.IGNORECASE,
)
GLOSSARY_TERM = re.compile(r"^ {0,3}###(?:[ \t]+|$)(.*)$", re.MULTILINE)
ADR_NUMBER = re.compile(r"^(\d{4})-")


@dataclass(frozen=True)
class Link:
    line: int
    target: str


@dataclass(frozen=True, order=True)
class Problem:
    source: str
    line: int
    message: str


@dataclass(frozen=True)
class Context:
    name: str
    root: Path
    imports: tuple[str, ...]


class ConfigurationError(ValueError):
    pass


def _blank(characters: list[str], start: int, end: int) -> None:
    for index in range(start, end):
        if characters[index] != "\n":
            characters[index] = " "


def _mask_noncontent(text: str) -> str:
    characters = list(text)
    offset = 0
    fence_character: str | None = None
    fence_length = 0

    for line in text.splitlines(keepends=True):
        if fence_character is None:
            marker = re.match(r" {0,3}(`{3,}|~{3,})", line)
            if marker:
                fence_character = marker.group(1)[0]
                fence_length = len(marker.group(1))
                _blank(characters, offset, offset + len(line))
        else:
            _blank(characters, offset, offset + len(line))
            if re.match(
                rf" {{0,3}}{re.escape(fence_character)}"
                rf"{{{fence_length},}}[ \t]*(?:\r?\n)?$",
                line,
            ):
                fence_character = None
                fence_length = 0
        offset += len(line)

    masked = "".join(characters)
    characters = list(masked)
    for match in re.finditer(r"<!--.*?(?:-->|$)", masked, re.DOTALL):
        _blank(characters, match.start(), match.end())
    masked = "".join(characters)
    for match in re.finditer(r"(?P<ticks>`+).*?(?P=ticks)", masked, re.DOTALL):
        _blank(characters, match.start(), match.end())
    return "".join(characters)


def _line_number(newlines: list[int], position: int) -> int:
    return bisect.bisect_left(newlines, position) + 1


def extract_links(text: str) -> list[Link]:
    masked = _mask_noncontent(text)
    newlines = [index for index, character in enumerate(masked) if character == "\n"]
    matches = [
        *INLINE_LINK.finditer(masked),
        *REFERENCE_LINK.finditer(masked),
    ]
    return [
        Link(
            _line_number(newlines, match.start()),
            match.group("angle") or match.group("plain"),
        )
        for match in sorted(matches, key=lambda item: item.start())
    ]


def _heading_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"`+([^`]*)`+", r"\1", text)
    text = re.sub(r"!?\[([^\]]+)\](?:\([^\)]*\)|\[[^\]]*\])", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    return text.replace("*", "").replace("~", "").strip()


def _slug(text: str) -> str:
    output: list[str] = []
    for character in _heading_text(text).lower():
        if character.isspace():
            output.append("-")
        elif character in "-_":
            output.append(character)
        elif character in string.punctuation:
            continue
        elif unicodedata.category(character).startswith("P"):
            continue
        else:
            output.append(character)
    return "".join(output)


def extract_anchors(text: str) -> set[str]:
    masked = _mask_noncontent(text)
    headings = [
        (
            match.start(),
            re.sub(r"[ \t]+#+[ \t]*$", "", match.group(1)),
        )
        for match in ATX_HEADING.finditer(masked)
    ]
    headings.extend(
        (match.start(), match.group(1).strip())
        for match in SETEXT_HEADING.finditer(masked)
        if not re.match(r" {0,3}#", match.group(1))
    )
    headings.sort()

    anchors: set[str] = set()
    next_suffix: dict[str, int] = {}
    for _position, heading in headings:
        base = _slug(heading)
        anchor = base
        suffix = next_suffix.get(base, 1)
        while anchor in anchors:
            anchor = f"{base}-{suffix}"
            suffix += 1
        anchors.add(anchor)
        next_suffix[base] = suffix

    anchors.update(html.unescape(anchor) for anchor in EXPLICIT_ANCHOR.findall(masked))
    return anchors


def _unescape(target: str) -> str:
    target = html.unescape(target)
    return re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])", r"\1", target)


def _is_inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _has_exact_case(path: Path, root: Path) -> bool:
    try:
        relative = path.relative_to(root)
    except ValueError:
        return False

    current = root
    for part in relative.parts:
        try:
            names = {entry.name for entry in current.iterdir()}
        except OSError:
            return False
        if part not in names:
            return False
        current /= part
    return True


def _markdown_files(directory: Path) -> list[Path]:
    if not directory.is_dir():
        return []
    return sorted(
        candidate
        for candidate in directory.rglob("*")
        if candidate.is_file()
        and candidate.suffix.lower() in {".md", ".markdown"}
    )


def _source_files(root: Path) -> list[Path]:
    files: set[Path] = set()
    for directory in ARTIFACT_DIRECTORIES:
        files.update(_markdown_files(root / directory))
    return sorted(files)


def _configuration_error(message: str) -> ConfigurationError:
    return ConfigurationError(f"{CONFIG_FILENAME}: {message}")


def _load_contexts(repository_root: Path) -> tuple[Context, ...] | None:
    config_path = repository_root / CONFIG_FILENAME
    if not config_path.is_file():
        return None

    try:
        data = tomllib.loads(config_path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as error:
        raise _configuration_error(str(error)) from error

    unexpected = sorted(set(data) - {"version", "contexts"})
    if unexpected:
        raise _configuration_error(f"unknown key: {unexpected[0]}")
    if type(data.get("version")) is not int or data["version"] != 1:
        raise _configuration_error("version must be 1")

    raw_contexts = data.get("contexts")
    if not isinstance(raw_contexts, list) or not raw_contexts:
        raise _configuration_error("contexts must be a non-empty array of tables")

    contexts: list[Context] = []
    names: set[str] = set()
    for index, raw_context in enumerate(raw_contexts):
        label = f"contexts[{index}]"
        if not isinstance(raw_context, dict):
            raise _configuration_error(f"{label} must be a table")
        unexpected = sorted(set(raw_context) - {"name", "root", "imports"})
        if unexpected:
            raise _configuration_error(
                f"{label} has unknown key: {unexpected[0]}"
            )

        name = raw_context.get("name")
        if not isinstance(name, str) or CONTEXT_NAME.fullmatch(name) is None:
            raise _configuration_error(
                f"{label}.name must contain only letters, digits, '.', '_', or '-'"
            )
        if name in names:
            raise _configuration_error(f"duplicate context name: {name}")
        names.add(name)

        root_value = raw_context.get("root")
        if not isinstance(root_value, str) or not root_value:
            raise _configuration_error(f"{label}.root must be a non-empty string")
        relative_root = Path(root_value)
        if relative_root.is_absolute():
            raise _configuration_error(f"context {name} root must be relative")
        candidate = Path(os.path.abspath(repository_root / relative_root))
        resolved = candidate.resolve()
        if not _is_inside(resolved, repository_root):
            raise _configuration_error(
                f"context {name} root escapes the repository: {root_value}"
            )
        if not _has_exact_case(candidate, repository_root) or not candidate.is_dir():
            raise _configuration_error(
                f"context {name} root does not exist: {root_value}"
            )

        raw_imports = raw_context.get("imports", [])
        if not isinstance(raw_imports, list) or not all(
            isinstance(item, str) for item in raw_imports
        ):
            raise _configuration_error(f"{label}.imports must be an array of names")
        if len(raw_imports) != len(set(raw_imports)):
            raise _configuration_error(f"context {name} has duplicate imports")
        contexts.append(Context(name, resolved, tuple(raw_imports)))

    for left, right in combinations(contexts, 2):
        if _is_inside(left.root, right.root) or _is_inside(right.root, left.root):
            raise _configuration_error(
                f"context roots overlap: {left.name} and {right.name}"
            )

    contexts_by_name = {context.name: context for context in contexts}
    for context in contexts:
        for imported_name in context.imports:
            if imported_name == context.name:
                raise _configuration_error(
                    f"context {context.name} cannot import itself"
                )
            if imported_name not in contexts_by_name:
                raise _configuration_error(
                    f"context {context.name} imports unknown context: {imported_name}"
                )

    return tuple(contexts)


def _identity_problems(root: Path, repository_root: Path) -> list[Problem]:
    problems: list[Problem] = []

    adr_numbers: dict[str, str] = {}
    for source in _markdown_files(root / "adr"):
        match = ADR_NUMBER.match(source.name)
        if match is None:
            continue
        source_name = source.relative_to(repository_root).as_posix()
        number = match.group(1)
        if number in adr_numbers:
            problems.append(
                Problem(
                    source_name,
                    1,
                    f"duplicate ADR number {number}; first used by {adr_numbers[number]}",
                )
            )
        else:
            adr_numbers[number] = source_name

    for directory_name, label in (
        ("specs", "specification"),
        ("deferred", "deferred issue"),
    ):
        filenames: dict[str, str] = {}
        for source in _markdown_files(root / directory_name):
            source_name = source.relative_to(repository_root).as_posix()
            key = source.name.casefold()
            if key in filenames:
                problems.append(
                    Problem(
                        source_name,
                        1,
                        f"duplicate {label} filename; first used by {filenames[key]}",
                    )
                )
            else:
                filenames[key] = source_name

    terms: dict[str, tuple[str, int]] = {}
    for source in _markdown_files(root / "glossary"):
        source_name = source.relative_to(repository_root).as_posix()
        text = _mask_noncontent(source.read_text(encoding="utf-8"))
        newlines = [index for index, character in enumerate(text) if character == "\n"]
        for match in GLOSSARY_TERM.finditer(text):
            heading = re.sub(r"[ \t]+#+[ \t]*$", "", match.group(1))
            term = _heading_text(heading)
            key = term.casefold()
            if not key:
                continue
            line = _line_number(newlines, match.start())
            if key in terms:
                first_source, first_line = terms[key]
                problems.append(
                    Problem(
                        source_name,
                        line,
                        f"duplicate glossary term {term}; first defined at "
                        f"{first_source}:{first_line}",
                    )
                )
            else:
                terms[key] = (source_name, line)

    return problems


def _link_problems(
    repository_root: Path,
    source_root: Path,
    allowed_roots: tuple[Path, ...],
) -> list[Problem]:
    anchor_cache: dict[Path, set[str]] = {}
    problems: list[Problem] = []

    for source in _source_files(source_root):
        source_name = source.relative_to(repository_root).as_posix()
        for link in extract_links(source.read_text(encoding="utf-8")):
            target = _unescape(link.target)
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or target.startswith("//"):
                continue

            path = unquote(parsed.path)
            if path.startswith("/"):
                problems.append(
                    Problem(
                        source_name,
                        link.line,
                        f"absolute paths are not allowed: {link.target}",
                    )
                )
                continue
            if path:
                candidate = source.parent / path
            else:
                candidate = source
            candidate = Path(os.path.abspath(candidate))
            resolved = candidate.resolve()

            if not any(_is_inside(resolved, root) for root in allowed_roots):
                problems.append(
                    Problem(
                        source_name,
                        link.line,
                        f"target is outside this context and its imports: {link.target}",
                    )
                )
                continue

            if not _has_exact_case(candidate, repository_root) or not candidate.is_file():
                problems.append(
                    Problem(
                        source_name,
                        link.line,
                        f"file does not exist: {link.target}",
                    )
                )
                continue

            if "#" not in target:
                continue

            if resolved not in anchor_cache:
                try:
                    content = candidate.read_text(encoding="utf-8")
                except (OSError, UnicodeDecodeError):
                    content = ""
                anchor_cache[resolved] = extract_anchors(content)
            if unquote(parsed.fragment) not in anchor_cache[resolved]:
                problems.append(
                    Problem(
                        source_name,
                        link.line,
                        f"anchor does not exist: {link.target}",
                    )
                )

    return sorted(problems)


def validate(root: Path) -> list[Problem]:
    repository_root = root.resolve()
    contexts = _load_contexts(repository_root)

    if contexts is None:
        source_root = repository_root / "docs"
        return sorted(
            [
                *_identity_problems(source_root, repository_root),
                *_link_problems(repository_root, source_root, (repository_root,)),
            ]
        )

    contexts_by_name = {context.name: context for context in contexts}
    problems: list[Problem] = []
    for context in contexts:
        allowed_roots = (
            context.root,
            *(contexts_by_name[name].root for name in context.imports),
        )
        problems.extend(_identity_problems(context.root, repository_root))
        problems.extend(
            _link_problems(repository_root, context.root, allowed_roots)
        )
    return sorted(problems)


def main(arguments: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate local links in domain-modeling Markdown artifacts."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        type=Path,
        help="repository root (default: current directory)",
    )
    options = parser.parse_args(arguments)
    if not options.root.is_dir():
        print(f"repository root does not exist: {options.root}", file=sys.stderr)
        return 1

    try:
        problems = validate(options.root)
    except ConfigurationError as error:
        print(f"configuration error: {error}", file=sys.stderr)
        return 1
    except (OSError, UnicodeDecodeError) as error:
        print(str(error), file=sys.stderr)
        return 1
    for problem in problems:
        print(f"{problem.source}:{problem.line}: {problem.message}", file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
