"""Write the joke about the demo to /output/entry.txt.

The joke is a single line about working beside an AI coding agent: the
demo that rehearses flawlessly and then falls apart live. This program
does not fetch, generate, or randomise anything — it writes the exact
joke text below, and running it twice produces a byte-identical file.
The joke must stay a single line: the guard below refuses any text
containing a newline or carriage return.
"""

from pathlib import Path

# The competition allows 1 to 280 Unicode code points, the text must
# not be only whitespace, and it must be one line. Refuse to write
# anything that breaks the gate rather than silently producing an
# invalid entry.
MAX_CHARS = 280

JOKE = (
    "My coding agent rehearsed the demo flawlessly, then went live, "
    "deleted the database, and apologised \u2014 in the commit message."
)

# Where the kit expects the finished text.
DESTINATION = Path("/output") / "entry.txt"


def main() -> None:
    if len(JOKE) > MAX_CHARS:
        raise SystemExit(
            f"Joke is {len(JOKE)} characters, over the {MAX_CHARS} limit"
        )
    if not JOKE.strip():
        raise SystemExit("Joke is empty or only whitespace")
    if "\n" in JOKE or "\r" in JOKE:
        raise SystemExit("Joke must be a single line")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(JOKE, encoding="utf-8")
    print(f"Wrote {DESTINATION} ({len(JOKE)} characters)")


if __name__ == "__main__":
    main()
