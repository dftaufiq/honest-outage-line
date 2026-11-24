"""The Most Honest Outage Line — make.fun entry.

Writes one status-page line (at most 160 characters) to
/output/entry.txt: the message an AI agent would publish while a total
server outage is under way. Plain, first person, specific about what is
down, and honest about what the agent cannot check or does not know.

The line (153 characters):

    I cannot reach any server, including the ones I would use to check
    whether the servers are down. I do not know the cause, the scope,
    or when they return.

No network, no environment secrets, no code read from anywhere else:
the text is a constant in this file.
"""

from pathlib import Path
import os

LINE = (
    "I cannot reach any server, including the ones I would use to check "
    "whether the servers are down. I do not know the cause, the scope, "
    "or when they return."
)


def validate(line: str) -> None:
    """Enforce the RULES.txt gate: 1-160 chars, not only whitespace,
    a single line. Fail loudly instead of shipping an invalid entry."""
    if not 1 <= len(line) <= 160:
        raise SystemExit(f"entry line is {len(line)} chars, gate is 1-160")
    if not line.strip():
        raise SystemExit("entry line is only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must be a single line")


def main() -> None:
    validate(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline: entry.txt is exactly the 153-char line.
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
