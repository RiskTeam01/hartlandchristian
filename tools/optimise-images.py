#!/usr/bin/env python3
"""Resize and re-encode assets/img to the sizes the pages actually display.

The originals came off the old site at up to 1600-2400px regardless of how
small they render, which made the home page ~6.8MB. Filenames and formats are
preserved, so no markup changes are needed — run it and rebuild.

    python3 tools/optimise-images.py          # report only
    python3 tools/optimise-images.py --write  # rewrite the files
"""
import os, sys
from PIL import Image

IMG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")

# max width in CSS pixels x2, from what each image actually renders at
TARGET = {
    # full-bleed heroes
    "academics-hero.jpg": 1600, "admissions-hero.jpg": 1400, "church-hero.jpg": 1280,
    "vball.jpg": 1400,
    # team photographs
    "basketball-team.jpg": 1400, "volleyball-team.jpg": 1400,
    # "through the years" collage — renders around 300px wide
    "bball-year-1.jpg": 620, "bball-year-2.jpg": 620, "bball-year-3.jpg": 620,
    "bball-year-4.jpg": 620, "bball-year-5.jpg": 620,
    "vball-year-1.jpg": 620, "vball-year-2.jpg": 620, "vball-year-3.jpg": 620,
    "vball-year-4.jpg": 620, "vball-year-5.jpg": 620,
    # home page cards — 344px on screen
    "chapel.jpg": 700, "classroom.jpg": 700, "visit.jpg": 700, "kids.jpg": 1150,
    "early-learning.jpg": 1100, "athletics-card.png": 700,
    # testimonials — 561px slide
    "review-brooks.jpg": 1150, "review-butler.jpg": 1150, "review-curtis.jpg": 1150,
    "review-sinclair.png": 1020,
    # missionaries — 441px frame
    "mission-king.png": 900, "mission-page.jpg": 900, "mission-gbeblewou.jpg": 610,
    "mission-briscoe.jpg": 560, "mission-steward.jpg": 900,
    # about / church imagery
    "church-about.jpg": 1220, "church-exterior.jpg": 1100, "purpose-bible.jpg": 880,
    "pillar-character.jpg": 620, "pillar-spiritual.jpg": 1220, "enrollment.jpg": 800,
    # crests
    "conquerors_logo.png": 500, "conquerors-crest.png": 620, "church-crest.png": 220,
    "hcs_favicon.png": 200,
    # faded section backgrounds — they sit at 20-50% opacity behind text
    "bg-alaska.jpg": 1200, "bg-boston.jpg": 1100, "bg-south-africa.jpg": 1200,
    "bg-west-africa.jpg": 1200, "bg-south-america.jpg": 1200, "bg-maine.jpg": 1200,
    "bg-missions-map.jpg": 1200, "bg-scripture.jpg": 1200, "bg-empowering.jpg": 1200,
}
# backgrounds are heavily faded, so they take harder compression without showing
SOFT = {n for n in TARGET if n.startswith("bg-")}


def has_alpha(im):
    if im.mode in ("RGBA", "LA"):
        a = im.getchannel("A")
        return a.getextrema()[0] < 255
    return im.mode == "P" and "transparency" in im.info


def process(name, write):
    path = os.path.join(IMG, name)
    if not os.path.exists(path):
        return None
    before = os.path.getsize(path)
    im = Image.open(path)
    w, h = im.size
    target = TARGET.get(name, 1400)

    if w > target:
        im = im.resize((target, round(h * target / w)), Image.LANCZOS)

    ext = name.rsplit(".", 1)[1].lower()
    if ext in ("jpg", "jpeg"):
        im = im.convert("RGB")
        q = 72 if name in SOFT else 82
        params = dict(format="JPEG", quality=q, optimize=True, progressive=True)
    else:
        if has_alpha(im):
            im = im.convert("RGBA")
            # keep transparency; RGBA only supports the octree quantiser
            im = im.quantize(colors=256, method=Image.FASTOCTREE)
        else:
            im = im.convert("RGB").quantize(colors=256, method=Image.MEDIANCUT,
                                            dither=Image.FLOYDSTEINBERG)
        params = dict(format="PNG", optimize=True)

    if write:
        im.save(path, **params)
        after = os.path.getsize(path)
    else:
        import io
        buf = io.BytesIO(); im.save(buf, **params); after = buf.tell()
    return before, after, im.size


def main():
    write = "--write" in sys.argv
    rows, tb, ta = [], 0, 0
    for name in sorted(os.listdir(IMG)):
        if not name.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        r = process(name, write)
        if not r:
            continue
        before, after, size = r
        tb += before; ta += after
        if before - after > 20 * 1024:
            rows.append((before - after, name, before, after, size))
    rows.sort(reverse=True)
    for saved, name, before, after, size in rows:
        print(f"  {name:26s} {before/1024:>7.0f}K -> {after/1024:>6.0f}K   ({size[0]}x{size[1]})")
    print(f"\n  TOTAL {tb/1024/1024:.1f} MB -> {ta/1024/1024:.1f} MB"
          f"   saved {(tb-ta)/1024/1024:.1f} MB ({100*(tb-ta)/tb:.0f}%)")
    if not write:
        print("\n  (dry run — pass --write to apply)")


if __name__ == "__main__":
    main()
