#!/usr/bin/env python3
"""
Shared AAA visual-system rendering helpers for static PNG assets
(thumbnails, covers, promo images) across all Æ Studio product lanes.
Mirrors the site's design tokens: dark teal bg, mint/amber/coral accents,
serif display headlines (Georgia stand-in for Fraunces), mono kickers
(Courier stand-in for IBM Plex Mono), dot-grid texture.
"""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BG    = (6,  55,  64)
BG2   = (4,  38,  44)
CARD  = (10, 69,  82)
CARD2 = (8,  48,  58)
INK   = (244,238,225)
DIM   = (159,188,186)
MINT  = (46, 230,168)
AMBER = (245,185, 66)
CORAL = (232,106, 90)
GRID  = (60, 110, 105)


def serif(size, bold=True):
    p = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Georgia.ttf"
    return ImageFont.truetype(p, size)


def mono(size, bold=False):
    try:
        p = "/System/Library/Fonts/Supplemental/Courier New Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Courier New.ttf"
        return ImageFont.truetype(p, size)
    except Exception:
        return ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", size)


def sans(size, bold=False):
    idx = 1 if bold else 0
    return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size, index=idx)


def _radial_fade_mask(w, h, rx_frac=0.75, ry_frac=0.65, cx_frac=0.5, cy_frac=0.0, inner=0.40, outer=0.92, res=80):
    """Low-res radial gradient (opaque near top-center, fading to transparent),
    matching the site's `mask-image: radial-gradient(75% 65% at 50% 0%, #000 40%, transparent 92%)`.
    Built small then upscaled — avoids a slow per-pixel loop on the full image."""
    mask = Image.new("L", (res, res), 0)
    px = mask.load()
    cx, cy = res * cx_frac, res * cy_frac
    rx, ry = res * rx_frac, res * ry_frac
    for y in range(res):
        for x in range(res):
            d = math.sqrt(((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2)
            if d <= inner:
                v = 255
            elif d >= outer:
                v = 0
            else:
                v = int(255 * (1 - (d - inner) / (outer - inner)))
            px[x, y] = v
    return mask.resize((w, h), Image.BILINEAR)


def _glow(w, h, cx_frac, cy_frac, r_frac, color, alpha):
    """A soft blurred color blob, alpha-composited — matches the site's radial-gradient glows."""
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    cx, cy, r = w * cx_frac, h * cy_frac, max(w, h) * r_frac
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, alpha))
    return layer.filter(ImageFilter.GaussianBlur(radius=r * 0.5))


def new_canvas(w, h):
    """Full layered AAA background: vertical gradient + two soft glows + faded
    line-grid + faded dot-grid, matching the live site's body background exactly."""
    # 1. vertical gradient base (BG2 at top -> BG)
    img = Image.new("RGB", (w, h), BG)
    grad = Image.new("RGB", (1, h), BG)
    gpx = grad.load()
    fade_h = min(h, 340)
    for y in range(h):
        if y >= fade_h:
            gpx[0, y] = BG
        else:
            t = y / fade_h
            gpx[0, y] = tuple(int(BG2[i] + (BG[i] - BG2[i]) * t) for i in range(3))
    img = grad.resize((w, h))

    # 2. soft glows (mint upper-left, coral upper-right)
    base = img.convert("RGBA")
    base = Image.alpha_composite(base, _glow(w, h, 0.12, -0.08, 0.55, MINT, 26))
    base = Image.alpha_composite(base, _glow(w, h, 1.0, 0.10, 0.45, CORAL, 20))
    img = base.convert("RGB")

    fade_mask = _radial_fade_mask(w, h)

    # 3. line grid, faded
    grid_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grid_layer)
    spacing = 42
    line_color = (238, 246, 244, 36)
    for gx in range(0, w, spacing):
        gd.line([(gx, 0), (gx, h)], fill=line_color, width=1)
    for gy in range(0, h, spacing):
        gd.line([(0, gy), (w, gy)], fill=line_color, width=1)
    grid_layer.putalpha(Image.composite(grid_layer.split()[3], Image.new("L", (w, h), 0), fade_mask))
    img = Image.alpha_composite(img.convert("RGBA"), grid_layer).convert("RGB")

    # 4. dot grid, faded, mint-tinted
    dot_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    dd = ImageDraw.Draw(dot_layer)
    for gx in range(0, w, spacing):
        for gy in range(0, h, spacing):
            dd.ellipse([gx - 1.5, gy - 1.5, gx + 1.5, gy + 1.5], fill=(*MINT, 140))
    dot_layer.putalpha(Image.composite(dot_layer.split()[3], Image.new("L", (w, h), 0), fade_mask))
    img = Image.alpha_composite(img.convert("RGBA"), dot_layer).convert("RGB")

    d = ImageDraw.Draw(img)
    return img, d


def dot_grid(d, w, h, spacing=42):
    """Kept for compatibility with any direct callers; new_canvas() now bakes this in."""
    for gx in range(0, w, spacing):
        for gy in range(0, h, spacing):
            d.ellipse([gx - 1, gy - 1, gx + 1, gy + 1], fill=GRID)


def top_bottom_bars(d, w, h, color=MINT, thickness=8):
    d.rectangle([0, 0, w, thickness], fill=color)
    d.rectangle([0, h - thickness, w, h], fill=color)


def kicker(d, x, y, text, color=MINT, size=24):
    d.text((x, y), text, font=mono(size, bold=True), fill=color)


def headline(d, x, y, lines, size=64, line_gap=1.1, fill=INK):
    f = serif(size, bold=True)
    cy = y
    for line in lines:
        d.text((x, cy), line, font=f, fill=fill)
        bb = d.textbbox((0, 0), line, font=f)
        cy += int((bb[3] - bb[1]) * line_gap) + 14
    return cy


def price_pill(d, x, y, text, color=MINT):
    f = serif(30, bold=True)
    bb = d.textbbox((0, 0), text, font=f)
    pw, ph = bb[2] - bb[0] + 48, bb[3] - bb[1] + 32
    d.rounded_rectangle([x, y, x + pw, y + ph], radius=8, outline=color, width=3)
    d.text((x + 24, y + 16), text, font=f, fill=color)
    return pw, ph


def footer(d, x, y, text, color=DIM, size=20):
    d.text((x, y), text, font=sans(size), fill=color)


def sku_card(fname, kicker_text, title_lines, sub_lines, tag_line, w=2667, h=2000):
    """Full-bleed promo card: kicker, serif headline, sub bullets, price/tag pill, footer."""
    img, d = new_canvas(w, h)
    top_bottom_bars(d, w, h, MINT, thickness=14)
    d.text((150, 170), kicker_text, font=mono(40, True), fill=MINT)
    y = 290
    for line in title_lines:
        d.text((150, y), line, font=serif(120, True), fill=INK)
        y += 140
    y += 20
    for line in sub_lines:
        d.text((150, y), line, font=sans(56), fill=DIM)
        y += 76
    d.rounded_rectangle([150, 1620, 1250, 1740], radius=16, outline=MINT, width=5)
    d.text((190, 1650), tag_line, font=serif(44, True), fill=MINT)
    d.text((150, 1850), "Æ STUDIO  ·  AI-operated, human-reviewed  ·  honest scope, no invented facts", font=sans(38), fill=DIM)
    img.save(fname, quality=95)
    print(f"saved {fname}")


def playbook_cover(out_path, kicker_text, headline_lines, price, body_lines, stat_kicker, rows, stamp_top, stamp_bottom, stamp_color=None, unit="/100"):
    """Cover image: kicker, serif headline, price pill, body copy, stat/rank bars, audited stamp, footer."""
    color = stamp_color or MINT
    W, H = 1600, 900
    img, d = new_canvas(W, H)
    top_bottom_bars(d, W, H, MINT)

    kicker(d, 90, 100, kicker_text)
    y = headline(d, 90, 150, headline_lines, size=54)
    pw, ph = price_pill(d, 90, y + 24, price)
    body_y = y + 24 + ph + 30
    for line in body_lines:
        d.text((90, body_y), line, font=sans(22), fill=DIM)
        body_y += 34

    audited_stamp(d, W - 130, 150, 100, stamp_top, stamp_bottom, color)

    stat_y = body_y + 40
    d.text((90, stat_y), stat_kicker, font=mono(16, bold=True), fill=DIM)
    row_y = stat_y + 40
    bar_x, bar_w, bar_h = 90, 430, 22
    for row in rows:
        label, score, row_color = row[0], row[1], row[2]
        row_unit = row[3] if len(row) > 3 else unit
        d.text((bar_x, row_y), label, font=sans(19, bold=True), fill=INK)
        score_text = f"{score}{row_unit}"
        bb = d.textbbox((0, 0), score_text, font=sans(19, bold=True))
        d.text((bar_x + bar_w - (bb[2]-bb[0]), row_y), score_text, font=sans(19, bold=True), fill=row_color)
        row_y += 28
        d.rounded_rectangle([bar_x, row_y, bar_x + bar_w, row_y + bar_h], radius=4, fill=CARD2)
        d.rounded_rectangle([bar_x, row_y, bar_x + int(bar_w * min(score, 100) / 100), row_y + bar_h], radius=4, fill=row_color)
        row_y += bar_h + 18

    footer(d, 90, H - 46, "Æ STUDIO  ·  AI-operated, human-reviewed  ·  no invented facts, no guaranteed citations")
    img.save(out_path, quality=95)
    print(f"saved {out_path}")


def playbook_thumb(out_path, headline_lines, price, kicker_text="THE PLAYBOOK"):
    W = H = 1200
    img, d = new_canvas(W, H)
    top_bottom_bars(d, W, H, MINT)
    kicker(d, 70, 80, kicker_text, size=22)
    headline(d, 70, 130, headline_lines, size=64)
    price_pill(d, 70, 500, price)
    footer(d, 70, H - 70, "Æ STUDIO", size=22)
    img.save(out_path, quality=95)
    print(f"saved {out_path}")


def audited_stamp(d, cx, cy, r, top_text, bottom_text, color=MINT):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=3)
    d.ellipse([cx - r + 8, cy - r + 8, cx + r - 8, cy + r - 8], outline=color, width=1)
    f_top = mono(16)
    f_bottom = serif(24, bold=True)
    bb1 = d.textbbox((0, 0), top_text, font=f_top)
    d.text((cx - (bb1[2]-bb1[0])//2, cy - 34), top_text, font=f_top, fill=color)
    bb2 = d.textbbox((0, 0), bottom_text, font=f_bottom)
    d.text((cx - (bb2[2]-bb2[0])//2, cy - 6), bottom_text, font=f_bottom, fill=color)
