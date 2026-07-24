#!/usr/bin/env python3
"""
Build Product Hunt gallery images + thumbnail for the AI Visibility Checker.
Visual system: matches alexander-k-eliot.github.io exactly.
Score: 62/100 (below industry avg of 67 — urgency framing, near-miss psychology).
"""
import os, math
from PIL import Image, ImageDraw, ImageFont

# ── Brand colors (exact site values) ────────────────────────────────────────
BG    = (6,  55,  64)   # #063740
CARD  = (10, 69,  82)   # #0a4552
CARD2 = (8,  48,  58)   # slightly darker card
INK   = (238,246,244)   # #eef6f4
DIM   = (159,188,186)   # #9fbcba
MINT  = (46, 230,168)   # #2ee6a8
AMBER = (245,185, 66)   # #f5b942
CORAL = (232,106, 90)   # #e86a5a

SCORE = 62  # Optimal: below industry avg (67), near-miss motivator

OUT = os.path.dirname(os.path.abspath(__file__))

# ── Fonts ────────────────────────────────────────────────────────────────────
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
        except:
            continue
    return ImageFont.load_default()

def centered_text(d, cx, y, text, f, fill):
    bb = d.textbbox((0,0), text, font=f)
    w = bb[2] - bb[0]
    d.text((cx - w//2, y), text, font=f, fill=fill)

def score_arc(d, cx, cy, r, score, stroke=20):
    """Draw score ring: dark bg track + mint arc from 12 o'clock clockwise."""
    box = [cx-r, cy-r, cx+r, cy+r]
    # Track (dark)
    d.arc(box, start=0, end=360, fill=CARD2, width=stroke)
    # Score arc
    end_deg = 270 + (score / 100) * 360
    d.arc(box, start=270, end=end_deg, fill=MINT, width=stroke)

def dot_check(d, x, y, passed, r=10):
    color = MINT if passed else CORAL
    d.ellipse([x-r, y-r, x+r, y+r], outline=color, width=3)
    inner = r - 4
    d.ellipse([x-inner, y-inner, x+inner, y+inner], fill=color)


# ── Gallery 1: Score card view ───────────────────────────────────────────────
def build_gallery_1():
    W, H = 1270, 760
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Accent bar top
    d.rectangle([0, 0, W, 7], fill=MINT)

    # Kicker
    d.text((60, 36), "Æ STUDIO  ·  FREE AI VISIBILITY CHECKER", font=font(20), fill=MINT)

    # Headline
    d.text((60, 76), "Will AI assistants find your website?", font=font(50, bold=True), fill=INK)

    # Sub
    d.text((60, 148), "Paste a URL. Instant results. No signup.", font=font(23), fill=DIM)

    # ── Score ring ──
    cx, cy, r = 220, 430, 110
    score_arc(d, cx, cy, r, SCORE, stroke=22)

    # Score number (inside ring)
    f_num = font(78, bold=True)
    num_str = str(SCORE)
    bb = d.textbbox((0,0), num_str, font=f_num)
    nw, nh = bb[2]-bb[0], bb[3]-bb[1]
    d.text((cx - nw//2, cy - nh//2 - 10), num_str, font=f_num, fill=INK)

    # "/100" — just below score number, still inside ring
    f_denom = font(20)
    denom = "/100"
    bb2 = d.textbbox((0,0), denom, font=f_denom)
    dw = bb2[2]-bb2[0]
    d.text((cx - dw//2, cy + nh//2 - 6), denom, font=f_denom, fill=DIM)

    # "AI visibility score" — BELOW ring (no overlap)
    f_label = font(19)
    label = "AI visibility score"
    bb3 = d.textbbox((0,0), label, font=f_label)
    lw = bb3[2]-bb3[0]
    d.text((cx - lw//2, cy + r + 18), label, font=f_label, fill=DIM)

    # Divider
    div_x = cx + r + 40
    d.line([(div_x, cy - r - 10), (div_x, cy + r + 50)], fill=CARD2, width=2)

    # ── Checklist ──
    checks = [
        (True,  "Crawler access (robots.txt)"),
        (True,  "JSON-LD structured data"),
        (False, "llms.txt present"),
        (True,  "Answer-first paragraph structure"),
        (True,  "H1 present and descriptive"),
        (False, "FAQ / entity schema"),
        (True,  "No-JS content legibility"),
        (True,  "Sitemap present"),
        (True,  "Title + meta description"),
    ]
    f_item = font(22)
    x0 = div_x + 40
    y0 = cy - r + 8
    row_h = 52

    for i, (passed, text) in enumerate(checks):
        y = y0 + i * row_h
        dot_check(d, x0, y + 10, passed, r=9)
        d.text((x0 + 24, y - 1), text, font=f_item, fill=INK)

    # Industry benchmark bar at bottom
    bench = f"Industry average: 67/100  ·  Your score: {SCORE}/100  ·  2 quick fixes could push you to 78"
    d.text((60, H - 56), bench, font=font(17), fill=DIM)

    # MACHINE VERIFIED stamp (top right)
    stamp_cx, stamp_cy = W - 110, 100
    stamp_r = 70
    d.ellipse([stamp_cx-stamp_r, stamp_cy-stamp_r, stamp_cx+stamp_r, stamp_cy+stamp_r],
              outline=MINT, width=3)
    d.ellipse([stamp_cx-stamp_r+8, stamp_cy-stamp_r+8, stamp_cx+stamp_r-8, stamp_cy+stamp_r-8],
              outline=MINT, width=1)
    centered_text(d, stamp_cx, stamp_cy - 28, "MACHINE", font(14), MINT)
    centered_text(d, stamp_cx, stamp_cy - 10, "VERIFIED", font(20, bold=True), MINT)
    # Tick marks around stamp
    for deg in range(0, 360, 30):
        rad = math.radians(deg)
        x1 = stamp_cx + (stamp_r - 4) * math.cos(rad)
        y1 = stamp_cy + (stamp_r - 4) * math.sin(rad)
        x2 = stamp_cx + (stamp_r + 4) * math.cos(rad)
        y2 = stamp_cy + (stamp_r + 4) * math.sin(rad)
        d.line([(x1,y1),(x2,y2)], fill=MINT, width=2)

    # Bottom bar
    d.rectangle([0, H-7, W, H], fill=MINT)

    out = f"{OUT}/gallery-1-score.png"
    img.save(out, quality=95)
    print(f"✓ {out}")
    return out


# ── Gallery 2: Fix list ──────────────────────────────────────────────────────
def build_gallery_2():
    W, H = 1270, 760
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, W, 7], fill=CORAL)
    d.text((60, 36), "Æ STUDIO  ·  YOUR FIX LIST", font=font(20), fill=CORAL)
    d.text((60, 76), "Two missing signals. Here's exactly what to add.", font=font(46, bold=True), fill=INK)
    d.text((60, 142), f"Your score: {SCORE}/100  ·  Industry average: 67/100  ·  Estimated after fix: 78/100", font=font(21), fill=DIM)

    fixes = [
        ("llms.txt missing", "+8 pts",
         "A plain-text file at /llms.txt tells AI crawlers which pages to read.",
         "Create /llms.txt listing your key pages. Takes 10 minutes."),
        ("FAQ / entity schema missing", "+8 pts",
         "Structured FAQ data lets AI assistants extract Q&A directly from your page.",
         "Add FAQ schema (JSON-LD) to your homepage. Use our free generator."),
    ]

    f_title = font(28, bold=True)
    f_pts   = font(26, bold=True)
    f_body  = font(21)
    f_fix   = font(20)

    y = 210
    for title, pts, why, how in fixes:
        # Card background
        d.rounded_rectangle([60, y, W-60, y+175], radius=10, fill=CARD)
        d.rounded_rectangle([60, y, 68, y+175], radius=4, fill=CORAL)

        # Title + points
        d.text((88, y + 18), title, font=f_title, fill=CORAL)
        pts_bb = d.textbbox((0,0), pts, font=f_pts)
        d.text((W - 80 - (pts_bb[2]-pts_bb[0]), y + 20), pts, font=f_pts, fill=MINT)

        # Why / How
        d.text((88, y + 62),  f"Why it matters: {why}", font=f_body, fill=INK)
        d.text((88, y + 102), f"How to fix:     {how}", font=f_fix, fill=DIM)

        # CTA pill
        pill_label = "Free llms.txt generator →" if "llms" in title else "Free FAQ schema generator →"
        d.rounded_rectangle([88, y + 136, 88 + 340, y + 164], radius=6, fill=CARD2)
        d.text((96, y + 139), pill_label, font=font(17), fill=MINT)

        y += 200

    d.text((60, H - 56), "Both fixes are free. Use the tools at aestudio.pro", font=font(18), fill=DIM)
    d.rectangle([0, H-7, W, H], fill=CORAL)

    out = f"{OUT}/gallery-2-fixlist.png"
    img.save(out, quality=95)
    print(f"✓ {out}")
    return out


# ── Gallery 3: Tool grid ─────────────────────────────────────────────────────
def build_gallery_3():
    W, H = 1270, 760
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, W, 7], fill=MINT)
    d.text((60, 36), "Æ STUDIO  ·  30+ FREE TOOLS", font=font(20), fill=MINT)
    d.text((60, 76), "Everything you need to fix your score.", font=font(46, bold=True), fill=INK)
    d.text((60, 140), "Free AI Visibility Check is part of a complete toolkit. All tools free, no signup.", font=font(21), fill=DIM)

    tools = [
        (MINT,  "AI Visibility\nChecker",       "Score your site"),
        (MINT,  "llms.txt\nGenerator",           "AI crawler file"),
        (MINT,  "FAQ Schema\nGenerator",         "Entity markup"),
        (MINT,  "Robots.txt\nChecker",           "Crawl policy"),
        (AMBER, "Schema\nValidator",             "Structured data"),
        (AMBER, "Answer-First\nScanner",         "Content structure"),
        (AMBER, "Writing Tells\nScanner",        "AI slop detector"),
        (CORAL, "Accessibility\nBenchmark",      "WCAG audit"),
        (CORAL, "Industry\nBenchmarks",          "10 industries"),
        (CORAL, "Compare\nSites",               "Side-by-side"),
        (DIM,   "Sitemap\nAnalyzer",             "Coverage check"),
        (DIM,   "GEO Content\nPlaybook →",       "$29 upgrade"),
    ]

    cols, rows = 4, 3
    cell_w = (W - 120) // cols
    cell_h = 150
    x0, y0 = 60, 195

    f_tool = font(21, bold=True)
    f_sub  = font(17)

    for i, (color, name, sub) in enumerate(tools):
        col = i % cols
        row = i // cols
        cx = x0 + col * cell_w
        cy = y0 + row * cell_h

        d.rounded_rectangle([cx, cy, cx+cell_w-12, cy+cell_h-12], radius=8, fill=CARD)
        d.rounded_rectangle([cx, cy, cx+5, cy+cell_h-12], radius=3, fill=color)

        # Name (handle newline)
        lines = name.split("\n")
        d.text((cx+20, cy+16), lines[0], font=f_tool, fill=INK)
        if len(lines) > 1:
            d.text((cx+20, cy+42), lines[1], font=f_tool, fill=INK)
        d.text((cx+20, cy+78), sub, font=f_sub, fill=DIM)

    d.text((60, H-56), "aestudio.pro  ·  Never Not Working", font=font(18), fill=DIM)
    d.rectangle([0, H-7, W, H], fill=MINT)

    out = f"{OUT}/gallery-3-toolgrid.png"
    img.save(out, quality=95)
    print(f"✓ {out}")
    return out


# ── Thumbnail: 240×240 square ────────────────────────────────────────────────
def build_thumbnail():
    W = H = 480  # Generate 2x, resize to 240
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, W, 7], fill=MINT)

    # Score ring, centered
    cx, cy, r = W//2, H//2 + 10, 140
    score_arc(d, cx, cy, r, SCORE, stroke=26)

    # Score number
    f_num = font(100, bold=True)
    num_str = str(SCORE)
    bb = d.textbbox((0,0), num_str, font=f_num)
    nw, nh = bb[2]-bb[0], bb[3]-bb[1]
    d.text((cx - nw//2, cy - nh//2 - 12), num_str, font=f_num, fill=INK)

    # /100
    f_d = font(26)
    denom = "/100"
    bb2 = d.textbbox((0,0), denom, font=f_d)
    dw = bb2[2]-bb2[0]
    d.text((cx - dw//2, cy + nh//2 - 8), denom, font=f_d, fill=DIM)

    # Label BELOW ring
    f_lbl = font(24)
    lbl = "AI visibility score"
    bb3 = d.textbbox((0,0), lbl, font=f_lbl)
    lw = bb3[2]-bb3[0]
    d.text((cx - lw//2, cy + r + 16), lbl, font=f_lbl, fill=DIM)

    # Kicker at top
    kicker = "Æ STUDIO"
    bb4 = d.textbbox((0,0), kicker, font=font(22))
    kw = bb4[2]-bb4[0]
    d.text((cx - kw//2, 28), kicker, font=font(22), fill=MINT)

    d.rectangle([0, H-7, W, H], fill=MINT)

    # Resize to 240×240
    thumb = img.resize((240, 240), Image.LANCZOS)
    out = f"{OUT}/ph-thumbnail.png"
    thumb.save(out)
    print(f"✓ {out}")
    return out


if __name__ == "__main__":
    build_gallery_1()
    build_gallery_2()
    build_gallery_3()
    build_thumbnail()
    print("\nAll 4 images built. Upload to PH gallery + thumbnail.")
