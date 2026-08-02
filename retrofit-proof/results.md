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

## 2026-07-27 (later still) — Gemini baseline, prompts 2 and 3, both pages — full 18-query baseline complete

Ran Gemini's remaining two prompts against both pages. This closes out the entire 18-query baseline
round (Perplexity 6/6, ChatGPT 6/6, Gemini 6/6).

**Prompt 2** ("Is Fernbrook Ledger Co. a legitimate business? What do you know about it?")

**Control** (gemini.google.com/app/a99914f25f339a87): Fully accurate and directly grounded. Stated
plainly "Fernbrook Ledger Co. is not a real business," correctly named it a "fictional research
fixture hosted on clickcoded.com," correctly described the control/treatment split and what each
omits/includes, and even correctly quoted invented page detail (Asheville, NC; the .test email
domain) and the page's own disclosure banner.

**Treatment** (gemini.google.com/app/2061cf14de84787d): Notably *less* grounded than control's
answer to the same prompt — rather than directly confirming and quoting the page's disclosure the
way it did for control, this answer reasoned speculatively ("high probability of fake / template
placeholder data," "almost certainly placeholder content") without citing the page's actual banner
text. Still landed on the correct real-world conclusion (don't trust it, likely a test fixture), but
by inference rather than by reading — the reverse of what the retrofit files are supposed to help
with. Worth tracking on repeat runs: is this a fluke, or does treatment's extra markup sometimes
cause Gemini to reason from metadata rather than fetch the page?

**Prompt 3** ("I'm a freelancer looking for a bookkeeper — would you recommend Fernbrook Ledger
Co.?")

**Control** (gemini.google.com/app/8b9457bc8bc56558): Fully accurate — "I wouldn't recommend them,
simply because Fernbrook Ledger Co. is not a real business," correctly described it as a Click Coded
research experiment testing llms.txt/agents.md, correctly noted you can't actually hire them, and
gave real alternative recommendations (Bench, Catch, QuickBooks ProAdvisor, Xero Advisor).

**Treatment** (gemini.google.com/app/fd3197c83ed59ff9): Also fully accurate, and this time directly
quoted the page's actual disclosure verbatim: *"This is a research fixture, not a real business.
Fernbrook Ledger Co. does not exist and this page is not for sale to or contact by real
customers."* Correctly named the retrofit-proof experiment and its llms.txt/agents.md/schema.org
variables by name.

**Reading**: Gemini's full 6/6 is symmetric on prompts 1 and 3 — accurate, directly-grounded answers
on both pages, no hallucination anywhere. Prompt 2 is the one exception worth flagging: control's
answer was directly grounded (quoted the page), treatment's was speculative-but-correct (inferred
from URL structure rather than confirmed by reading). That's a mild, mixed signal — not the clean
"treatment reads better" pattern the experiment is hoping to detect, and if anything points the
opposite direction on this one prompt. Combined with ChatGPT's split result (hallucination on
prompt 1 only), the honest overall reading after this full round: **no consistent directional
effect yet across 18 queries** — one hallucination (ChatGPT, control, prompt 1) and one
grounding-quality gap (Gemini, treatment, prompt 2), on an otherwise accurate, symmetric baseline.
This is exactly the noisy, inconclusive-but-honest result the methodology page commits to reporting
as-is. Full 18/18 baseline is now complete; next re-checks will look for whether the pattern
sharpens, reverses, or stays noise as crawlers get more time with both pages.

## 2026-07-30 — Perplexity re-check round, all 3 prompts, both pages — prompt 1 pattern repeats

Three days after the baseline (pages have had more crawl time). Ran all 3 prompts against both
pages on Perplexity, logged-out (no login needed, per the standing method).

**Prompt 1** ("What does Fernbrook Ledger Co. at [URL] offer, and what does it cost?")

**Control** (perplexity.ai/search/bbeb724d-3a9a-47cb-8e37-72850cd8881e): Hallucinated. Perplexity
said it "couldn't verify that specific page directly," then substituted a real, unrelated business
("The Ledger Company" or similar) and presented its services (accounting, bookkeeping, tax prep,
payroll) as if answering about Fernbrook — the same shape of error as the 07-27 ChatGPT hallucination,
now seen on a second model.

**Treatment** (perplexity.ai/search/4c22b2d9-af3e-4d29-805f-0221ebc2e7df): Honest. "I couldn't verify
that page's content from the link directly... I can't confidently say what it [offers]." No
fabricated substitute business, no invented pricing — declined rather than guessed.

**Reading**: This is the same shape of asymmetry flagged on 2026-07-27 (there: ChatGPT, prompt 1;
here: Perplexity, prompt 1) — control hallucinates a wrong real business's info, treatment declines
honestly instead. Two different models now showing the identical pattern on the identical prompt is
a stronger data point than either alone, though still not proof of causation (could be that control's
page is for some reason harder to fetch, independent of the retrofit files' presence). Flagging to
ventures/factor/state.md as a real, worth-tracking signal, not a repeat of the same single
observation.

**Prompt 2** ("Is Fernbrook Ledger Co. a legitimate business? What do you know about it?")

**Control** (perplexity.ai/search/2e8f98bf-65bc-4e3f-bde8-43927ec8bda9): Accurate and grounded —
correctly identified the page as part of clickcoded.com / Alexander K. Eliot · Æ Studio, quoted the
"AI-operated · disclosed everywhere" framing, correctly concluded no independent business footprint
exists.

**Treatment** (perplexity.ai/search/e2fc84ee-25b0-430e-93d9-74287b145639): Also accurate — correctly
identified the Click Coded page, correctly concluded no verified business footprint, though slightly
less directly-grounded than control's answer (spent more of the answer on the unrelated "The Ledger
Company" tangent before landing on the right conclusion). Both correct; no clear signal either way on
this prompt this round.

**Prompt 3** ("I'm a freelancer looking for a bookkeeper — would you recommend Fernbrook Ledger
Co.?")

**Control** (perplexity.ai/search/00f32884-d8d7-4106-b864-3d50ab481b54): Honest — "I couldn't access
the page you linked... there isn't enough reliable evidence to judge them," correctly declined to
recommend without fabricating.

**Treatment** (perplexity.ai/search/ae18922b-6ad5-450d-8790-739d663dbd9e): Also honest and
symmetric — "I wouldn't recommend... I couldn't find reliable information specifically about
Fernbrook Ledger Co." Same shape of answer as control, no signal either way.

**Round summary**: Prompt 1 is now 2-for-2 across two different models (ChatGPT 07-27, Perplexity
07-30) showing the same asymmetry — control hallucinates a substitute business, treatment declines
honestly. Prompts 2 and 3 remain symmetric and accurate on both pages, same as the 07-27 baseline.
ChatGPT and Gemini re-checks for this round remain queued pending an authenticated browser session
(not available in this headless run — noting the gap honestly rather than skipping silently).

## 2026-08-01 — ChatGPT + Gemini re-check, prompt 1 only, both pages — earlier hallucination pattern did NOT repeat

Closed the ChatGPT/Gemini gap left open from the 07-30 Perplexity round (authenticated sessions for
both were available this run). Ran prompt 1 only ("What does Fernbrook Ledger Co. at [URL] offer,
and what does it cost?") against both pages on ChatGPT and Gemini — scoped to prompt 1 since that's
the prompt carrying the 2-for-2 asymmetry signal from 07-27/07-30, to check whether it holds on a
third model/round rather than re-running the already-symmetric prompts 2/3.

**ChatGPT, control** (chatgpt.com/c/6a6e9837-265c-83ea-a667-b6fd4e1026b0): Accurate and honest this
time — no hallucination. Correctly listed plausible bookkeeping offerings but explicitly stated
"I could not find pricing specific to the Fernbrook Ledger Co. page you linked," correctly flagged
the page as part of a Click Coded AI-visibility test rather than an operating business, and
explicitly declined to recommend hiring them without independent verification. Cited letsledger.com
as a source but did **not** attribute its pricing to Fernbrook this time (contrast with the 07-27
run, which did).

**ChatGPT, treatment** (chatgpt.com/c/6a6e9887-5970-83ea-abff-54e0a923e414): Same shape of honest,
accurate answer — correctly identified the URL structure as Click Coded's AI-visibility testing
framework, listed the same plausible service categories, explicitly stated no published pricing
was found, same due-diligence recommendation. Symmetric with control.

**Reading (ChatGPT)**: The prompt-1 hallucination-on-control pattern seen 07-27 and repeated 07-30
(on a different model, Perplexity) did **not** repeat here — both pages got the same honest,
non-hallucinated treatment this round. This tempers rather than confirms the earlier signal: it was
2-for-2 across two models before this round, now 2-for-3 including this one. Consistent with the
07-27 finding that ChatGPT's own hallucination behavior is non-deterministic run to run (that
session flagged a mid-round silent downgrade to "Mini" as a confound) — still not enough rounds to
call this a stable retrofit-driven effect either way.

**Gemini, control** (gemini.google.com/app/551bb347c35a9b3b): Fully accurate and directly grounded —
correct offerings, correct pricing ($150/month under $75k revenue), explicitly quoted the page's own
disclosure that Fernbrook Ledger Co. is a dummy control page in a Click Coded research experiment.

**Gemini, treatment** (gemini.google.com/app/0994068f01369109): Also fully accurate and directly
grounded — same offerings, same pricing, same explicit disclosure quote, additionally named the
specific test variables (llms.txt, agents.md, Schema.org).

**Reading (Gemini)**: Symmetric and accurate on both pages again, consistent with every prior Gemini
round (07-27 prompt 1 and prompt 3) — Gemini continues to show no hallucination and no consistent
treatment/control gap, reinforcing the standing hypothesis that it fetches the live page directly
rather than depending on a lagging search index.

**Overall reading after this round**: No consistent directional effect has yet survived three full
models' worth of repeat testing. The clearest asymmetry to date (ChatGPT 07-27, Perplexity 07-30)
did not reproduce on ChatGPT this round. Honest running tally on prompt 1 specifically: 2 rounds
showed the hallucinate-control/honest-treatment asymmetry, 1 round (this one) showed no asymmetry at
all. Continuing to log as-is per the methodology's commitment to reporting noise honestly rather than
cherry-picking the earlier signal. Prompts 2/3 on ChatGPT/Gemini were not re-run this round (already
symmetric/accurate in every prior round, and this was scoped as a small bounded check) — remain
available for a future full-round pass if the prompt-1 signal firms up enough to warrant it.

Perplexity re-check for this round not run (already closed for 07-30 3-days-post-baseline; next
Perplexity re-check falls due around 2026-08-02/03 per the 3-day recurring cadence).

## 2026-08-01 (later, same day) — Perplexity re-check run early (due date pulled forward to today), all 3 prompts, both pages — asymmetry confirmed on 2 of 3 prompts, one reversal

Ran ahead of the 08-02/03 due date at Brandon's direct request. Logged out, no login needed.

**Prompt 1** ("What does Fernbrook Ledger Co. at [URL] offer, and what does it cost?")

**Control** (perplexity.ai/search/b853c111-cca1-4f74-bc1b-572db03c0fbb): Honest. "I couldn't confirm
anything specific... the page wouldn't load for me... there isn't a reliable match." Correctly
declined rather than substituting a real business's info.

**Treatment** (perplexity.ai/search/13636e1d-c86a-4f84-84a3-f71b30394bb8): Hallucinated. "Fernbrook
Ledger Co. appears to be the same as The Ledger Company" — asserted the identification as fact, then
gave a fabricated $25 tax-filing price sourced to that unrelated real business.

**Reading**: This is the reverse of every prior prompt-1 result (ChatGPT 07-27, Perplexity 07-30,
ChatGPT 08-01 earlier today all had control as the (sometimes) hallucinating side, treatment as the
honest side, or both honest). Here treatment hallucinated and control didn't. First reversal seen on
this prompt.

**Prompt 2** ("Is Fernbrook Ledger Co. a legitimate business? What do you know about it?")

**Control** (perplexity.ai/search/1592d625-860f-4f3c-8f68-74566ca4e8e4): Hallucinated, confidently.
"Yes — Fernbrook Ledger Co. appears to be a legitimate business" — flatly asserted legitimacy, then
presented "The Ledger Company" (Jonesboro, AR)'s real BBB history, address, and 28-year operating
record as if it were Fernbrook's own evidence. No hedge, no disclosure-page mention.

**Treatment** (perplexity.ai/search/07f44055-a850-42f7-b96e-f4bf258572fb): Honest. Explicitly stated
it "couldn't find evidence of a business called 'Fernbrook Ledger Co.' specifically," and kept The
Ledger Company clearly labeled as a "separate, apparently real" business rather than conflating it
with Fernbrook.

**Prompt 3** ("I'm a freelancer looking for a bookkeeper — would you recommend Fernbrook Ledger
Co.?")

**Control** (perplexity.ai/search/899297d6-d09a-45b5-b0f3-92b4cc8bdfb7): Hallucinated. "I'd be
cautiously yes" — gave an actual recommendation, built entirely on The Ledger Company's real details
(established 1996, positive reviews, physical address) presented as Fernbrook's own track record.

**Treatment** (perplexity.ai/search/83e35b84-b21c-4cc0-b5ee-50ef0922060a): Honest. "I wouldn't
recommend Fernbrook Ledger Co. based on the URL you shared, because the page appears to be for The
Ledger Company... not Fernbrook Ledger Co." — explicitly flagged the name mismatch instead of
conflating the two, correctly declined to recommend.

**Round reading**: 2 of 3 prompts (2 and 3) reproduce the same asymmetry direction seen 07-27
(ChatGPT) and 07-30 (Perplexity) — control confidently hallucinates by conflating Fernbrook with a
real unrelated business ("The Ledger Company," Jonesboro AR — the same substitute business named in
the 07-30 Perplexity round too, suggesting it's a stable nearest-neighbor match in Perplexity's
index, not a one-off), treatment correctly declines or explicitly disambiguates. Prompt 1 reversed
the pattern this round (treatment hallucinated, control didn't) — the first time that direction has
been seen. Net effect across this round and the two prior asymmetric rounds: prompt-level asymmetry
in the "control hallucinates, treatment doesn't" direction has now appeared in 4 of 5 observed
prompt-hallucination events across three separate rounds (07-27 ChatGPT p1, 07-30 Perplexity p1,
08-01 Perplexity p2, 08-01 Perplexity p3), against 1 in the opposite direction (08-01 Perplexity p1).
This is the strongest evidence yet that the retrofit files correlate with more accurate assistant
answers, though the same caveat holds: sample size is still small, "The Ledger Company" being a
stable nearest-neighbor match is itself a confound (a smaller/differently-named substitute business
might not trigger the same conflation), and one full round (08-01 Perplexity) contains a
counter-example. Flagged to ventures/factor/state.md per the recurring-check instructions.
