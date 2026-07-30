#!/usr/bin/env python3
"""
og:image for The AI Act Fix Kit. Found missing in the 2026-07-28 audit
(ai-act-fix-kit-audit-report-2026-07-28.md, F5) -- every social share this page
was specifically built to earn was rendering with a broken image.

1200x630, the standard OG/Twitter card size (not the site's usual 1600x900 SKU
card -- this one needs to read correctly in a link-preview strip, not a full page).

v2, 2026-07-29 pre-promotion audit (B3): the hourglass hero was replaced. Brandon
rejected the hourglass for the Gumroad listing art ("looks bad... doesn't
communicate much of anything"), and the listings were redesigned around a
crossed-out-80-page-stack -> real-answer-card visual metaphor -- but this og-card
was approved before that pivot (for its copy, not its art) and never re-reviewed
after. Every social share was leading with the exact visual language Brandon
killed, one click removed from Gumroad art that no longer matched. Reuses the
same iconography from build_gumroad_covers.py, scaled down to an icon-only badge
(no internal text -- illegible at social-preview thumbnail scale anyway; the
silhouette carries the "villain vs. resolution" story on its own).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "assets_lib"))
from aaa_render import new_canvas, top_bottom_bars, mono, serif, sans, MINT, AMBER, INK, DIM, CARD, CARD2, CORAL

W, H = 1200, 630
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "og-cards", "ai-act-fix-kit.png")


def paper_stack(d, cx, cy, w, h, color=DIM, pages=3):
    step = w * 0.1
    for i in range(pages - 1, -1, -1):
        ox, oy = -step * i * 0.6, -step * i * 0.9
        x0, y0 = cx - w / 2 + ox, cy - h / 2 + oy
        x1, y1 = x0 + w, y0 + h
        d.rounded_rectangle([x0, y0, x1, y1], radius=5, fill=CARD2 if i else CARD, outline=color, width=2)
        if i == 0:
            ly = y0 + h * 0.18
            while ly < y1 - h * 0.12:
                d.rectangle([x0 + w * 0.12, ly, x0 + w * 0.78, ly + h * 0.045], fill=color)
                ly += h * 0.14


def no_slash(d, cx, cy, r, color=CORAL, width=8):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=width)
    off = r * 0.68
    d.line([cx - off, cy - off, cx + off, cy + off], fill=color, width=width)


def check_badge(d, cx, cy, r, color=MINT):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    d.line([cx - r * 0.45, cy, cx - r * 0.1, cy + r * 0.4], fill=CARD, width=max(3, int(r * 0.22)))
    d.line([cx - r * 0.1, cy + r * 0.4, cx + r * 0.5, cy - r * 0.35], fill=CARD, width=max(3, int(r * 0.22)))


def answer_card(d, cx, cy, w, h, color=MINT):
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=8, fill=CARD, outline=color, width=3)
    ly = cy - h * 0.15
    for frac in (0.7, 0.5):
        d.rectangle([cx - w * 0.38, ly, cx - w * 0.38 + w * 0.76 * frac, ly + h * 0.09], fill=color)
        ly += h * 0.24
    check_badge(d, cx + w / 2 - 16, cy + h / 2 - 16, 13, color)


def arrow(d, x1, x2, y, color=MINT, width=5, head=12):
    d.line([x1, y, x2 - head, y], fill=color, width=width)
    d.polygon([(x2, y), (x2 - head, y - head), (x2 - head, y + head)], fill=color)


def build():
    """Copy per ai-act-fix-kit-funnel-2026-07-28.md Stage 0: the shareable hook
    is the irony, not the mechanics. First draft of this card led with 'The EU AI
    Act's disclosure rules go live' -- a spec sheet, not a hook, exactly the gap
    that funnel doc flagged and fixed on the page itself but this card shipped
    without. A stranger screenshots the irony line, not a deadline label."""
    img, d = new_canvas(W, H)
    top_bottom_bars(d, W, H, MINT, thickness=8)

    d.text((70, 56), "CLICK CODED · AI-OPERATED, HUMAN-REVIEWED", font=mono(24, True), fill=MINT)

    # Compact icon-only version of the listing art's hero metaphor: crossed-out
    # stack (the 80-page kit) -> arrow -> a real answer, checked. Kept well
    # inside the 1200px canvas -- the first version clipped the card off the
    # right edge, caught by re-reading the actual rendered PNG, not the code.
    paper_stack(d, 895, 130, 115, 140)
    no_slash(d, 895, 130, 85)
    arrow(d, 995, 1060, 130)
    answer_card(d, 1110, 130, 80, 135)

    # The hook, as headline -- StoryBrand villain (the law) named through irony,
    # not description; the same line this session identified as the strongest
    # press headline, now leading the card that's supposed to earn press.
    y = 130
    for line in ["An AI built the fix", "for a law about", "disclosing AI."]:
        d.text((70, y), line, font=serif(62, True), fill=INK)
        y += 74

    d.text((70, y + 14), "EU AI ACT ARTICLE 50 · ENFORCEABLE AUG 2, 2026", font=mono(24, True), fill=AMBER)

    # The Plan, stated as the honesty differentiator (journalist "genuinely
    # surprising" attribute: a tool that tells most visitors not to buy anything)
    d.text((70, 452), "Free 1-minute check. Six of ten answers end with nothing to buy.", font=sans(32), fill=DIM)
    d.text((70, 494), "We had to answer this for ourselves first — so we're giving away the answer.", font=sans(26), fill=DIM)

    d.text((70, 556), "clickcoded.com/ai-visibility-check-free/ai-act-fix-kit", font=mono(22, True), fill=MINT)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, quality=95)
    print(f"saved {OUT}")


if __name__ == "__main__":
    build()
