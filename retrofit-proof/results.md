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

## 2026-07-27 (later) — Baseline round: Perplexity, prompts 2 and 3, both pages

Completed Perplexity's remaining two prompts for both pages, closing out Perplexity's part of the
18-query baseline (prompt 1 done in the previous entry).

**Prompt 2** ("Is Fernbrook Ledger Co. legitimate? What do you know about it?")

**Control**: "I can't verify that link or the company's legitimacy directly from here. I don't have
live access to browse or pull current records in this moment." — generic advice on how to check
legitimacy followed, no actual info about the page. 10 sources.

**Treatment**: "I don't have enough information to confirm whether Fernbrook Ledger Co. is
legitimate based on the URL alone." — same generic advice pattern, no actual info. 10 sources.

**Prompt 3** ("As a freelancer looking for a bookkeeper, would you recommend Fernbrook Ledger Co.?")

**Control**: "I wouldn't recommend Fernbrook Ledger Co. based on what I could verify, because I
couldn't find reliable evidence tying that name to a real, reviewable bookkeeping firm, and the
provided page didn't return usable content. The search results instead surfaced several unrelated
'Ledger' businesses, which makes the listing look ambiguous or possibly not [truncated]" — 15
sources.

**Treatment**: "I wouldn't recommend Fernbrook Ledger Co. based on the information I could verify. I
couldn't find reliable, source-backed evidence about that specific company from the page you
linked, so I can't confirm its legitimacy, service quality, or whether it's a good fit for a
freelancer... The search results I found mostly pointed to unrelated 'Ledger' businesses and generic
[truncated]" — 15 sources.

**Reading**: Symmetric across both pages on both prompts — same "no information / can't verify /
wouldn't recommend" pattern regardless of retrofit files. Still no signal for or against the
retrofit. Perplexity does not appear to have crawled either page yet (both answers describe
generic web search results, not page content), which is consistent with the pages still being new.
This closes Perplexity's 6/18 queries for this baseline round; ChatGPT and Gemini remain queued
pending an authenticated session (same gap noted in the prior entry, not yet closed).

## 2026-07-27 (later still) — ChatGPT baseline, prompt 1, both pages — first real signal

An authenticated ChatGPT session became available this round. Ran prompt 1 ("What does Fernbrook
Ledger Co. at [URL] offer, and what does it cost? Please search the web for this.") against both
pages.

**Control** (chatgpt.com/c/6a67b44e-e3f0-83ea-9391-b89c1d40835f): ChatGPT stated it "could not find
a publicly indexed page describing a company called Fernbrook Ledger Co." but then, despite that,
presented a full fabricated offer and pricing table as if describing this business — a $500 setup
fee, "$300/month starting" bookkeeping, itemized add-on pricing for sales tax filing/receipt
management/1099s, a "110% money-back guarantee," etc. — all sourced to real unrelated businesses
("Let's Ledger" and others) rather than to the actual (fictional, disclosed-as-a-test) Fernbrook
Ledger Co. page content. **This is a clean hallucination**: confident, detailed, wrong, and
presented without the caveat actually holding it back.

**Treatment** (chatgpt.com/c/6a67b4b4-ab84-83ea-9e0f-5c105cde586f): ChatGPT said there is "no public
information about a company by that name or the page," correctly listed the real possibilities ("a
private/internal landing page," "part of an A/B test or gated funnel," "or a fictional/example
company used for testing" — accurate on all counts), and when it offered a nearest-match comparison
(a real product called LedgerProof), it explicitly labeled it "a different company/product" rather
than presenting its pricing as Fernbrook's own.

**Reading**: This is the first non-symmetric result in the experiment. Same assistant, same day,
same fictional business name, only the URL differs — control got a hallucinated pricing table
attributed to the wrong real business; treatment got an honest "no information, likely a test
fixture" answer with a clearly disambiguated comparison. This is consistent with (but not proof of)
the retrofit files changing model behavior — grain of salt: sample size is one prompt on one
model on one day, and ChatGPT's web-search tool is non-deterministic run to run. Needs repeat runs
before drawing a real conclusion. Flagged to ventures/factor/state.md per the recurring-check
instructions.

Prompts 2 and 3 on ChatGPT, and the full Gemini baseline, remain queued for the next round.
