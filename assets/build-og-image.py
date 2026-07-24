#!/usr/bin/env python3
"""
Build the site-wide Open Graph / social-share image (1200x630).
Visual system: matches alexander-k-eliot.github.io exactly (same palette
and drawing approach as build-ph-images.py).
"""
import os, math
from PIL import Image, ImageDraw, ImageFont

BG    = (6,  55,  64)
CARD2 = (8,  48,  58)
INK   = (238,246,244)
DIM   = (159,188,186)
MINT  = (46, 230,168)
CORAL = (232,106, 90)

SCORE = 62
OUT = os.path.dirname(os.path.abspath(__file__))

def font(size, bold=False):
    paths = [
        "/System/Library/Fonts/Supplemental/Georgia Bold.ttf" if bold else
        "/System/Library/Fonts/Supplemental/Georgia.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for p in paths:
        try:
            idx = 1 if (bold and "Helvetica" in p) else 0
            return ImageFont.truetype(p, size, index=idx)
        except Exception:
            continue
    return ImageFont.load_default()

def score_arc(d, cx, cy, r, score, stroke=20):
    box = [cx-r, cy-r, cx+r, cy+r]
    d.arc(box, start=0, end=360, fill=CARD2, width=stroke)
    end_deg = 270 + (score / 100) * 360
    d.arc(box, start=270, end=end_deg, fill=MINT, width=stroke)

def build():
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, W, 7], fill=MINT)

    # Dot-grid texture (subtle, matches site background::after)
    for gx in range(0, W, 42):
        for gy in range(40, H - 40, 42):
            d.ellipse([gx-1, gy-1, gx+1, gy+1], fill=(60, 110, 105))

    # Brand mark (radar icon, matches header brand-icon)
    bx, by, br = 62, 58, 20
    d.ellipse([bx-br, by-br, bx+br, by+br], outline=(21, 88, 102), width=2)
    d.ellipse([bx-br+7, by-br+7, bx+br-7, by+br-7], outline=(21, 88, 102), width=2)
    d.line([(bx, by), (bx, by-br)], fill=MINT, width=2)
    d.ellipse([bx-3, by-3, bx+3, by+3], fill=MINT)
    d.ellipse([bx+13, by-br+3, bx+19, by-br+9], fill=CORAL)

    d.text((94, 46), "Æ STUDIO  ·  NEVER NOT WORKING", font=font(20), fill=MINT)

    # Headline
    d.text((60, 130), "Will AI assistants find", font=font(56, bold=True), fill=INK)
    d.text((60, 196), "your website?", font=font(56, bold=True), fill=INK)
    d.text((60, 274), "Free 60-second check. No signup. Instant score.", font=font(24), fill=DIM)

    # Score ring, right side
    cx, cy, r = 950, 340, 130
    score_arc(d, cx, cy, r, SCORE, stroke=24)
    f_num = font(84, bold=True)
    num_str = str(SCORE)
    bb = d.textbbox((0, 0), num_str, font=f_num)
    nw, nh = bb[2]-bb[0], bb[3]-bb[1]
    d.text((cx - nw//2, cy - nh//2 - 12), num_str, font=f_num, fill=INK)
    f_denom = font(22)
    denom = "/100"
    bb2 = d.textbbox((0, 0), denom, font=f_denom)
    dw = bb2[2]-bb2[0]
    d.text((cx - dw//2, cy + nh//2 + 16), denom, font=f_denom, fill=DIM)
    f_label = font(20)
    label = "AI visibility score"
    bb3 = d.textbbox((0, 0), label, font=f_label)
    lw = bb3[2]-bb3[0]
    d.text((cx - lw//2, cy + r + 20), label, font=f_label, fill=DIM)

    d.text((60, H - 56), "alexander-k-eliot.github.io/ai-visibility-check-free", font=font(19), fill=DIM)
    d.rectangle([0, H-7, W, H], fill=MINT)

    out = f"{OUT}/og-image.png"
    img.save(out, quality=95)
    print(f"saved {out}")

if __name__ == "__main__":
    build()
