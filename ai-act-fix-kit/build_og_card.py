#!/usr/bin/env python3
"""
og:image for The AI Act Fix Kit. Found missing in the 2026-07-28 audit
(ai-act-fix-kit-audit-report-2026-07-28.md, F5) -- every social share this page
was specifically built to earn was rendering with a broken image.

1200x630, the standard OG/Twitter card size (not the site's usual 1600x900 SKU
card -- this one needs to read correctly in a link-preview strip, not a full page).

Real drawn element per the iconographic canon: an hourglass, matching the live
page's own SVG icon exactly in shape, not a stock icon or text-on-block. Deadline
date is static text ("AUGUST 2, 2026"), not a live day-count -- a "3 days left"
image would be stale and wrong within a week of being generated.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "assets_lib"))
from aaa_render import new_canvas, top_bottom_bars, mono, serif, sans, MINT, AMBER, INK, DIM

W, H = 1200, 630
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "og-cards", "ai-act-fix-kit.png")


def hourglass(d, cx, cy, size, color=AMBER):
    """Same shape as the live page's inline SVG hourglass, redrawn at card scale."""
    half = size / 2
    bar_h = size * 0.06
    d.rounded_rectangle([cx - half, cy - half, cx + half, cy - half + bar_h], radius=3, fill=color)
    d.rounded_rectangle([cx - half, cy + half - bar_h, cx + half, cy + half], radius=3, fill=color)
    top_tri = [(cx - half * 0.75, cy - half + bar_h), (cx + half * 0.75, cy - half + bar_h), (cx, cy)]
    bot_tri = [(cx - half * 0.55, cy + half - bar_h), (cx + half * 0.55, cy + half - bar_h), (cx, cy + half * 0.15)]
    d.polygon(top_tri, outline=color, width=4)
    d.polygon(bot_tri, outline=color, width=4)
    # sand: mostly settled at the bottom, a little still in the top -- matches the
    # live page's mid-cycle animation frame rather than a static full/empty state
    sand_top = [(cx - half * 0.42, cy - half + bar_h + 10), (cx + half * 0.42, cy - half + bar_h + 10), (cx, cy - half * 0.15)]
    sand_bot = [(cx - half * 0.5, cy + half - bar_h - 6), (cx + half * 0.5, cy + half - bar_h - 6), (cx, cy + half * 0.35)]
    d.polygon(sand_top, fill=color)
    d.polygon(sand_bot, fill=color)


def build():
    """Copy per ai-act-fix-kit-funnel-2026-07-28.md Stage 0: the shareable hook
    is the irony, not the mechanics. First draft of this card led with 'The EU AI
    Act's disclosure rules go live' -- a spec sheet, not a hook, exactly the gap
    that funnel doc flagged and fixed on the page itself but this card shipped
    without. A stranger screenshots the irony line, not a deadline label."""
    img, d = new_canvas(W, H)
    top_bottom_bars(d, W, H, MINT, thickness=8)

    d.text((70, 56), "CLICK CODED · AI-OPERATED, HUMAN-REVIEWED", font=mono(24, True), fill=MINT)

    hourglass(d, 995, 130, 130)

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
    d.text((70, 452), "Free 1-minute check. Two of five answers are “you're fine.”", font=sans(32), fill=DIM)
    d.text((70, 494), "We had to answer this for ourselves first — so we're giving away the answer.", font=sans(26), fill=DIM)

    d.text((70, 556), "clickcoded.com/ai-visibility-check-free/ai-act-fix-kit", font=mono(22, True), fill=MINT)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, quality=95)
    print(f"saved {OUT}")


if __name__ == "__main__":
    build()
