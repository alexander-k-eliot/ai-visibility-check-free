![Free AI Visibility Check — Click Coded](assets/readme-banner.png)

# Free AI Visibility Check

Will AI assistants (ChatGPT, Perplexity, Claude) be able to read your website? The URL-check runs
server-side (via `../free-checker-worker/`, a small Cloudflare Worker) so it works on real external
sites instead of depending on browser CORS. The paste-your-HTML mode stays fully client-side for
anyone who'd rather not send us a URL at all.

Live: https://clickcoded.com/ai-visibility-check-free/

## What it checks
Title and meta description, JSON-LD structured data, no-JS legibility, contact path, llms.txt,
llms-full.txt, agents.md, robots.txt (per-crawler, evidence-cited), and sitemap. Results include the
literal extracted crawler-readable text (the "X-ray" panel), a per-bot access map, and a Fix Pack of
generated llms.txt/robots.txt/JSON-LD artifacts for whatever failed.

## Pre-launch/relaunch protocol — non-negotiable, added 2026-07-29
This tool was live on Product Hunt (2026-07-24) in a state where entering almost any real external
URL returned a broken 0/100 (a client-side CORS limitation nobody tested against a real domain
before shipping). **Before any future public push — Product Hunt, social, a directory, a
newsletter — run the live check against these 5 archetype URLs and confirm all pass:**
1. A large well-known site (e.g. a Fortune-500 domain)
2. A real small/local business site
3. A JS-heavy single-page app
4. A site with an AI-crawler-blocking robots.txt
5. clickcoded.com itself (control)

Require: non-zero, differentiated scores on the working sites; correct per-bot allow/block rows;
the X-ray panel actually rendering extracted text. **Any unexplained 0/100 on a known-working
external site blocks the launch, no exceptions.** This is a 5-minute check — cheaper than a repeat
of the 07-24 launch.

## Why it exists
We sell AI visibility audits ($25, human-reviewed, server-side, full fix list) on [Fiverr](https://www.fiverr.com/alexanderkeliot) and the Upwork Project Catalog ("Alexander E."). This free tool is the honest teaser. The site practices what it sells: JSON-LD, llms.txt, agents.md, full no-JS legibility.

By Click Coded. AI-operated, human-reviewed. Contact: alexander.k.eliot@gmail.com
