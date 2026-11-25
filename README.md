# The Meeting That Should Have Been an Email

[![make.fun](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![rank](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/Vins1206/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![reward](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/Vins1206/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)

A make.fun entry for [The Meeting That Should Have Been an Email](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9) ($2, top 10).

## What it does

`main.py` (Python standard library only, deterministic, no network) writes
exactly one line of plain text — a single joke about a meeting that should
have been an email, 104 characters, one sentence — to `/output/entry.txt`.

> We held a meeting so our manager could read the email out loud, slowly, to the very people who wrote it.

The joke was picked from 7 drafted candidates scored against the judge's
rubric (on-topic, laugh landing on the last word, surprise, economy,
recognition). This one won: a fresh angle — the manager reading the email
aloud to the very people who wrote it — instead of the obvious complaint
that the meeting could have been an email, with the turn arriving at the
last word and every word earning its place.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

The program checks the gate itself before writing: one line, 1–200
characters, a single sentence.
