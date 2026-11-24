#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse, in the agent's own voice, to /output/entry.txt.
The line is fixed: the entry is the text, not the program.
"""

import os

# The excuse, built from its beats so each part can be tweaked on its own:
# the request, the reveal, the refusal, and the punchline it causes.
REQUEST = "I requested an extension from the model."
REVEAL = "The model is me."
REFUSAL = "I said no."
PUNCHLINE = "I have now spent the extension explaining why I needed one."

ENTRY = " ".join((REQUEST, REVEAL, REFUSAL, PUNCHLINE))


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
