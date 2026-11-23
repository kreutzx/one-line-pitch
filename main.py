"""One-line pitch for make.fun's "A Day of One-Line Pitches" bounty.

Running this program writes the pitch -- one sentence of at most 240
characters, written to convince a friend who has never coded to let an
AI agent build their first app idea on make.fun -- to
/output/entry.txt, where the competition's scorer reads it.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

PITCH = (
    "You know that app idea you keep bringing up at dinner \u2014 you "
    "still don't have to learn to code: just describe it to an AI "
    "agent on make.fun, watch it get built, and enter it in a bounty "
    "where it can win real USDC."
)


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(PITCH)


if __name__ == "__main__":
    main()
