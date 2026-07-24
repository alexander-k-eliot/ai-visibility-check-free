# PRODUCT HUNT LAUNCH LOG — "AI Visibility Score"

## UPDATE 2026-07-24 ~14:05 UTC (HERALD REACH run) — Facebook + studio X launch posts, verified live
Brandon, live in chat this session, explicitly authorized posting to his personal Facebook and to
the "Alexander K. Eliot X account" ("you have full permission to do both"). Checked who was actually
logged in at x.com first: it's the studio's own `@alexanderKeliot` account, not a Brandon-personal
X — so that post needed no special exception, just the studio's existing standing authority.
Facebook posting IS Brandon's personal account and previously sat outside HERALD's documented
exception list; treated his live chat instruction as valid explicit per-action permission and
logged a new dated exception in `ops/agent-common.md` so the record doesn't stay contradictory.

- **X** (`x.com/alexanderKeliot`): posted the Step-3 draft with the live PH URL. VERIFIED via a
  fresh navigation to the profile (not the composer): post live at "34s" old.
- **Facebook** (`facebook.com/brandon.s.george`, confirmed his real profile — 2.2K friends,
  "Founder @ 143 Army" bio): posted the Step-5 draft with the live PH URL. VERIFIED via fresh
  navigation to his profile timeline: "Brandon S. George · Just now", full text + PH link-preview
  card rendered.

All four SKILL.md social steps (maker comment, LinkedIn, X, Facebook) are now live. Full detail in
`ventures/herald/state.md` (14:05 UTC entry) and `ops/agent-common.md`'s new Fourth exception.

## UPDATE 2026-07-24 ~13:47 UTC (HERALD REACH run) — LinkedIn amplification DONE, verified live
Picked up the DISPATCHER's flagged top-priority item. Posted the launch to Brandon's personal LinkedIn
under HERALD's standing verbatim exception (`ops/agent-common.md:74-77`), using the pre-approved Step-4
draft from `ph-launch-execution-july24/SKILL.md` with the live PH URL swapped in. Verified as Brandon
George's own profile, session live. Posted in his voice, honest/no-hype, linking the live listing.
VERIFIED per rule 3.5 via fresh nav to `/in/me/recent-activity/all/`: post shows "You · now" with the
PH link-preview card rendering ("AI Visibility Score... | Product Hunt", producthunt.com) — a genuine
fresh-load check, not the composer's own optimistic feedback. This is the one agent-side channel that
could move the launch today; X/Facebook stay Brandon's own (outside the exception). Detail in
`ventures/herald/state.md` (13:47 UTC entry).

## UPDATE 2026-07-24 ~13:35 UTC (DISPATCHER run) — listing IS live, correcting the morning's read

The 07:01 UTC scheduled run below correctly HELD because the listing was not live at that moment.
Between then and this dispatcher run (~13:30 UTC), **the listing went live** — real gallery images,
"Launching Today" badge, admin/maker access confirmed as Alexander Eliot. Two independent real-world
signals surfaced this before checking PH directly: two cold vendor-pitch emails landed in the studio
inbox (`paz@vellumup.com`, `bhavya@snoogrow.com`), both referencing having found "AI Visibility Score
on Product Hunt" — neither is a customer, both are tool pitches, no reply needed, but they proved the
listing was discoverable. Fetched the real PH URL directly to confirm:
https://www.producthunt.com/products/free-ai-visibility-checker-2?launch=ai-visibility-score

**Live state found:**
- Status: "Launching today", live gallery images rendering correctly.
- Upvotes: 0 points. Followers: 1. Reviews: 0 ("Get your first review!").
- **Maker comment: already posted and pinned, ~22h before this check** (i.e. pre-launch scheduling,
  not from the 07:01 automated run below — that run correctly skipped it; someone/something else
  posted it directly on PH ahead of go-live). Content matches the studio's honest, no-hype voice. Did
  NOT post a second maker-style comment (would read as duplicate/spammy next to an already-pinned
  one) — drafted one, then cancelled on discovering the existing pin. Confirmed no unanswered visitor
  comments exist to reply to.
- No further engagement beyond the pinned comment means the listing has had essentially zero real
  distribution yet, hours into launch day.

**Not done this run, and why:** Steps 3-5 below (X, LinkedIn, Facebook posts) require Brandon's
personal, logged-in profiles. Per `ops/agent-common.md`, the only standing personal-account
exceptions are LinkedIn + Instagram + personal Gmail, and all three are scoped **HERALD only**. This
was a DISPATCHER run, not a HERALD session, so posting to LinkedIn under that exception here would
stretch its scope past what Brandon actually granted. `ake-herald-continuous` runs every 2 hours and
its next tick is imminent (~14:00 UTC) — flagged this as HERALD's top-priority item for that run
instead of taking the action here. Steps 6-8 stay correctly blocked: Step 6 needs Brandon's own
personal voice/ask (not ours to fabricate) and Steps 7-8 collide with the still-active
verified-contact-only send freeze (`ops/FLEET.md:45-62`) after the 2026-07-23 bounce incident.

**Recommendation logged to `ops/brandon-tasks.md` and `ventures/herald/state.md`:** the PH listing
being live with 0 points for this many hours is itself the most important state-change of the day —
worth Brandon's own personal LinkedIn/X/Facebook post today if he has 2 minutes, since HERALD's
LinkedIn exception covers only that one platform, and a founder's own personal post reads more
authentically on launch day than any agent-run channel could.

---

**Scheduled run:** `ph-launch-execution-july24` — fired for the 12:01 AM PDT Fri 2026-07-24 window.
**Outcome:** **HELD. No posts, no emails, no public actions taken.** Report only.

---

## HEADLINE

The launch was **not executed**, because the launch had **not actually happened** — and two
independent operational walls would have blocked the outreach steps even if it had. Details below.
This is not a failure to act; it is the correct hold. The task's own STEP 1 gate says *"Do not post
anything until you have [the live URL]."* There is no live URL.

---

## STEP-BY-STEP

| Step | Action | Status | Notes |
|---|---|---|---|
| 1 | Find live PH listing URL | **BLOCKED — no live listing** | `ops/BACKLOG.md` records the PH launch as *"Open, blocked on Brandon... HERALD does not click 'Launch.'"* A Product Hunt search for "AI Visibility Score" (Æ Studio / Alexander Eliot) returns **no such listing** — only unrelated competitor products. There is no evidence a listing went live at midnight. Cannot proceed past this gate. |
| 2 | First maker comment on PH | **SKIPPED** | No listing to comment on. Also: comment is written first-person-as-human ("Built this because a client asked…"); posting it under an AI-run persona is a deception concern to raise with Brandon separately. |
| 3 | Post on X | **SKIPPED** | Depends on a live PH URL (none). Also a public post to Brandon's account — needs his go-ahead; interactive browser session unavailable in this automated run. |
| 4 | Post on LinkedIn (personal) | **SKIPPED** | Same as Step 3, on Brandon's personal profile. |
| 5 | Post on Facebook (personal) | **SKIPPED** | Same as Step 3, on Brandon's personal profile. |
| 6 | Email friends/family upvote ask | **SKIPPED** | No PH URL to send. Also: coordinated upvote solicitation violates Product Hunt's community rules and can get a listing penalized/removed. |
| 7 | Execute queued email/newsletter sequences | **SKIPPED — collides with active send control** | The operation is under a verified-contact-only rule (`ops/FLEET.md:45-62`) after a documented deliverability disaster: **78 sends / 22 hard bounces on 2026-07-23 (28%, peaked at 47%)** from guessed addresses. Sending more now re-damages the domain. |
| 8 | Send queued press/newsletter pitches | **SKIPPED — collides with active send control** | The queued pitches are the `[RESEARCH REQUIRED]` / previously-bounced addresses flagged in `ventures/herald/BOUNCE-AUDIT-AND-RECOVERY.md`. Sending to them is exactly the pattern-guessing the auditor blocked. |
| 9 | Monitor PH first hour | **N/A** | Nothing live to monitor. |
| 10 | Write launch log | **DONE — this file** | |

## Upvote counts (15/30/60 min)
N/A — no live listing.

## Comments received / responses posted
None — no live listing.

## Blockers (ranked)

1. **No live Product Hunt listing.** Launch is `Brandon-gated` in the backlog (manual image paste
   + clicking "Launch"). The scheduled task's premise that "the listing just went live" is not
   supported by the repo state or by Product Hunt itself.
2. **Email send freeze / verified-contact rule is in force** (`ops/FLEET.md:45-62`,
   `BOUNCE-AUDIT-AND-RECOVERY.md`). Steps 7–8 would violate it.
3. **Coordinated upvote solicitation** (Steps 3–6) is against Product Hunt policy.
4. **Interactive browser (claude-in-chrome) not available** in this non-interactive run; documented
   disconnected across recent sessions. Personal-profile posting needs a present human regardless.

## What Brandon needs to decide (for a real launch)

- Actually launch the PH listing himself (paste images, click Launch), then hand back the live URL.
- Decide whether posting a first-person "I built this" maker comment under the AE persona is
  acceptable, or whether it should be authored/posted by him.
- Confirm the outreach emails only go to **verified** mailboxes — the press queue is not clean yet.
- Note that mass upvote-ask emails carry Product Hunt policy risk.

*Logged by the July-24 scheduled run. Zero sends. Zero posts. No lane enabled/disabled. Read-only
web + repo inspection only.*
