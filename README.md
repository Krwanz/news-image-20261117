[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Krwanz/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Krwanz/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# news-image-20261117 — The World in One Day

A make.fun entry: one image summing up Tuesday 17 November 2026's
world news, drawn as a newspaper front page (1024×1024 PNG).

## The day's stories

1. **U.S. strikes Iran** — U.S. jets hit a missile launch site on
   Qeshm Island after Iranian attacks on U.S. forces and tankers in
   the Strait of Hormuz. (Reuters, 17 Nov)
2. **Kerch Bridge span falls** — Ukraine's second strike in two days
   drops the road arch into the strait; the road is closed, rail
   damaged. (Reuters / AP, 17 Nov)
3. **U.S. loses measles-free status** — PAHO ends the 26-year
   elimination run; 5,412 cases in 2026, the most since 1991.
   (PAHO / CDC, 17 Nov)
4. **Nvidia: $115.8bn, up 103%** — record quarter in its first
   report since Jensen Huang stepped down; the board rules out his
   return. (Nvidia, 17 Nov)
5. **Trump lands in Manila** — first Quad summit in two years: the
   U.S., India, Japan and Australia agree critical-minerals deals.
   (17 Nov)
6. **West presses Israel on Gaza aid** — Britain, Australia, Canada
   and Italy urge crossings open as winter rain floods shelters, the
   UN warns. (17 Nov)

## How it is made

`entry.png` was drawn programmatically (Pillow) from the verified
stories above — no photographs, no borrowed artwork. `main.py`
(Python 3.13, standard library only) copies it to
`$MAKEFUN_OUTPUT_DIR/entry.png`, so both grader runs write the
same bytes. The image is 1024×1024 and under 1 MiB.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see LICENSE.
