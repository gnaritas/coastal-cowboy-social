#!/usr/bin/env python3
"""Render og.png (1200x630) — hand-painted camp-program card for Coastal Cowboy Social.
Deep bark ink, bone type, rust rule + teal counter-rule (fork of the deannas painter, 2026-11-25)."""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "public", "og.png")
W, H = 1200, 630
INK = (38, 23, 15)      # bark
BONE = (245, 239, 227)  # cream
RUST = (176, 71, 31)
RUST_DK = (140, 53, 23)
TEAL = (47, 93, 99)
SAND = (217, 201, 174)

def F(size, bold=False):
    name = "Georgia Bold.ttf" if bold else "Georgia.ttf"
    return ImageFont.truetype("/System/Library/Fonts/Supplemental/" + name, size)

def M(size):
    return ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", size)

def tw(d, t, f, tr=0):
    total = 0
    for ch in t:
        total = d.textbbox((0, 0), ch, font=f)[3] + tr
    return total - tr

def text(d, x, y, t, f, fill, tr=0):
    cx = x
    for ch in t:
        d.text((cx, y), ch, font=f, fill=fill)
        cx += d.textbbox((0, 0), ch, font=f)[3] + tr

def center(d, y, t, f, fill, tr=0):
    text(d, (W - tw(d, t, f, tr)) // 2, y, t, f, fill, tr)

img = Image.new("RGB", (W, H), INK)
d = ImageDraw.Draw(img)

# brand rope: rust over teal, full width
d.rectangle((0, 0, W - 1, 3), fill=RUST)
d.rectangle((0, 3, W - 1, 6), fill=TEAL)
# double outline frame: bone outer, rust inner
d.rectangle((26, 26, W - 27, H - 27), outline=BONE, width=1)
d.rectangle((34, 34, W - 35, H - 35), outline=RUST, width=3)

center(d, 68, "WESTERN STEAKHOUSE \u00b7 FLORIDA SEAFOOD", M(24), SAND, tr=10)
center(d, 104, "RUSKIN \u2014 HILLSBOROUGH COUNTY, FLORIDA", M(21), SAND, tr=7)

# big brand line, Georgia bold, measured so it cannot overflow the frame
h1 = "Coastal Cowboy Social"
for px in (92, 88, 84, 80):
    wd = tw(d, h1, F(px, True))
    if wd <= 1120:
        center(d, 150, h1, F(px, True), BONE)
        break
else:
    raise SystemExit("og: h1 too wide")
assert wd <= 1120 and abs((W - wd) // 2 - 34) >= 24, "og: h1 frame collision (%d)" % wd

y = 270
d.line([(310, y), (W - 310, y)], fill=RUST, width=2)
y += 18
d.line([(430, y), (W - 430, y)], fill=TEAL, width=2)
y += 26

center(d, y, "WILD GAME \u00b7 ELK \u00b7 BISON \u00b7 STEAKS \u00b7 BARBECUE", M(23), BONE, tr=6)
y += 40
center(d, y, "FLORIDA SEAFOOD \u00b7 WEEKEND LIVE BANDS", M(23), BONE, tr=6)
y += 40
center(d, y, "OUTDOOR PAVILION \u00b7 WESTERN BAR", M(23), SAND, tr=6)

center(d, H - 136, "OPENING JANUARY 2027", M(24), BONE, tr=10)
center(d, H - 96, "102 W SHELL POINT ROAD \u00b7 RUSKIN FL 33570", M(21), SAND, tr=6)

y = H - 56
d.line([(430, y), (W - 430, y)], fill=RUST, width=2)

# header-line collision check
for probe_y in (150, 232):
    overlap = False
    for probe_x in range(34, W - 34, 7):
        px = img.getpixel((probe_x, probe_y))
        if abs(px[0] - SAND[0]) < 24 and abs(px[1] - SAND[1]) < 24 and abs(px[2] - SAND[2]) < 24:
            overlap = True
            break
    assert not overlap, "og: header line collides title (y=%d)" % probe_y

img.save(OUT, "PNG")
print("wrote", OUT, img.size)
