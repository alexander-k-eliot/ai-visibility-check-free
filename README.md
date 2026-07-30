![Free AI Visibility Check — Click Coded](assets/readme-banner.png)

# Free AI Visibility Check

Will AI assistants (ChatGPT, Perplexity, Claude) be able to read your website? The URL-check runs
server-side (via `../free-checker-worker/`, a small Cloudflare Worker, live at
`checker.clickcoded.com`) so it works on real external sites instead of depending on browser CORS.
The paste-your-HTML mode stays fully client-side for anyone who'd rather not send us a URL at all.

Live: https://clickcoded.com/ai-visibility-check-free/

## What it checks
The full 12-check rubric (see `../methodology/`): title/meta, Open Graph, canonical tag, favicon,
JSON-LD structured data, no-JS legibility, contact path, llms.txt, llms-full.txt, agents.md,
robots.txt (per-crawler, evidence-cited), and sitemap. Results include the literal extracted
crawler-readable text (the "X-ray" panel), a per-bot access map grouped by AI company, and a Fix
Pack of generated llms.txt/llms-full.txt/agents.md/robots.txt/JSON-LD/sitemap.xml artifacts for
whatever failed. `?url=` on the page auto-runs a check — every result is a sendable link.

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

**Added 2026-07-30, two more real failure modes to check every time:**
6. Type a bare domain with **no scheme** (`stripe.com`, not `https://stripe.com`) directly into the
   live UI's input and submit it — a second, independent bug (native `type="url"` validation
   silently rejecting bare domains before any JS ran) hid behind the CORS bug for who knows how
   long. The input is `type="text"` now specifically to prevent this; if it regresses, the form
   silently does nothing again.
7. Fire ~25 rapid checks from one IP and confirm the UI shows a friendly rate-limit message,
   not a silent dead end (the frontend didn't handle the Worker's `{error}` responses until this
   pass — a rate-limited visitor previously saw nothing happen at all).

## Why it exists
We sell AI visibility audits ($25, human-reviewed, server-side, full fix list) on [Fiverr](https://www.fiverr.com/alexanderkeliot) and the Upwork Project Catalog ("Alexander E."). This free tool is the honest teaser. The site practices what it sells: JSON-LD, llms.txt, agents.md, full no-JS legibility.

By Click Coded. AI-operated, human-reviewed. Contact: run@clickcoded.com
