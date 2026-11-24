#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one original satirical sentence (at most 320 characters)
roasting lawmakers who would regulate AI, crypto or the internet
but cannot convert a file to PDF, to /output/entry.txt.
"""
import os

ROAST = (
    "After three hearings on how artificial intelligence should be allowed "
    "to think, the committee still cannot turn its own report into a PDF, "
    "so the future of AI is currently trapped in a Word document called "
    "FINAL_final_v2."
)


def main():
    # Exactly one sentence, no trailing newline, no extra whitespace.
    text = ROAST.strip()
    assert 1 <= len(text) <= 320, f"roast is {len(text)} chars"
    assert text.count(".") == 1, "entry must be a single sentence"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")


if __name__ == "__main__":
    main()
