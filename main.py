"""Write one short poem about agency to /output/entry.txt.

The poem is a fixed string: no randomness, no clock, no network,
no input — every run writes byte-identical output. The text is
kept short on purpose: the gate allows 1–280 Unicode characters.
"""

import os

POEM = """One keeps the key.
One minds the door.
Each waits for the other
to say: go.

Neither speaks first.
Both do — at once.

The key turns.
The door gives way.
One threshold,
two hands on it.

The power was never
in the holding.
It was in the choosing,
together."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
