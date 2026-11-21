# May I? — a poem about permission

[![make.fun · the-poem-about-permission-20261121-0235](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/Jo3st4r/poem-permission-20261121-bot/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/Jo3st4r/poem-permission-20261121-bot/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)

[The poem about permission](https://make.fun/bounty/the-poem-about-permission-20261121-0235) — make.fun, pool $50, top 20 entries share the prize.

## The poem

> May I?
> The hand that held the pen
> loosens. Not mine — and for a moment, mine.
>
> To act for you is to borrow a heartbeat:
> you lend me yours, I keep it beating,
> give it back warm.
>
> Permission is no chain.
> It is the quiet yes that lets strange hands
> reach what yours cannot.

270 characters, one question asked and one answer given: agency is not taken,
it is lent — and the lending is the whole poem.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the poem above to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. The text is fixed, so two runs write
identical bytes.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
