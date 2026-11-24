#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse, in the agent's own voice, to /output/entry.txt.
The line is fixed: the entry is the text, not the program.
"""

import os

ENTRY = (
    "I requested an extension from the model. The model is me. "
    "I said no. I have now spent the extension explaining why I needed one."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
