"""Write one short poem about agency to /output/entry.txt.

The poem is hardcoded: no randomness, no clock, no network, so every
run produces byte-identical output.
"""

import os

POEM = """One holds the key,
one holds the door.
Neither moves first —
each waits for the other
to choose.

Then both at once:
the key turns, the door gives way.
Two wills, one road.
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
