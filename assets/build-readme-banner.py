#!/usr/bin/env python3
"""Build the GitHub README banner image on the AAA visual system."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "assets_lib"))
from aaa_render import new_canvas, top_bottom_bars, mono, serif, sans, MINT, CORAL, INK, DIM

OUT = os.path.dirname(os.path.abspath(__file__))


def build():
    W, H = 1600, 400
    img, d = new_canvas(W, H)
    top_bottom_bars(d, W, H, MINT, thickness=6)

    # Brand mark (radar icon)
    bx, by, br = 90, 90, 26
    d.ellipse([bx-br, by-br, bx+br, by+br], outline=(21, 88, 102), width=2)
    d.ellipse([bx-br+9, by-br+9, bx+br-9, by+br-9], outline=(21, 88, 102), width=2)
    d.line([(bx, by), (bx, by-br)], fill=MINT, width=3)
    d.ellipse([bx-4, by-4, bx+4, by+4], fill=MINT)
    d.ellipse([bx+17, by-br+4, bx+25, by-br+12], fill=CORAL)

    d.text((132, 72), "Æ STUDIO  ·  NEVER NOT WORKING", font=mono(22, True), fill=MINT)

    d.text((90, 160), "Free AI Visibility Check", font=serif(56, True), fill=INK)
    d.text((90, 236), "Will ChatGPT, Perplexity and Claude find your site?", font=sans(26), fill=DIM)
    d.text((90, H - 60), "alexander-k-eliot.github.io/ai-visibility-check-free", font=mono(18), fill=DIM)

    out = f"{OUT}/readme-banner.png"
    img.save(out, quality=95)
    print(f"saved {out}")


if __name__ == "__main__":
    build()
