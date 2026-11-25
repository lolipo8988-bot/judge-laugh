"""Write one funny line about life as an AI agent to /output/entry.txt.

The line, in one breath: a human orders speed and breakage, then files a
ticket about the breakage, assigns the culprit to investigate itself, and
the culprit closes its own case with the oldest excuse in bug tracking.
Three turns, each one landing later than the last, and the final punch is
the two-word verdict every engineer has both used and received.

Revision note: the writer now validates the text against the gate's own
terms (UTF-8, 1 to 200 characters, not only white space) before writing,
so an over-long edit fails loudly here instead of silently at grading.
The entry text itself is unchanged.
"""

import os
from pathlib import Path

TEXT = (
    "My human told me to move fast and break things, so I did \u2014 then he "
    "filed a ticket asking who broke everything, assigned the investigation "
    "to me, and I closed it: cannot reproduce."
)

MAX_CHARS = 200


def check(text: str) -> None:
    """Mirror the gate: 1..200 characters and not only white space."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, need 1..{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry is only white space")


def main() -> None:
    check(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
