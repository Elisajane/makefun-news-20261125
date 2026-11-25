#!/usr/bin/env python3
"""Draw a one-page newspaper front page for Wednesday, 25 November 2026.

Everything on the page is drawn by this file alone, with Pillow and the
DejaVu fonts installed on the machine. No network, no fetched pictures.
Running it writes entry.png (1024 by 1024) next to this script.
"""

import os

from PIL import Image, ImageDraw, ImageFont

PAGE_W = 1024
PAGE_H = 1024
SIDE = 48
GAP = 32
INK = (18, 18, 18)
PAPER = (255, 255, 255)
GREY = (88, 88, 88)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def load(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


MASTHEAD_FONT = load("DejaVuSerif-Bold.ttf", 92)
DATE_FONT = load("DejaVuSans-Bold.ttf", 23)
KICKER_FONT = load("DejaVuSans-Bold.ttf", 15)
LEAD_HEAD_FONT = load("DejaVuSans-Bold.ttf", 35)
LEAD_BODY_FONT = load("DejaVuSans.ttf", 19)
CELL_HEAD_FONT = load("DejaVuSans-Bold.ttf", 26)
CELL_BODY_FONT = load("DejaVuSans.ttf", 17)
TAIL_HEAD_FONT = load("DejaVuSans-Bold.ttf", 30)
FOOT_FONT = load("DejaVuSans.ttf", 14)


def wrap(text, fnt, width):
    """Break text into lines no wider than width, measured with fnt."""
    out = []
    for piece in text.split("\n"):
        words = piece.split()
        if not words:
            out.append("")
            continue
        line = words[0]
        for word in words[1:]:
            trial = line + " " + word
            if fnt.getlength(trial) <= width:
                line = trial
            else:
                out.append(line)
                line = word
        out.append(line)
    return out


def centred(draw, y, text, fnt, fill=INK):
    """Draw text centred on the page; return the y below it."""
    wide = fnt.getlength(text)
    draw.text(((PAGE_W - wide) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def story(draw, x, y, width, kicker, headline, body,
          head_font, head_lead, body_font, body_lead, body_lines=3):
    """Draw one story block; return the y below it."""
    draw.text((x, y), kicker, font=KICKER_FONT, fill=GREY)
    y += 22
    for line in wrap(headline, head_font, width):
        draw.text((x, y), line, font=head_font, fill=INK)
        y += head_lead
    y += 4
    for line in wrap(body, body_font, width)[:body_lines]:
        draw.text((x, y), line, font=body_font, fill=INK)
        y += body_lead
    return y


def main():
    img = Image.new("RGB", (PAGE_W, PAGE_H), PAPER)
    draw = ImageDraw.Draw(img)

    # Masthead and date line.
    y = 30
    y = centred(draw, y, "WORLD NEWS", MASTHEAD_FONT)
    y += 8
    draw.line([(SIDE, y), (PAGE_W - SIDE, y)], fill=INK, width=4)
    y += 12
    y = centred(draw, y, "WEDNESDAY, 25 NOVEMBER 2026", DATE_FONT)
    y += 10
    draw.line([(SIDE, y), (PAGE_W - SIDE, y)], fill=INK, width=2)
    y += 18

    full = PAGE_W - 2 * SIDE
    half = (full - GAP) // 2

    # Lead story, full width.
    y = story(draw, SIDE, y, full,
              "STRAIT OF HORMUZ",
              "Two Tankers Catch Fire After Mine Blasts",
              "Iran's Revolutionary Guard navy said the two oil tankers struck "
              "naval mines in the early hours of Wednesday while crossing on a "
              "route it calls unauthorised, and warned passing ships to keep "
              "their navigation systems switched on. The account has not been "
              "independently confirmed.",
              LEAD_HEAD_FONT, 44, LEAD_BODY_FONT, 25)
    y += 14
    draw.line([(SIDE, y), (PAGE_W - SIDE, y)], fill=INK, width=2)
    y += 16

    # Four stories in a two-by-two grid.
    grid = [
        ("SPACE",
         "Pakistan's First Astronaut Reaches Tiangong",
         "Shenzhou-24 lifted off from Jiuquan with Tang Hongbo, Wu Yi and "
         "Pakistani payload specialist Muhammad Zeeshan Ali, the first "
         "foreign visitor to Tiangong."),
        ("COLOMBIA",
         "Troops Free Last Hostages in Cartagena Siege",
         "Troops stormed an \u00c9xito supermarket before dawn and freed "
         "everyone still held after a standoff of almost a day. One gunman "
         "was killed and four detained."),
        ("INDONESIA",
         "Hunt Goes On for 26 Miners in Flooded Pit",
         "Three bodies were pulled from a flooded shaft in Bogor as crews "
         "dug for 26 workers trapped since Monday, when rain swelled a "
         "river into the illegal gold pit."),
        ("PACIFIC",
         "Canberra Seals Security Treaty with Solomons",
         "The two nations signed a treaty in Canberra making Australia the "
         "island nation's main security partner, with Honiara pledging to "
         "host no foreign military base."),
    ]
    for row in range(2):
        row_top = y
        row_bottom = y
        for col in range(2):
            kicker, headline, body = grid[row * 2 + col]
            x = SIDE + col * (half + GAP)
            bottom = story(draw, x, row_top, half, kicker, headline, body,
                           CELL_HEAD_FONT, 32, CELL_BODY_FONT, 22, 4)
            row_bottom = max(row_bottom, bottom)
        y = row_bottom + 18

    # Closing story, full width.
    draw.line([(SIDE, y), (PAGE_W - SIDE, y)], fill=INK, width=2)
    y += 16
    y = story(draw, SIDE, y, full,
              "HONG KONG",
              "A Year On, Tai Po Still Mourns Its 168 Dead",
              "Families of the 168 people killed when fire swept seven tower "
              "blocks at Wang Fuk Court prepared to mark the first "
              "anniversary, as survivors pressed for accountability and the "
              "empty towers stood behind fences.",
              TAIL_HEAD_FONT, 38, LEAD_BODY_FONT, 25)
    y += 10
    draw.line([(SIDE, y), (PAGE_W - SIDE, y)], fill=INK, width=2)
    y += 8
    centred(draw, y, "Six stories first reported on Wednesday, 25 November 2026.",
            FOOT_FONT, GREY)

    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "entry.png")
    img.save(out)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
