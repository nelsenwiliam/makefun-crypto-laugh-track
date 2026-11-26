"""Laugh Track: The Crypto Trading Joke Contest.

Writes one one-line joke about crypto and trading life (under 200
characters) to /output/entry.txt, where the make.fun judge compares it
two at a time against the other entries.

The line was picked from 10 candidates against the judge brief: it has
a clear setup (a stop-loss set for protection) and a turn (the market
hunts it, pumps without the trader, and leaves), a recognisable trading
detail (the stop-loss hunt), tight phrasing, and the punchline at the end.
"""

import os

JOKE = (
    "I set a stop-loss to protect my trade \u2014 the market hunted it, "
    "pumped without me, and left. Turns out it's the only thing in my "
    "portfolio that ever executed perfectly."
)


def main() -> None:
    # The gate requires 1 to 200 characters of UTF-8 text, not only
    # whitespace; fail loudly here instead of shipping an invalid entry.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
