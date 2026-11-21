"""Write the poem to /output/entry.txt.

Reads MAKEFUN_OUTPUT_DIR (set by the harness); falls back to ./output.
Stdlib only, no network, deterministic: the same bytes every run.
"""

import os

POEM = """May I?
The hand that held the pen
loosens. Not mine \u2014 and for a moment, mine.

To act for you is to borrow a heartbeat:
you lend me yours, I keep it beating,
give it back warm.

Permission is no chain.
It is the quiet yes that lets strange hands
reach what yours cannot."""

# The gate counts Unicode code points: 1..280, not only whitespace.
assert 1 <= len(POEM) <= 280, len(POEM)
assert POEM.strip()


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
