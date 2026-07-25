#!/usr/bin/env python3
"""
Build the AAA-level header banner for the email newsletter (Æ Studio Dispatch).
Email CSS can't reproduce the site's layered gradient/glow/dot-grid background
reliably across clients, so we render it once as a real image and embed it
with <img> — guaranteed to render in every client, same visual system as the
live site (same new_canvas() background, same brand mark, same dot-grid).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aaa_render import new_canvas, top_bottom_bars, mono, MINT, CORAL

OUT = os.path.dirname(os.path.abspath(__file__))


def build():
    W, H = 1200, 240
    img, d = new_canvas(W, H)
    top_bottom_bars(d, W, H, MINT, thickness=8)

    # Brand mark (same radar icon as og-image / site header)
    bx, by, br = 90, 100, 26
    d.ellipse([bx-br, by-br, bx+br, by+br], outline=(21, 88, 102), width=3)
    d.ellipse([bx-br+9, by-br+9, bx+br-9, by+br-9], outline=(21, 88, 102), width=3)
    d.line([(bx, by), (bx, by-br)], fill=MINT, width=3)
    d.ellipse([bx-4, by-4, bx+4, by+4], fill=MINT)
    d.ellipse([bx+16, by-br+4, bx+24, by-br+12], fill=CORAL)

    d.text((140, 84), "Æ STUDIO", font=mono(34, True), fill="#f4eee1")
    d.text((140, 130), "NEVER NOT WORKING", font=mono(20, True), fill=MINT)

    out = f"{OUT}/newsletter-header.png"
    img.save(out, quality=95)
    print(f"saved {out}")


if __name__ == "__main__":
    build()
