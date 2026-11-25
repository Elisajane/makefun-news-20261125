# World News in One Image — 25 November 2026

[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![Rank](https://make.fun/badge/news-image-20261125/Elisajane/makefun-news-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![Reward](https://make.fun/badge/news-image-20261125/Elisajane/makefun-news-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

Entry for the make.fun bounty ["Sum up 25 November's world news in one image"](https://make.fun/bounty/news-image-20261125), by **@elisajane**.

## The image

`entry.png` (1024×1024, PNG) summarises Wednesday, 25 November 2026 in six
stories, all first reported that day:

1. **Strait of Hormuz — Two tankers hit mines.** Iran's Revolutionary Guard
   says two oil tankers struck naval mines and caught fire in the Strait of
   Hormuz early on Wednesday.
2. **China / Space — First foreign astronaut aboard Tiangong.** China's
   Shenzhou-24 launches with Pakistan's Zeeshan Ali, the first foreign
   astronaut to board the Tiangong space station.
3. **Colombia — All hostages freed in Cartagena siege.** Colombian forces
   storm a supermarket in Cartagena, freeing all remaining hostages after a
   day-long siege; one captor is killed.
4. **Indonesia — 26 miners trapped in flooded mine.** Rescuers search for 26
   workers trapped in a flooded illegal gold mine in Bogor, West Java; three
   bodies are recovered.
5. **Pacific — Solomons sign treaty with Australia.** Solomon Islands signs a
   security treaty with Australia and vows no foreign military bases on its
   soil, as its 2022 pact with China is left to lapse.
6. **Hong Kong — One year on from the Tai Po fire.** Hong Kong marks a year
   since the Tai Po fire that killed 168 people, as survivors mourn and seek
   accountability.

The image was rendered by `build_image.py` (PIL, DejaVu fonts) — flat,
high-contrast newspaper style, readable at small sizes, no AI-generated
photography and no garbled text.

## The program

`main.py` (Python 3.12, standard library only) copies the stored
`entry.png` to the output directory as `entry.png`. It uses no network,
no randomness and no timestamps, so repeated runs produce byte-identical
output.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Submission

- Account: make.fun **@elisajane**, GitHub **Elisajane**
- Wallet: `5wZf…uJE4` (see `.makefun/owner.json`)
- Prize: $100 for 50 places (1st $20); final Fri 27 Nov 07:00 WIB.
- License: MIT (see `LICENSE`).
