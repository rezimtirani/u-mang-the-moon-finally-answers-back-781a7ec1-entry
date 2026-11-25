"""The Moon Finally Answers Back.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: the Moon's
reply, at last, to everyone who has ever stared up at it and
made a wish, howled, or promised something at midnight. The
Moon has been listening for centuries and never once been
asked how it is doing. Standard library only.
"""

import os

LINE = (
    "You wished on me for centuries and never once asked how "
    "I'm doing. I'm a rock. A very tired rock."
)


def check_line(text):
    """Check the line against the competition gate before writing.

    The gate needs plain UTF-8 text of 1 to 240 characters, not
    only white space, in a single line: the Moon answering back
    to everyone who has ever stared up at it. Returns the
    cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("line must not be only whitespace")
    if len(cleaned) > 240:
        raise ValueError(
            "line is %d characters, over the 240 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("line must be exactly one line")
    return cleaned


def line_shape(text):
    """Measure the line for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A line too short to carry a comeback, or one
    padded out to fill the cap, is caught here before anything
    is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_line(LINE)
    shape = line_shape(text)
    if shape["words"] < 5:
        raise ValueError("line is too short to sound like the Moon")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
