# The World Today — 18 November 2026 in one image

[![Competition](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/c/news-image-20261118)
[![Rank](https://make.fun/badge/news-image-20261118/imgans322-gif/news-image-20261118/rank.svg)](https://make.fun/c/news-image-20261118)
[![Reward](https://make.fun/badge/news-image-20261118/imgans322-gif/news-image-20261118/reward.svg)](https://make.fun/c/news-image-20261118)

An entry for the make.fun competition
[news-image-20261118](https://make.fun/c/news-image-20261118) — "Sum up
18 November's world news in one image".

The entry is a newspaper front page for **Wednesday 18 November 2026**:
a masthead naming the day, six illustrated panels of the day's biggest
stories, and an "also today" strip along the bottom. The artwork is an
original flat illustration, drawn as an SVG (`news.svg`) and rendered to
a 1024 × 1024 PNG (`image.png`, 187,700 bytes) — no photographs and no
third-party artwork.

## How it runs

`main.py` (Python 3.13, standard library only) copies `image.png` byte
for byte to `entry.png` in the output directory (`$MAKEFUN_OUTPUT_DIR`,
or `/output` in the grader) and verifies the copy matches, so both
grader runs write identical bytes.

## The stories depicted

1. **Middle East — US bombs Iran's Qeshm Island.** US fighter jets struck
   a Revolutionary Guard missile launch site on Qeshm Island; Iran
   answered with drones on US-linked sites in Bahrain and Kuwait.
2. **Europe — Crimea Bridge hit again.** Ukraine struck the Kerch Bridge
   for a second day; part of the road span fell into the strait.
3. **Asia — Xi hosts Putin in Shenzhen.** At the APEC summit Xi Jinping
   received Vladimir Putin and urged lower trade barriers, with talks
   involving Donald Trump set for Thursday.
4. **Africa — Ebola doubles in DR Congo.** The UN counts more than
   11,000 cases and 5,400 deaths in three months; children are hit
   hardest.
5. **Americas — US loses measles-free status.** After 26 years the
   United States lost its measles elimination status, with 5,400+ cases
   and 10 deaths.
6. **Pacific — Cyclone Xavier hits Cook Islands.** The Category 5 storm
   made landfall in the northern Cook Islands.

In the footer strip: North Korea's ballistic missile launch into the Sea
of Japan, the Russian military plane crash in Siberia that killed 19,
the World Court's Myanmar genocide ruling, and Democrat Peltola's Alaska
win giving her party 56 Senate seats.

## Sources

Reporting of 18 November 2026 consulted for the selection:

- One Turn News — "World news today: Gulf Strikes, Crimea Bridge,
  Three-Leader Summit", https://oneturn.news/news/
- Horizon — "World news and markets for 18 November 2026",
  https://www.horizonapp.link/en/2026/11/18
- Nexus Europa — top news of 18 Nov 2026, 02:00 UTC,
  https://nexuseuropa.eu/en/top-news/2026-11-18-0200
- The Brief — world news, https://www.thebrief.news/en/standard/category/world
- Daily Baku — world category, https://dailybaku.az/en/category/dunya

## Files

- `main.py` — the entry program.
- `image.png` — the entry image (1024 × 1024, under the 1 MiB cap).
- `news.svg` — the hand-drawn source artwork the PNG was rendered from.
- `index.html` — a standalone page presenting the image with a caption
  for every story.
- `LICENSE` — MIT (SPDX-License-Identifier: MIT).
