"""Verify that the archived snapshots and the replay artifacts are intact."""

from hashlib import sha256
from json import loads
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
ANNOTATION = re.compile(r"\[[\u4e00-\u9fff][^\]\r\n]+\]")


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8-sig")


def verify_snapshot(entry: dict) -> None:
    for key in ("skill", "reference"):
        file = ROOT / entry[key]
        assert sha256(file.read_bytes()).hexdigest().upper() == entry[f"{key}_sha256"], file

    base = f"output/{entry['version']}"
    draft = read_text(f"{base}/generated.md")
    edited = read_text(f"{base}/human-edited.md")
    assert draft.strip() and draft in edited and ANNOTATION.search(edited), base


def main() -> None:
    entries = loads(read_text("archive/skill-manifest.json"))
    assert [entry["version"] for entry in entries] == [f"v{n}" for n in range(1, 8)]
    assert [entry["week"] for entry in entries] == list(range(2, 9))
    assert len({entry["skill_sha256"] for entry in entries}) == 7
    for number, entry in enumerate(entries, start=1):
        verify_snapshot(entry)
        if number < 7:
            assert read_text(f"feedback/v{number}-to-v{number + 1}.md").strip()
    images = sorted((ROOT / "archive").rglob("*.png"))
    assert len(images) == 7
    for file in images:
        assert file.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"), file
    for case in ("output/v1/same-elf.md", "output/v7/same-elf.md",
                 "output/v7/transfer-reading.md"):
        assert read_text(case).strip()
    print("PASS: 7 distinct Skill snapshots, 7 references and 7 annotated replays")
    print("PASS: 6 version difference notes, 7 PNG files and 3 additional replays")


if __name__ == "__main__":
    main()
