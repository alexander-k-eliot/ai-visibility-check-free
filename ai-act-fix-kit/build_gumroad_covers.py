#!/usr/bin/env python3
"""
Real Gumroad cover + thumbnail images for both AI Act Fix Kit listings.
Found missing 2026-07-28: both live listings were still showing the inherited
GEO Playbook artwork from the Duplicate they were built from.

House convention confirmed against the existing catalog (retrofit-cover.png,
checklist-cover.png, bundle-cover.png): covers are 1600x900, thumbnails
1200x1200 (Gumroad's own minimum is 600x600 -- using 2x for retina).

Real drawn differentiator between the two tiers, per the iconographic canon
(a real visual element, not a color swap or a price-only difference): Fix It
shows ONE touchpoint icon (a chat bubble -- the single thing that tier
unlocks). Fix It All shows THREE (chat bubble, image frame, document) --
the actual, honest difference between the two products, drawn, not stated.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "assets_lib"))
from aaa_render import new_canvas, top_bottom_bars, mono, serif, sans, MINT, AMBER, INK, DIM, CARD

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "listing-art")


def hourglass(d, cx, cy, size, color=AMBER):
    half = size / 2
    bar_h = size * 0.06
    d.rounded_rectangle([cx - half, cy - half, cx + half, cy - half + bar_h], radius=3, fill=color)
    d.rounded_rectangle([cx - half, cy + half - bar_h, cx + half, cy + half], radius=3, fill=color)
    d.polygon([(cx - half * 0.75, cy - half + bar_h), (cx + half * 0.75, cy - half + bar_h), (cx, cy)], outline=color, width=4)
    d.polygon([(cx - half * 0.55, cy + half - bar_h), (cx + half * 0.55, cy + half - bar_h), (cx, cy + half * 0.15)], outline=color, width=4)
    d.polygon([(cx - half * 0.42, cy - half + bar_h + 10), (cx + half * 0.42, cy - half + bar_h + 10), (cx, cy - half * 0.15)], fill=color)
    d.polygon([(cx - half * 0.5, cy + half - bar_h - 6), (cx + half * 0.5, cy + half - bar_h - 6), (cx, cy + half * 0.35)], fill=color)


def chat_bubble_icon(d, cx, cy, s, color=MINT):
    r = s * 0.5
    d.rounded_rectangle([cx - r, cy - r * 0.75, cx + r, cy + r * 0.55], radius=r * 0.35, outline=color, width=max(2, int(s * 0.06)))
    tail = [(cx - r * 0.35, cy + r * 0.5), (cx - r * 0.05, cy + r * 0.5), (cx - r * 0.2, cy + r * 0.95)]
    d.polygon(tail, fill=color)
    for i, dx in enumerate((-0.32, 0, 0.32)):
        d.ellipse([cx + r * dx - s * 0.045, cy - s * 0.02, cx + r * dx + s * 0.045, cy + s * 0.07], fill=color)


def image_icon(d, cx, cy, s, color=MINT):
    r = s * 0.5
    d.rounded_rectangle([cx - r, cy - r * 0.75, cx + r, cy + r * 0.75], radius=r * 0.2, outline=color, width=max(2, int(s * 0.06)))
    d.ellipse([cx - r * 0.55, cy - r * 0.45, cx - r * 0.25, cy - r * 0.15], outline=color, width=max(2, int(s * 0.05)))
    d.polygon([(cx - r * 0.7, cy + r * 0.55), (cx - r * 0.1, cy - r * 0.05), (cx + r * 0.25, cy + r * 0.25),
               (cx + r * 0.5, cy - r * 0.05), (cx + r * 0.7, cy + r * 0.55)], fill=color)


def doc_icon(d, cx, cy, s, color=MINT):
    w, h = s * 0.72, s * 0.92
    fold = s * 0.2
    x0, y0 = cx - w / 2, cy - h / 2
    d.polygon([(x0, y0), (x0 + w - fold, y0), (x0 + w, y0 + fold), (x0 + w, y0 + h), (x0, y0 + h)],
               outline=color, width=max(2, int(s * 0.05)))
    d.polygon([(x0 + w - fold, y0), (x0 + w, y0 + fold), (x0 + w - fold, y0 + fold)], outline=color, width=2)
    ly = y0 + fold + s * 0.14
    for frac in (0.6, 0.75, 0.45):
        d.rectangle([x0 + s * 0.1, ly, x0 + s * 0.1 + w * frac * 0.8, ly + s * 0.045], fill=color)
        ly += s * 0.16


def touchpoint_row(d, cx, cy, icons, size=70, gap=34):
    n = len(icons)
    total_w = n * size + (n - 1) * gap
    x = cx - total_w / 2 + size / 2
    for icon_fn in icons:
        icon_fn(d, x, cy, size)
        x += size + gap


def cover(out_path, title_lines, price, tag_line, icons, touchpoint_label):
    W, H = 1600, 900
    img, d = new_canvas(W, H)
    top_bottom_bars(d, W, H, MINT, thickness=8)
    d.text((90, 70), "THE AI ACT FIX KIT", font=mono(30, True), fill=MINT)

    hourglass(d, 1340, 190, 190)

    y = 200
    for line in title_lines:
        d.text((90, y), line, font=serif(74, True), fill=INK)
        y += 90

    d.text((90, y + 20), price, font=serif(46, True), fill=AMBER)

    d.rounded_rectangle([90, y + 100, 90 + 480, y + 100 + 140], radius=14, outline=CARD, width=2)
    touchpoint_row(d, 90 + 240, y + 170, icons, size=64, gap=30)
    d.text((90, y + 250), touchpoint_label, font=sans(26), fill=DIM)

    d.text((90, H - 90), tag_line, font=sans(30), fill=DIM)
    d.text((90, H - 50), "CLICK CODED  ·  AI-operated, human-reviewed  ·  EU AI Act Article 50", font=mono(22), fill=DIM)

    os.makedirs(OUT_DIR, exist_ok=True)
    img.save(out_path, quality=95)
    print(f"saved {out_path}")


def thumb(out_path, title_lines, price, icons):
    S = 1200
    img, d = new_canvas(S, S)
    top_bottom_bars(d, S, S, MINT, thickness=10)
    d.text((70, 70), "AI ACT FIX KIT", font=mono(28, True), fill=MINT)

    hourglass(d, 600, 380, 260)

    y = 660
    for line in title_lines:
        bb = d.textbbox((0, 0), line, font=serif(64, True))
        d.text(((S - (bb[2] - bb[0])) / 2, y), line, font=serif(64, True), fill=INK)
        y += 76

    bb = d.textbbox((0, 0), price, font=serif(56, True))
    d.text(((S - (bb[2] - bb[0])) / 2, y + 10), price, font=serif(56, True), fill=AMBER)

    touchpoint_row(d, 600, y + 140, icons, size=74, gap=40)

    d.text((70, S - 70), "CLICK CODED · AI-operated, human-reviewed", font=mono(22, True), fill=DIM)

    os.makedirs(OUT_DIR, exist_ok=True)
    img.save(out_path, quality=95)
    print(f"saved {out_path}")


if __name__ == "__main__":
    cover(os.path.join(OUT_DIR, "ai-act-fix-kit-cover.png"),
          ["Fix It"], "$39", "One touchpoint, unlocked. Ready to paste.",
          [chat_bubble_icon], "Covers the one touchpoint you diagnosed")

    cover(os.path.join(OUT_DIR, "ai-act-fix-kit-complete-cover.png"),
          ["Fix It All"], "$69", "Every touchpoint, unlocked. Ready to paste.",
          [chat_bubble_icon, image_icon, doc_icon], "Covers every touchpoint you might have")

    thumb(os.path.join(OUT_DIR, "ai-act-fix-kit-thumb.png"),
          ["Fix It"], "$39", [chat_bubble_icon])

    thumb(os.path.join(OUT_DIR, "ai-act-fix-kit-complete-thumb.png"),
          ["Fix It All"], "$69", [chat_bubble_icon, image_icon, doc_icon])
