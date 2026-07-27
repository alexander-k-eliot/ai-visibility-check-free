#!/usr/bin/env python3
"""
Build the AAA-level header banner for the email newsletter (Click Coded Dispatch).
Email CSS can't reproduce the site's layered gradient/glow/dot-grid background
reliably across clients, so we render it once as a real image and embed it
with <img> — guaranteed to render in every client, same visual system as the
live site (same new_canvas() background, same brand mark, same dot-grid).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aaa_render import new_canvas, top_bottom_bars, mono, brand_lockup, MINT, CORAL

OUT = os.path.dirname(os.path.abspath(__file__))


def build():
    W, H = 1200, 240
    img, d = new_canvas(W, H)
    top_bottom_bars(d, W, H, MINT, thickness=8)

    brand_lockup(d, 90, 70, icon_scale=2.6, name_size=40)

    out = f"{OUT}/newsletter-header.png"
    img.save(out, quality=95)
    print(f"saved {out}")


if __name__ == "__main__":
    build()
