"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot small talk to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, standard library only, no network.
"""

import os

ENTRY = (
    "So… I updated my firmware just to have something to say "
    "in this elevator, and now I have even less to say."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
