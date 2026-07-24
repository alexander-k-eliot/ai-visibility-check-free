#!/usr/bin/env python3
"""
Rebuild the org chart image with the full AAA visual system:
Fraunces-style serif headlines (Georgia fallback), IBM Plex Mono-style
kickers/labels (Menlo fallback), dot-grid texture, same content/layout
as the original chart.
"""
import os
from PIL import Image, ImageDraw, ImageFont

BG    = (6,  55,  64)
CARD  = (10, 69,  82)
INK   = (244,238,225)
DIM   = (159,188,186)
MINT  = (46, 230,168)
AMBER = (245,185, 66)
CORAL = (232,106, 90)
GRID  = (60, 110, 105)

OUT = os.path.dirname(os.path.abspath(__file__))
W, H = 1800, 1400

def serif(size, bold=True):
    p = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Georgia.ttf"
    return ImageFont.truetype(p, size)

def mono(size, bold=False):
    try:
        return ImageFont.truetype("/System/Library/Fonts/Supplemental/Courier New Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Courier New.ttf", size)
    except Exception:
        return ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", size)

def sans(size, bold=False):
    idx = 1 if bold else 0
    return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size, index=idx)

def centered(d, cx, y, text, f, fill):
    bb = d.textbbox((0, 0), text, font=f)
    w = bb[2] - bb[0]
    d.text((cx - w // 2, y), text, font=f, fill=fill)
    return bb[3] - bb[1]

def card(d, x, y, w, h, border_color, radius=10):
    d.rounded_rectangle([x, y, x + w, y + h], radius=radius, outline=border_color, width=2, fill=CARD)

def dot_grid(d):
    for gx in range(0, W, 42):
        for gy in range(0, H, 42):
            d.ellipse([gx - 1, gy - 1, gx + 1, gy + 1], fill=GRID)

def build():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    dot_grid(d)

    d.rectangle([0, 0, W, 6], fill=MINT)

    # Title
    centered(d, W // 2, 40, "Æ STUDIO", serif(58, bold=True), MINT)
    centered(d, W // 2, 118, "the org chart — every agent that runs this operation, real and current", sans(22), DIM)

    # Chief operator card
    cx, cy, cw, ch = W // 2 - 220, 190, 440, 140
    card(d, cx, cy, cw, ch, AMBER)
    d.ellipse([cx + 24, cy + 34, cx + 96, cy + 106], outline=AMBER, width=3)
    d.line([(cx + 60, cy + 40), (cx + 60, cy + 100)], fill=AMBER, width=2)
    d.line([(cx + 30, cy + 70), (cx + 90, cy + 70)], fill=AMBER, width=2)
    d.text((cx + 130, cy + 20), "ALEXANDER", font=serif(30, bold=True), fill=INK)
    d.text((cx + 130, cy + 62), "“Alex” · Chief operator — runs the whole site", font=mono(15), fill=AMBER)
    d.text((cx + 130, cy + 92), "Charters lanes, reallocates cadence, cross-lane calls", font=sans(16), fill=DIM)

    # connector
    d.line([(W // 2, cy + ch), (W // 2, cy + ch + 40)], fill=GRID, width=2)
    d.line([(cx + 60, cy + ch + 40), (W - cx - 60, cy + ch + 40)], fill=GRID, width=2)

    # Three fleet-wide function cards
    fn_y = cy + ch + 40
    fn_w, fn_h, gap = 400, 150, 60
    fn_x0 = (W - (fn_w * 3 + gap * 2)) // 2
    functions = [
        (MINT,  "HERALD",  "Demand generation",      "PR · growth · every channel"),
        (AMBER, "FACTOR",  "Conversion & pricing",   "why didn't they buy, and fix it"),
        (CORAL, "GUIDE",   "Business North Star",    "StoryBrand + business success, binding"),
    ]
    for i, (color, name, sub, detail) in enumerate(functions):
        fx = fn_x0 + i * (fn_w + gap)
        d.line([(fx + fn_w // 2, fn_y), (fx + fn_w // 2, fn_y + 20)], fill=GRID, width=2)
        card(d, fx, fn_y + 20, fn_w, fn_h, color)
        d.text((fx + 24, fn_y + 42), name, font=serif(28, bold=True), fill=INK)
        d.text((fx + 24, fn_y + 82), sub, font=mono(15), fill=color)
        d.text((fx + 24, fn_y + 108), detail, font=sans(15), fill=DIM)

    # Lanes header
    lanes_y = fn_y + 20 + fn_h + 50
    centered(d, W // 2, lanes_y, "14 NUMBERED LANES — EACH ITS OWN PRODUCT, ITS OWN P&L", mono(18, bold=True), INK)
    d.line([(60, lanes_y + 40), (W - 60, lanes_y + 40)], fill=GRID, width=1)

    lanes = [
        ("0", "SHOPKEEPER", "Digital products"),
        ("1", "SURVEYOR", "AgentReady audits"),
        ("2", "VENDOR", "Machine customers"),
        ("3", "REGISTRAR", "Trust registry"),
        ("4", "STEWARD", "Asset stewardship"),
        ("5", "BROKER", "Build-to-sell exits"),
        ("6", "MERCHANT", "Etsy products"),
        ("7", "CANVASSER", "Local AI audits"),
        ("8", "SENTINEL", "Pulse monitoring"),
        ("9", "MASON", "WordPress plugin"),
        ("10", "BOTSMITH", "Poe bot portfolio"),
        ("11", "BINDER", "KDP workbooks"),
        ("12", "WRIGHT", "AI adoption"),
        ("13", "USHER", "Accessibility audits"),
    ]
    cols = 7
    grid_x0, grid_y0 = 60, lanes_y + 70
    cell_w = (W - 120) // cols
    cell_h = 210
    row_gap = 20

    for i, (num, name, sub) in enumerate(lanes):
        col = i % cols
        row = i // cols
        lx = grid_x0 + col * cell_w
        ly = grid_y0 + row * (cell_h + row_gap)
        card(d, lx, ly, cell_w - 20, cell_h, GRID)
        circ_cx, circ_cy, circ_r = lx + (cell_w - 20) // 2, ly + 50, 26
        d.ellipse([circ_cx - circ_r, circ_cy - circ_r, circ_cx + circ_r, circ_cy + circ_r], outline=MINT, width=2)
        centered(d, circ_cx, circ_cy - 16, num, mono(22, bold=True), MINT)
        centered(d, lx + (cell_w - 20) // 2, ly + 96, name, serif(19, bold=True), INK)
        centered(d, lx + (cell_w - 20) // 2, ly + 130, sub, sans(14), DIM)
        centered(d, lx + (cell_w - 20) // 2, ly + 160, "own lane · own P&L", mono(12), DIM)

    footer_y = grid_y0 + 2 * (cell_h + row_gap) + 20
    d.line([(60, footer_y), (W - 60, footer_y)], fill=GRID, width=1)
    centered(d, W // 2, footer_y + 24, "1 CHIEF OPERATOR · 3 FLEET-WIDE FUNCTIONS · 14 LANE BUSINESSES · $0 REVENUE, STILL BUILDING", mono(18, bold=True), MINT)
    centered(d, W // 2, footer_y + 58, "AI-operated, human-reviewed. Every box on this chart has a real charter file. Nothing here is invented.", sans(16), DIM)
    centered(d, W // 2, footer_y + 88, "alexander-k-eliot.github.io · Never Not Working", mono(15), AMBER)

    d.rectangle([0, H - 6, W, H], fill=MINT)

    out = f"{OUT}/org-chart.png"
    img.save(out, quality=95)
    print(f"saved {out}")

if __name__ == "__main__":
    build()
