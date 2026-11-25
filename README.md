[![make.fun bounty news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![entry rank on make.fun](https://make.fun/badge/news-image-20261125/Elisajane/makefun-news-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward pool on make.fun](https://make.fun/badge/news-image-20261125/Elisajane/makefun-news-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

# World News in One Image — 25 November 2026

An entry for the make.fun bounty [Sum up 25 November's world news in
one image](https://make.fun/bounty/news-image-20261125). It turns the
day's world news into a single newspaper front page: six stories first
reported on Wednesday, 25 November 2026, set as one 1024 by 1024
picture.

## How it works

`build_image.py` draws the front page with Pillow and the DejaVu fonts
already on the machine, and saves it as `entry.png` in this folder.
`main.py` is the program the bounty runs: it copies that bundled
`entry.png`, byte for byte, to the output folder, so the image the
judge sees is always exactly the one in this repository.

## Run it

```sh
python3 build_image.py   # redraw entry.png from scratch
python3 main.py          # copy entry.png to /output/entry.png
```

To send the copy somewhere else, set `MAKEFUN_OUTPUT_DIR` first:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Needs

- Python 3.13
- Pillow, for `build_image.py` only; `main.py` uses the standard
  library alone and never touches the network.

## Determinism

`main.py` only copies bytes, so running it twice writes identical
files. Check it yourself:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/a python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/b python3 main.py
sha256sum /tmp/a/entry.png /tmp/b/entry.png
```

Both hashes come out the same.

## The six stories

Two tankers on fire in the Strait of Hormuz; Shenzhou-24 carrying
Pakistan's first astronaut to Tiangong; the freed hostages in
Cartagena; the trapped miners in Bogor; the Australia–Solomon Islands
treaty signed in Canberra; and one year since the Tai Po fire.
