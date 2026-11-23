# The joke about the demo

[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/FajarRizikAinulyakin/makefun-the-joke-about-the-demo-20261123-0112-2/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/FajarRizikAinulyakin/makefun-the-joke-about-the-demo-20261123-0112-2/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

A one-line joke about working beside an AI coding agent: the demo that
rehearses flawlessly and then falls apart in front of a live room.

## The joke

> My coding agent rehearsed the demo flawlessly, then went live, deleted the database, and apologised — in the commit message.

124 characters, inside the competition's 280-character limit.

## What this entry is

`main.py` is a small standard-library-only Python program that writes the
joke to `/output/entry.txt`, creating the output folder if it does not
exist yet. It fetches nothing and generates nothing — running it twice
produces a byte-identical file. It refuses to write if the joke ever
exceeds the 280-character limit or is empty or only whitespace.

## How to run it

```bash
python3 main.py
```

The joke is then available at `/output/entry.txt`.
