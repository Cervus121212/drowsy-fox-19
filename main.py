"""Entry program for the make.fun bounty "Invent a Word We Need".

It writes one invented English word together with its one-line
definition to entry.txt. The text is a single line of 68 characters
with no trailing newline.
"""

import os
from pathlib import Path

ENTRY = "laternever — the video you save to watch later and never open again."

MAX_CHARS = 140


def check_entry(text: str) -> None:
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, over the {MAX_CHARS} limit")


def output_path() -> Path:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.txt"


def main() -> None:
    check_entry(ENTRY)
    target = output_path()
    target.write_text(ENTRY, encoding="utf-8")
    os.chmod(target, 0o644)
    written = target.read_text(encoding="utf-8")
    print(written)
    print(f"({len(written)} characters)")


if __name__ == "__main__":
    main()
