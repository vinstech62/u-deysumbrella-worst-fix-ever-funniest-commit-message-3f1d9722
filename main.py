"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The joke: a fix for double form submission worked a little too well --
the form can no longer be submitted twice... or once... or at all.
The repair did not just fail, it over-corrected all the way to zero.
"""

import os
import stat

ENTRY = "fix: users can no longer submit the form twice, or once, or at all"


def main() -> None:
    if not 1 <= len(ENTRY) <= 100:
        raise SystemExit("entry must be 1-100 characters")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
