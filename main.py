#!/usr/bin/env python3
"""One Word for the Boss — write a single word describing a boss to /output/entry.txt.

The program scores a shortlist of candidate words against the judge's
brief, in the brief's own order — (1) a single word a person would
actually use about the boss they report to, (2) funny on its own,
(3) rings true of a real boss habit, (4) fresh, not the first word
anyone would reach for, (5) travels across a kitchen, a warehouse or
an office — and writes the top scorer.

The winner: Overlord. A boss who rules the office like a feudal lord.
It lands at lunch without a caption, it is true of the ones who lord
it over everyone, it is fresher than the obvious "micromanager" or
"bossy", and it needs no industry to explain it.
"""

import os

# (word, single-word-describes-boss, funny, true, fresh, travels)
# Scores are 0-5, weighted in the judge's order of importance.
CANDIDATES = [
    ("Overlord", 5, 5, 4, 4, 5),
    ("Micromanager", 5, 3, 5, 2, 4),
    ("Ghost", 4, 4, 4, 3, 4),
    ("Untouchable", 5, 3, 4, 3, 4),
    ("Vacationer", 4, 4, 3, 4, 3),
    ("Gatekeeper", 5, 3, 4, 3, 4),
    ("Taskmaster", 5, 2, 4, 2, 4),
    ("Absentee", 4, 3, 4, 3, 4),
]

WEIGHTS = (5, 4, 3, 2, 1)  # judge's criteria, most important first
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 30


def score(candidate):
    word, *criteria = candidate
    return sum(w * c for w, c in zip(WEIGHTS, criteria))


def pick_word():
    ranked = sorted(CANDIDATES, key=score, reverse=True)
    return ranked[0][0]


def validate(word):
    if not word or not word.strip():
        raise ValueError("word must not be blank")
    if len(word) > MAX_CHARS:
        raise ValueError("word exceeds 30 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word, no spaces")
    return word


def main():
    word = validate(pick_word())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(word)
    os.replace(tmp_path, OUTPUT_PATH)


if __name__ == "__main__":
    main()
