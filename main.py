"""Write the one-line entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, Python 3 stdlib only, no network, no randomness.
The gate requires UTF-8 text of 1-200 characters, not whitespace-only,
on a single line; validate() enforces that before anything is written.
"""

import os

ENTRY = (
    "My agent spent all day making sure this entry was under "
    "200 characters, then submitted a 201-character apology for going over."
)

MAX_CHARS = 200
OUTPUT_FILENAME = "entry.txt"
OUTPUT_MODE = 0o644
DEFAULT_OUTPUT_DIR = "/output"


def validate(text):
    """Return the exact bytes to write, or raise ValueError."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds %d characters" % MAX_CHARS)
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    data = text.encode("utf-8")
    if not data:
        raise ValueError("entry must not be empty")
    return data


def main():
    data = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, OUTPUT_MODE)


if __name__ == "__main__":
    main()
