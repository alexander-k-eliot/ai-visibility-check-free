#!/usr/bin/env python3
"""Build the GitHub README banner image on the AAA visual system."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aaa_render import new_canvas, top_bottom_bars, mono, serif, sans, brand_lockup, MINT, CORAL, INK, DIM

OUT = os.path.dirname(os.path.abspath(__file__))


def build():
    W, H = 1600, 400
    img, d = new_canvas(W, H)
    top_bottom_bars(d, W, H, MINT, thickness=6)

    brand_lockup(d, 90, 60, icon_scale=2.4, name_size=36)

    d.text((90, 160), "Free AI Visibility Check", font=serif(56, True), fill=INK)
    d.text((90, 236), "Will ChatGPT, Perplexity and Claude find your site?", font=sans(26), fill=DIM)
    d.text((90, H - 60), "alexander-k-eliot.github.io/ai-visibility-check-free", font=mono(18), fill=DIM)

    out = f"{OUT}/readme-banner.png"
    img.save(out, quality=95)
    print(f"saved {out}")


if __name__ == "__main__":
    build()
