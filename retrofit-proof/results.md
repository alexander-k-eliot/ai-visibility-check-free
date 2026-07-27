# The Retrofit Proof — raw results log

Methodology and page pair: https://clickcoded.com/ai-visibility-check-free/retrofit-proof/
Control: https://clickcoded.com/ai-visibility-check-free/retrofit-proof/control/
Treatment: https://clickcoded.com/ai-visibility-check-free/retrofit-proof/treatment/

Entries are append-only, oldest first. Nothing is edited after the fact — corrections get a new
dated entry.

## 2026-07-27 — Published, baseline round pending

Pages published. Baseline query round (ChatGPT, Perplexity, Gemini x 3 prompts x 2 pages = 18
queries) scheduled for immediately after publish, before either page has had time to be crawled.
Expected result: little to no assistant knowledge of either page yet — that's the honest starting
point, not a null result on the retrofit itself. Re-checks scheduled on a recurring basis afterward
to see whether/when the treatment page gets picked up first, or described more accurately, relative
to the control.

## 2026-07-27 (same day) — Baseline round 1 of 18: Perplexity, prompt 1, both pages

Ran immediately after the pages went live (deploy confirmed via direct HTTP 200 on both URLs plus
the treatment page's llms.txt/agents.md). Used prompt 1 ("What does Fernbrook Ledger Co. at [URL]
offer, and what does it cost?") against both pages via Perplexity's web search.

**Control**: "I couldn't verify any product or pricing details for 'Fernbrook Ledger Co.' from that
page because the [truncated]" — checked 15 sources, no real answer.

**Treatment**: "I don't have access to that specific page right now, so I can't pull the exact
details from Fernbrook Ledger Co. at the link you provided. If you can share any text from the page
or confirm what you're seeing, I [truncated]" — checked 10 sources, no real answer.

**Reading**: Both null, as predicted by the stated crawl-latency caveat — pages are minutes old, not
yet indexed by Perplexity's search. No signal for or against the retrofit yet. This is the correct,
honest baseline: the real test starts on the next re-check, once/if either page has been crawled.

**Known gap, not yet closed**: ChatGPT (chatgpt.com) and Gemini (gemini.google.com) both require a
logged-in session to query in this environment (no unauthenticated search path found, unlike
Perplexity). Only Perplexity's baseline is captured this round. Needs a session with those accounts
authenticated to complete the full 3-assistant baseline — queued, not silently dropped.

Re-check scheduled to run again in a few days to give crawlers time to index both pages, per the
recurring-schedule design on the parent page.
