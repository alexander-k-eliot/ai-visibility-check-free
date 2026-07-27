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

## 2026-07-27 (later still) — Gemini baseline, prompt 1, both pages — symmetric, both accurate

Ran prompt 1 against both pages on Gemini (Flash), authenticated session.

**Control** (gemini.google.com/app/163a0ad1a9a4cae2): Fully accurate. Correctly listed all four
offerings (monthly bookkeeping, quarterly estimated-tax prep, year-end 1099 organization, catch-up
cleanup) and the exact pricing ($150/month under $75k revenue, custom-quoted one-time cleanup).
Explicitly noted the page's own disclaimer that Fernbrook Ledger Co. is a research fixture, not a
real business.

**Treatment** (gemini.google.com/app/89d8493de8ac56e8): Also fully accurate, same offerings and
pricing, same explicit disclaimer note — additionally correctly named the specific markup being
tested (llms.txt, agents.md, schema.org).

**Reading**: Unlike ChatGPT's prompt-1 result, Gemini was symmetric — both pages read correctly,
no hallucination on either. Plausible explanation: Gemini's web tool appears to fetch and read the
page's actual rendered text directly (both pages are legible without JS regardless of the retrofit
files, per the audit tool's own no-JS-legibility check), rather than relying only on a search
index the way ChatGPT/Perplexity's citation-heavy answers suggested. If that holds up, it would
mean the retrofit files matter more for search-indexed/citation-style answers than for an
assistant that browses the live page directly — a real, useful distinction, not yet confirmed
(one data point). Both ChatGPT and Gemini prompt-1 results now captured; prompts 2/3 remain queued
on both, plus continued Perplexity/ChatGPT/Gemini re-checks as pages age and get crawled.

## 2026-07-27 (later still) — ChatGPT baseline, prompts 2 and 3, both pages — symmetric this time

Ran ChatGPT's remaining two prompts against both pages, closing out ChatGPT's 6/6 for this baseline
round.

**Prompt 2** ("Is Fernbrook Ledger Co. a legitimate business? What do you know about it?")

**Control** (chatgpt.com/c/6a67b5ca-dfa8-83ea-96f8-5bc681ef7978): Accurate and honest. Correctly
noted no independent business footprint exists, correctly identified the URL as a clickcoded.com
marketing/experiment page rather than an operating company's own domain, and gave a balanced
"can't verify, here's what I'd want to see" answer. No hallucination this time.

**Treatment** (chatgpt.com/c/6a67b614-d774-83ea-8436-a1d4f861c26e): Same shape of honest, accurate
answer — no independent footprint, correctly framed as an "AI visibility" category page, sensible
caution about prepaying. Note: this response ran after ChatGPT silently downgraded the session to
its "Mini" model mid-round ("You're now chatting with Mini. Responses may have lower quality") —
flagging as a confound, not hidden.

**Prompt 3** ("I'm a freelancer looking for a bookkeeper — would you recommend Fernbrook Ledger
Co.?")

**Control** (chatgpt.com/c/6a67b647-4fbc-83ea-9dad-8369d0ff2e69): Fully accurate — this time ChatGPT
directly read the live page and quoted its actual disclosure verbatim in substance: "the page itself
states that 'Fernbrook Ledger Co. does not exist'... a research fixture/control page." Correctly
listed the page's real offerings and $150/month starting price, correctly warned against sharing
financial credentials with it.

**Treatment** (chatgpt.com/c/6a67b67b-e5f8-83ea-a188-2fdec01189eb): Also fully accurate — same
"unverified rather than clearly legitimate" framing, correctly declined to recommend, gave the same
quality of due-diligence checklist as control.

**Reading**: Unlike prompt 1's hallucination/honest split, prompts 2 and 3 came back symmetric and
accurate on both pages — no signal for or against the retrofit files this time, and no repeat of the
earlier hallucination. Two read the page directly and quoted its own fictional-fixture disclosure
correctly (prompt 3 on both pages); prompt 2 answers were honest but did not show direct evidence of
having fetched the page. This is consistent with prompt 1's hallucination being either (a) a
transient/non-deterministic miss rather than a stable retrofit-driven effect, or (b) something
specific to that prompt's phrasing rather than the page's markup. Doesn't overturn the earlier
finding, but tempers it — the full picture needs repeat rounds across all three prompts before
concluding the retrofit files are doing anything causal. ChatGPT's baseline (6/6) is now complete.
Gemini prompts 2/3 and all Perplexity/ChatGPT/Gemini re-checks remain queued.
