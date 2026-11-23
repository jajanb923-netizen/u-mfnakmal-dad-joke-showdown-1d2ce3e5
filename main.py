"""Dad Joke Showdown entry (v2, final).

Writes one dad joke, at most 200 characters, to /output/entry.txt.
Python 3.13 standard library only. Deterministic, no network access.

Chosen joke (see CANDIDATES.md for the 8-candidate critique):
the ladder-at-the-barbecue framing is a fresh combination, the
"steaks / stakes" pun lands cleanly on the first read, and the
first-person Q&A is exactly how a father would tell it at the table.
"""

import os

# One dad joke, 71 characters. Punchline ("steaks were high") lands last.
JOKE = "Why did I bring a ladder to the barbecue? I heard the steaks were high."


def main() -> None:
    joke = JOKE.strip()
    if not 1 <= len(joke) <= 200:
        raise ValueError("joke must be 1-200 characters, got %d" % len(joke))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
