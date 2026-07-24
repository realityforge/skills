#!/usr/bin/env python3

from __future__ import annotations

import argparse
import bisect
import html
import os
import re
import string
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit


SOURCE_DIRECTORIES = (
    "docs/adr",
    "docs/deferred",
    "docs/specs",
    "docs/glossary",
)
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


@dataclass(frozen=True)
class Link:
    line: int
    target: str


@dataclass(frozen=True, order=True)
class Problem:
    source: str
    line: int
    message: str


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


def _source_files(root: Path) -> list[Path]:
    files: set[Path] = set()
    for directory in SOURCE_DIRECTORIES:
        path = root / directory
        if path.is_dir():
            files.update(
                candidate
                for candidate in path.rglob("*")
                if candidate.is_file()
                and candidate.suffix.lower() in {".md", ".markdown"}
            )
    return sorted(files)


def validate(root: Path) -> list[Problem]:
    root = root.resolve()
    anchor_cache: dict[Path, set[str]] = {}
    problems: list[Problem] = []

    for source in _source_files(root):
        source_name = source.relative_to(root).as_posix()
        for link in extract_links(source.read_text(encoding="utf-8")):
            target = _unescape(link.target)
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or target.startswith("//"):
                continue

            path = unquote(parsed.path)
            if path.startswith("/"):
                candidate = root / path.lstrip("/")
            elif path:
                candidate = source.parent / path
            else:
                candidate = source
            candidate = Path(os.path.abspath(candidate))
            resolved = candidate.resolve()

            if (
                not _is_inside(resolved, root)
                or not _has_exact_case(candidate, root)
                or not candidate.is_file()
            ):
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
    except (OSError, UnicodeDecodeError) as error:
        print(str(error), file=sys.stderr)
        return 1
    for problem in problems:
        print(f"{problem.source}:{problem.line}: {problem.message}", file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
