"""The Meeting That Should Have Been an Email.

Writes exactly one line of plain text -- a single joke about a
meeting that should have been an email -- to /output/entry.txt.
Python standard library only; deterministic, no input, no network.
"""

from pathlib import Path

JOKE = (
    "We held a meeting so our manager could read the email out loud, "
    "slowly, to the very people who wrote it."
)


def main() -> None:
    # Gate, checked locally before writing: one line, 1-200 chars,
    # plain text, no second sentence and no trailing whitespace.
    assert "\n" not in JOKE and 1 <= len(JOKE) <= 200, "joke breaks the gate"
    assert JOKE == JOKE.strip() and JOKE.count(".") == 1, "joke is not one sentence"
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
