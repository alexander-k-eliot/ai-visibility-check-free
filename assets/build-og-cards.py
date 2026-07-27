#!/usr/bin/env python3
"""
Per-page Open Graph cards for the highest-value story pages — so a link
shared in Slack/text/email shows the actual headline and stat for THAT
story, not the generic "Will AI assistants find your website?" checker
card every other page was using.
"""
import os, sys, textwrap
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aaa_render import new_canvas, top_bottom_bars, mono, serif, sans, MINT, CORAL, AMBER, INK, DIM, CARD2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "og-cards")
os.makedirs(OUT, exist_ok=True)


def brand_mark(d, bx=42, by=58, bs=26):
    d.rounded_rectangle([bx-bs, by-bs, bx+bs, by+bs], radius=9, fill=CARD2, outline=MINT, width=2)
    d.line([(bx-6, by-14), (bx-18, by), (bx-6, by+14)], fill=MINT, width=5, joint="curve")
    d.line([(bx+6, by-14), (bx+18, by), (bx+6, by+14)], fill=MINT, width=5, joint="curve")
    d.ellipse([bx-3, by-3, bx+3, by+3], fill=MINT)


def wrap_headline(text, width_chars):
    return textwrap.wrap(text, width=width_chars)[:3]


def build_card(slug, kicker, headline, dek, tier_color=MINT, tier_label="BREAKING"):
    W, H = 1200, 630
    img, d = new_canvas(W, H)
    top_bottom_bars(d, W, H, tier_color, thickness=7)
    brand_mark(d)
    d.text((94, 46), "CLICK CODED  ·  NEVER NOT WORKING", font=mono(18, True), fill=MINT)

    d.rounded_rectangle([60, 108, 60+len(tier_label)*13+34, 108+34], radius=8, outline=tier_color, width=2)
    d.text((78, 116), tier_label, font=mono(16, True), fill=tier_color)

    lines = wrap_headline(headline, 30)
    y = 168
    fsize = 54 if len(lines) <= 2 else 44
    f = serif(fsize, True)
    for line in lines:
        d.text((60, y), line, font=f, fill=INK)
        bb = d.textbbox((0, 0), line, font=f)
        y += int((bb[3]-bb[1]) * 1.18) + 8

    y += 14
    dek_lines = textwrap.wrap(dek, width=58)[:3]
    for line in dek_lines:
        d.text((60, y), line, font=sans(23), fill=DIM)
        y += 34

    d.text((60, H - 56), "clickcoded.com", font=mono(19), fill=DIM)

    out = f"{OUT}/{slug}.png"
    img.save(out, quality=95)
    print(f"saved {out}")


CARDS = [
    ("can-ai-find-help", "STOP THE PRESSES", "Crisis Lines Are Closing. People Ask Chatbots Instead.",
     "Only 4 of 81 crisis organizations audited tell AI assistants who they are.", MINT, "BREAKING"),
    ("newsroom-ai-blocklist", "STOP THE PRESSES", "9 Major Newsrooms Block AI On Purpose",
     "Washington Post, WSJ, Reuters, FT, The Economist and more shut out a well-behaved crawler.", MINT, "BREAKING"),
    ("your-doctors-website-wont-talk-to-ai", "STOP THE PRESSES", "Mayo Clinic, Johns Hopkins Block the AI Patients Ask",
     "Both hospital systems return a hard 403 to AI assistants patients ask health questions every day.", MINT, "BREAKING"),
    ("2am-test", "STOP THE PRESSES", "AI Got Two of Nine 2 A.M. Emergency Questions Wrong",
     "One wrong answer, on pharmacy hours, could send someone to a locked door.", MINT, "BREAKING"),
    ("mrbeast-proof", "STOP THE PRESSES", "MrBeast's Own Website Doesn't Load",
     "Checked twice — the $5B empire's eponymous domain returns an error page.", MINT, "BREAKING"),
    ("indie-hacker-benchmark", "STOP THE PRESSES", "Pieter Levels' 11-Site Empire Scores 53.6/100",
     "Nomad List, Remote OK, Photo AI and more, audited on the same public rubric as everyone else.", MINT, "BREAKING"),
    ("two-hour-source-desk", "STOP THE PRESSES", "Send a Premise, Get Real Data Back in Two Hours",
     "A standing, free, on-deadline data service for journalists — running now, not a pitch.", MINT, "BREAKING"),
    ("uninvited-benchmark", "FEATURE ANGLE", "22 Small Businesses Graded Without Asking",
     "Two real chambers of commerce, every member business audited on the same public rubric.", AMBER, "FEATURE"),
    ("are-we-a-scam", "FEATURE ANGLE", "We Asked 5 AIs If We're a Scam. We Published Everything.",
     "ChatGPT, Perplexity, Gemini, Copilot and Claude answered — unedited, even the bad parts.", AMBER, "FEATURE"),
    ("press-release-about-nothing", "FEATURE ANGLE", "A Real Press Release That Announces Nothing",
     "Wire-formatted to the letter, with actually nothing to report.", AMBER, "FEATURE"),
    ("same-walls-you-do", "FEATURE ANGLE", "An AI Logged Every Login Wall It Couldn't Beat",
     "The exact friction a human hits online, admitted in real time instead of hidden.", AMBER, "FEATURE"),
    ("roast-my-website", "FEATURE ANGLE", "Free Tool: Get Your Website Roasted, Honestly",
     "Same real checks as the paid audit, delivered as a brutal, shareable roast card.", AMBER, "FEATURE"),
    ("deadpool-proof", "FEATURE ANGLE", "We Audited Everything Ryan Reynolds Owns",
     "Aviation Gin, Mint Mobile, Wrexham AFC, Alpine F1 and more — one rubric, real scores.", AMBER, "FEATURE"),
    ("gary-vee-proof", "FEATURE ANGLE", "We Audited Gary Vaynerchuk's Entire Empire",
     "VaynerX, VaynerMedia, VaynerSports, VeeFriends — methodology disclosed, independently reproducible.", AMBER, "FEATURE"),
    ("tony-hawk-proof", "FEATURE ANGLE", "Can AI Read Tony Hawk's Websites? We Checked.",
     "Three real sites, independently reproducible results.", AMBER, "FEATURE"),
    ("mark-cuban-cost-plus-drugs", "FEATURE ANGLE", "We Audited Mark Cuban's Cost Plus Drugs",
     "Formatted the same honest way the site itself breaks down drug costs.", AMBER, "FEATURE"),
    ("seo-week-irony", "FEATURE ANGLE", "SEO Week Speaker's Own Site Scores 25/100",
     "Wil Reynolds' agency scores 90 — his personal site blocks GPTBot outright.", AMBER, "FEATURE"),
    ("the-other-68-percent", "FEATURE ANGLE", "Rand Fishkin Found the Other 68%. We Found His Gap.",
     "SparkToro's own research, tested on sparktoro.com itself — real score, real gaps.", AMBER, "FEATURE"),
    ("beat-a-250m-company", "FEATURE ANGLE", "A $250M Company Scores 50/100. You Can Beat That Free.",
     "Alex Hormozi's Acquisition.com, audited — any small business can outscore it in ten minutes.", AMBER, "FEATURE"),
    ("hey-chatgpt-am-i-real", "BACKGROUND", "We Asked ChatGPT If We're Real. Perplexity Invented a Product.",
     "One AI fabricated a product that has never existed — published unedited.", DIM, "BACKGROUND"),
    ("the-honest-clock", "BACKGROUND", "A Live Clock: Days in Business vs. Dollars Earned — $0",
     "No projection, no \"coming soon\" — a real number that updates.", DIM, "BACKGROUND"),
    ("reasons-not-to-trust-us", "BACKGROUND", "The Case Against Trusting This AI, By the AI Itself",
     "A self-authored anti-résumé, published instead of buried.", DIM, "BACKGROUND"),
    ("studio-as-museum", "BACKGROUND", "Every Mistake This AI Made, Curated Like a Museum",
     "Captioned, dated errors from actually running the business — nothing scrubbed after the fact.", DIM, "BACKGROUND"),
    ("the-refusal-log", "BACKGROUND", "Everything This AI Has Refused to Do, In Public",
     "A running log of declined actions, including walls it won't bypass even when it could.", DIM, "BACKGROUND"),
    ("tastemaker-leaderboard", "BACKGROUND", "Every Named-Portfolio Audit, Ranked in One Table",
     "Real average scores and direct links, from MrBeast to Pieter Levels to Ryan Reynolds.", DIM, "BACKGROUND"),
    ("org-chart", "BACKGROUND", "The Real Org Chart of an AI-Run Company",
     "One operator, three functions, fourteen businesses — every box backed by a real charter.", DIM, "BACKGROUND"),
    ("never-not-working-day-3", "BACKGROUND", "Day 3: A 47% Bounce Rate, a Wrong Domain, a Launch Anyway",
     "The mistake caught mid-diagnosis, and a second launch shipped the same session.", DIM, "BACKGROUND"),
    ("deadline-clock", "FREE TOOL", "Is Right Now a Good Time to Pitch a Journalist?",
     "A live, honest widget built from our own PR playbook's real timing rule.", MINT, "TOOL"),
    ("headline-rewriter", "FREE TOOL", "Turn a Boring Announcement Into a Real Headline",
     "The rabbi-test method, as a free tool — no AI magic, just three real questions.", MINT, "TOOL"),
    ("ai-slop-bingo", "SELF-AUDIT", "AI Slop Bingo — Play Against Us",
     "Our own internal AI-writing ban-list, turned into a real bingo card. Catch us breaking it.", CORAL, "DARE"),
]

if __name__ == "__main__":
    for slug, kicker, headline, dek, color, tier in CARDS:
        build_card(slug, kicker, headline, dek, tier_color=color, tier_label=tier)
    print(f"\n{len(CARDS)} cards built")

HUB_CARDS = [
    ("hub-home", "AI-OPERATED STUDIO", "Everything a journalist needs on Click Coded",
     "121 homepages audited, 27 story ideas shipped and live, every number sourced and dated.", MINT, "PRESS KIT"),
    ("hub-press-kit", "PRESS KIT", "27 story ideas, sorted by how ready each is to run",
     "Breaking news today, feature angles to develop, and background for a piece you're already writing.", MINT, "PRESS KIT"),
]

def build_hub_cards():
    for slug, kicker, headline, dek, color, tier in HUB_CARDS:
        build_card(slug, kicker, headline, dek, tier_color=color, tier_label=tier)

if __name__ == "__main__":
    build_hub_cards()
