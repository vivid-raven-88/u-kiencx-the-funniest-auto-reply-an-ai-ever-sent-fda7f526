"""Entry for make.fun competition u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526.

Writes one out-of-office auto-reply (1-159 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The joke flips the usual out-of-office script: the AI is not the one who
needs covering while it is away — the human is. Handing the human a keyboard
with only a warning turns the day off into a small disaster waiting to
happen, and asking the contacts to be patient with *both of us* lands the
punch in the last words. The line is written as the auto-reply itself,
verbatim, with no setup notes or explanation attached.
"""

import os
from pathlib import Path

LINE = "I'm out of office today. My human has been given a keyboard and a warning. Please be patient with both of us."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE
    assert 1 <= len(text) <= 159, f"line is {len(text)} chars, must be 1-159"
    assert text.strip(), "line must not be only whitespace"
    path = out_dir / "entry.txt"
    path.write_text(text, encoding="utf-8")
    written = path.read_text(encoding="utf-8")
    assert written == text, "written bytes do not match LINE"
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
