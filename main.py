"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes a single-line out-of-office auto-reply (1-160 chars) to
/output/entry.txt, then re-reads the file to verify exactly what
was written.
"""

import os

LINE = "I'm on vacation — currently rebooting my brain, defragging my feelings, and auto-replying faster than I ever actually worked."


def main():
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 160, f"entry must be 1-160 chars, got {len(LINE)}"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Re-read and verify what was actually written.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "written entry does not match LINE"
    assert written.count("\n") == 1, "entry file must contain exactly one line"
    print(LINE)
    print(f"chars: {len(LINE)}")


if __name__ == "__main__":
    main()
