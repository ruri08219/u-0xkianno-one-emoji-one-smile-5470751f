#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the smiling face with a
tear (U+1F972). The judge brief asks for the single emoji most likely to
make a stranger smile, weighed in this order: warm and friendly; warmth
at first glance; universal; chosen rather than default; right for a
stranger (no intimacy, sarcasm or flirtation).

Why this emoji, against the brief's five criteria in order:
1. Warm and friendly: it is a smiling face, directly warm — it aims to
   make a stranger smile.
2. Warmth at first glance: the smile reads at once; the single tear reads
   as being genuinely moved or touched, not as sadness.
3. Universal: a touched smile reads the same for any age or background;
   no irony, no in-joke.
4. Chosen rather than default: the plain smiling face is the first smiley
   that comes to mind; this one is a deliberate pick with a reason.
5. Right for a stranger: no hug, no hearts, no flirtation — nothing that
   would read oddly from someone unknown.
"""

import os

EMOJI = "\U0001F972"  # 🥲 smiling face with tear
MAX_CHARS = 8  # the sealed gate accepts 1 to 8 characters

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if len(EMOJI) != 1:
        raise ValueError("entry must be exactly one emoji")
    if len(EMOJI) > MAX_CHARS:
        raise ValueError("entry exceeds the 8-character gate")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # Read-back verification: the file must hold exactly the emoji.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != EMOJI:
        raise ValueError("read-back mismatch")


if __name__ == "__main__":
    main()
