#!/usr/bin/env python3
"""
Real Gumroad cover + thumbnail images for both AI Act Fix Kit listings.

v2, 2026-07-28: replaced the hourglass hero (looked bad, communicated
nothing about the product) after Brandon's direct correction -- the
countdown/timer motif belongs on the site's own tool as a deadline
reminder, not as the lead visual selling the product. Covers instead
have to carry the Think-Like-A-Journalist + StoryBrand story visually,
not just in copy.

The actual story, drawn: the villain is the 80-page compliance kit
(shown as a crossed-out stack of dense pages) -> the transformation is
the arrow -> the resolution is the concrete, real answer-card with the
actual disclosure sentence on it, checked and ready to paste. This is
the same "David-vs-Goliath / format contrast" angle already validated
as the strongest press headline for this product (see
brandscript-ai-act-fix-kit-2026-07-28.md), made visual instead of only
textual.

Honest tier differentiator, drawn not stated: Fix It shows ONE answer
card (the one touchpoint it unlocks). Fix It All shows THREE cascaded
answer cards (every touchpoint) -- the same real difference as before,
now integrated into the hero itself instead of a separate icon row.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "assets_lib"))
from aaa_render import new_canvas, top_bottom_bars, mono, serif, sans, MINT, AMBER, INK, DIM, CARD, CARD2, CORAL

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "listing-art")


def paper_stack(d, cx, cy, w, h, color=DIM, pages=4):
    """A messy stack of dense document pages -- the villain (the 80-page kit)."""
    step = w * 0.09
    for i in range(pages - 1, -1, -1):
        ox, oy = -step * i * 0.6, -step * i * 0.9
        x0, y0 = cx - w / 2 + ox, cy - h / 2 + oy
        x1, y1 = x0 + w, y0 + h
        shade = tuple(int(c + (CARD2[j] - c) * (i / pages) * 0.5) for j, c in enumerate(color))
        d.rounded_rectangle([x0, y0, x1, y1], radius=6, fill=CARD2 if i else CARD, outline=shade, width=2)
        if i == 0:
            # dense text lines on the front page -- "wall of text" texture
            ly = y0 + h * 0.16
            while ly < y1 - h * 0.1:
                lw = w * (0.55 + 0.35 * ((ly * 7) % 3) / 3)
                d.rectangle([x0 + w * 0.12, ly, x0 + w * 0.12 + lw, ly + h * 0.035], fill=shade)
                ly += h * 0.11


def no_slash(d, cx, cy, r, color=CORAL, width=10):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=width)
    off = r * 0.68
    d.line([cx - off, cy - off, cx + off, cy + off], fill=color, width=width)


def arrow(d, x1, x2, y, color=MINT, width=7, head=16):
    d.line([x1, y, x2 - head, y], fill=color, width=width)
    d.polygon([(x2, y), (x2 - head, y - head), (x2 - head, y + head)], fill=color)


def check_badge(d, cx, cy, r, color=MINT):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    d.line([cx - r * 0.45, cy, cx - r * 0.1, cy + r * 0.4], fill=CARD, width=max(3, int(r * 0.22)))
    d.line([cx - r * 0.1, cy + r * 0.4, cx + r * 0.5, cy - r * 0.35], fill=CARD, width=max(3, int(r * 0.22)))


def answer_card(d, x, y, w, h, quote_lines, label="YOUR DISCLOSURE TEXT", color=MINT, filled=True):
    """The resolution: a real card showing the actual (generic) disclosure sentence, checked."""
    if filled:
        d.rounded_rectangle([x, y, x + w, y + h], radius=12, fill=CARD, outline=color, width=3)
    else:
        d.rounded_rectangle([x, y, x + w, y + h], radius=12, outline=DIM, width=2)
        return
    d.text((x + 22, y + 16), label, font=mono(15, True), fill=color)
    ly = y + 46
    for line in quote_lines:
        d.text((x + 22, ly), line, font=serif(23, False), fill=INK)
        ly += 30
    check_badge(d, x + w - 26, y + h - 26, 15, color)


def hero(d, cx_stack, cx_card, cy, card_w, card_h, quote_lines, tiers=1):
    stack_w, stack_h = 220, 265
    paper_stack(d, cx_stack, cy, stack_w, stack_h)
    no_slash(d, cx_stack, cy, stack_h * 0.62)
    arrow_x1 = cx_stack + stack_w * 0.62 + 40
    card_x = cx_card - card_w // 2
    arrow_x2 = card_x - 14
    arrow(d, arrow_x1, arrow_x2, cy)

    card_y = cy - card_h // 2
    if tiers >= 3:
        answer_card(d, card_x + 30, card_y - 22, card_w, card_h, [], filled=False)
        answer_card(d, card_x + 15, card_y - 11, card_w, card_h, [], filled=False)
    answer_card(d, card_x, card_y, card_w, card_h, quote_lines)


def cover(out_path, headline_lines, tier_price, tag_line, quote_lines, tiers, sub_label):
    """v3, 2026-07-29: copy-only revision (Brandon's direct correction -- the prior
    "Fix It / $39" headline didn't say what the product IS, only its brand name and
    price; a stranger scrolling Gumroad had to already understand the product to
    parse it). Headline now states the product itself (StoryBrand Plan-as-product),
    kicker leads with the deadline fact (Think-Like-A-Journalist who/what/when), tier
    name demoted to a small chip next to price. Visual treatment (hero icon, layout,
    palette) deliberately unchanged -- Brandon confirmed that part is working."""
    W, H = 1600, 900
    img, d = new_canvas(W, H)
    top_bottom_bars(d, W, H, MINT, thickness=8)
    d.text((90, 60), "EU AI ACT ARTICLE 50  ·  ENFORCEABLE AUG 2, 2026", font=mono(24, True), fill=MINT)

    hero(d, 290, 1080, 330, 720, 220, quote_lines, tiers)
    d.text((160, 502), "the 80-page kit", font=sans(21), fill=DIM)

    hy = 590
    for line in headline_lines:
        d.text((90, hy), line, font=serif(52, True), fill=INK)
        hy += 62
    hy += 14
    d.text((90, hy), tier_price, font=mono(24, True), fill=AMBER)
    d.text((90, hy + 40), sub_label, font=sans(24), fill=DIM)

    d.text((90, H - 92), tag_line, font=sans(27), fill=INK)
    d.text((90, H - 50), "CLICK CODED  ·  AI-operated, human-reviewed  ·  EU AI Act Article 50", font=mono(20), fill=DIM)

    os.makedirs(OUT_DIR, exist_ok=True)
    img.save(out_path, quality=95)
    print(f"saved {out_path}")


def thumb(out_path, headline_lines, tier_price, quote_lines, tiers, sub_label, tag_line):
    """v3, 2026-07-29: same copy-only revision as cover() -- see its docstring."""
    S = 1200
    img, d = new_canvas(S, S)
    top_bottom_bars(d, S, S, MINT, thickness=10)
    d.text((60, 54), "EU AI ACT 50 · ENFORCEABLE AUG 2, 2026", font=mono(19, True), fill=MINT)

    hero(d, 270, 850, 320, 640, 215, quote_lines, tiers)
    d.text((155, 488), "the 80-page kit", font=sans(19), fill=DIM)

    hy = 570
    for line in headline_lines:
        d.text((60, hy), line, font=serif(48, True), fill=INK)
        hy += 56
    hy += 12
    d.text((60, hy), tier_price, font=mono(22, True), fill=AMBER)
    d.text((60, hy + 36), sub_label, font=sans(26), fill=DIM)

    box_y = hy + 90
    d.rounded_rectangle([60, box_y, 1140, box_y + 90], radius=12, outline=MINT, width=2)
    d.text((88, box_y + 30), tag_line, font=serif(28, True), fill=INK)

    d.text((60, S - 60), "CLICK CODED · AI-operated, human-reviewed", font=mono(19, True), fill=DIM)

    os.makedirs(OUT_DIR, exist_ok=True)
    img.save(out_path, quality=95)
    print(f"saved {out_path}")


if __name__ == "__main__":
    single_quote = ["“You're chatting with [Your Business]'s AI", "assistant, not a human team member.”"]
    complete_quote = ["“You're chatting with [Your Business]'s AI", "assistant, not a human team member.”  +2 more"]

    single_headline = ["Your Exact AI", "Disclosure Sentence"]
    complete_headline = ["Every AI Disclosure", "Sentence You Need"]

    cover(os.path.join(OUT_DIR, "ai-act-fix-kit-cover.png"),
          single_headline, "FIX IT · $39", "The law requires this exact disclosure. We wrote it for your business.",
          single_quote, 1, "Answer 4 questions. Get the sentence. Paste it before Aug 2.")

    cover(os.path.join(OUT_DIR, "ai-act-fix-kit-complete-cover.png"),
          complete_headline, "FIX IT ALL · $69", "Chatbots, content, ads — one law, every disclosure covered.",
          complete_quote, 3, "Every touchpoint, not just one. Written, ready to paste.")

    thumb(os.path.join(OUT_DIR, "ai-act-fix-kit-thumb.png"),
          single_headline, "FIX IT · $39", single_quote, 1, "Answer 4 questions. Get the sentence.",
          "The law requires this. We wrote it for your business.")

    thumb(os.path.join(OUT_DIR, "ai-act-fix-kit-complete-thumb.png"),
          complete_headline, "FIX IT ALL · $69", complete_quote, 3, "Every touchpoint, not just one.",
          "Chatbots, content, ads — every disclosure covered.")
