# Revenue Baseline — 2026 YTD (from Square + Stripe exports)

**Analyzed:** July 26, 2026  
**Sources:** Square transactions (Jan 6–Jul 25, 2026), Square customers (lifetime), Stripe customers (lifetime)  
**Raw files:** [`data/revenue/`](../../data/revenue/)

---

## TL;DR

1. **In-store (Square) is ~$112k net sales YTD** with a **median AOV of ~$49** — well below the plan’s ~$80–90 baseline estimate and the $95 90-day target.
2. **Online (Stripe/Squarespace) runs a much healthier ticket** — median ~$103 per payment — but we only have customer lifetime totals, not a clean monthly online revenue series yet.
3. **Biggest unlocks:** raise everyday POS AOV, capture emails/phones at checkout (only **55%** of Square txs have a customer ID; **~8%** of all Square customers have email), and treat Valentine’s + Mother’s Day as the revenue engine they already are.

---

## 1. Revenue dashboard summary

### Square POS + invoices (transaction-level, solid)

| Month | Payments | Net sales | AOV (net) | POS net | Invoice net |
|-------|----------|-----------|-----------|---------|-------------|
| 2026-01 | 218 | $15,436 | $70.81 | $12,419 | $3,017 |
| 2026-02 | 334 | $23,844 | $71.39 | $23,025 | $819 |
| 2026-03 | 233 (+1 refund) | $13,224 | $56.75 | $11,820 | $1,404 |
| 2026-04 | 204 (+2 refunds) | $12,974 | $63.60 | $12,279 | $694 |
| 2026-05 | 372 (+2 refunds) | $27,529 | $74.00 | $26,418 | $1,111 |
| 2026-06 | 157 | $9,292 | $59.18 | $8,896 | $396 |
| 2026-07 (through 25th) | 162 | $9,280 | $57.28 | $8,966 | $313 |
| **YTD** | **1,680 payments** (+5 refunds) | **$111,578** | **$66.22 mean / $48.87 median** | **$103,823 (93%)** | **$7,754 (7%)** |

Derived monthly file: [`square-monthly-summary-2026-ytd.csv`](../../data/revenue/square-monthly-summary-2026-ytd.csv)

**Seasonality (clear):**

| Window | Net sales | Share of YTD |
|--------|-----------|--------------|
| Valentine’s month (Feb) | $23,844 | 21% |
| Valentine’s week (Feb 7–14) | $13,237 | 12% |
| Mother’s Day month (May) | ~$27.9k | 25% |
| Mother’s week (May 4–10) | $17,765 | 16% |
| Soft months (Jun + Jul partial) | ~$18.6k combined | — |

Top days are almost entirely holiday peaks (May 9 $6.5k, Feb 13 $5.5k, May 10 $4.5k, Feb 14 $4.3k).

**Operating pattern:** Tue–Sat volume; **Monday = $0** (closed). Friday is the strongest weekday (~$30.5k YTD).

**Fees:** ~**3.0%** of total collected (~$3.5k YTD) — normal card processing, not a strategic leak.

**Discounts & tips in export:** both **$0** across all rows — either unused or not flowing into this report. Worth confirming in Square settings.

### Stripe / online (customer-level only — incomplete for monthly revenue)

| Metric | Value |
|--------|-------|
| Customers | 4,202 (all with email) |
| Lifetime spend (all-time) | **$720,801** |
| Lifetime payments | 6,395 |
| Refunded volume | $10,044 (~1.4%) |
| Dispute losses | $114 |
| Median spend / payment (proxy AOV) | **$102.60** |
| Mean spend / payment | $111.28 |
| One-time payers | 73.5% |
| Multi-payment customers | 20.9% (avg 3.8 payments, $441 lifetime) |
| New Stripe customers created in 2026 YTD | 362 · $50,462 lifetime spend on those profiles |

**Important caveat:** Stripe export is **lifetime spend per customer**, not charges by month. The ~$50k figure for 2026-created customers is a **lower bound** on 2026 online revenue (excludes returning buyers created in prior years). Need a Stripe **Payments** or **Balance transactions** export for a true online monthly series.

### Combined picture (directional)

| Channel | What we can say today |
|---------|----------------------|
| **In-store Square POS** | Dominant tracked channel; ~$104k net YTD; low AOV |
| **Square Invoices** | $7.8k YTD (47 txs); mean AOV **$165** — custom / delivery / larger orders |
| **Online (Stripe)** | Higher AOV (~$100+); email-rich; monthly $ unknown until payments export |
| **Wire / FTD** | Not in these files |
| **Subscriptions / weddings as tagged revenue** | Not separable cleanly from item names |

Simple Square run-rate (~$204k/year if every day matched YTD average) **understates** a full year because Jul is partial and Q4 holidays are ahead — but it confirms the shop is a **low-six-figures Square book** plus a meaningful online book on top.

---

## 2. Channel & product mix

### Tender / source

- **Card:** ~99.7% of collected value (mostly **tapped**)
- **Cash App:** ~$216 · **Cash:** ~$72
- **Source:** Point of Sale 93% / Invoices 7%
- **Channel / dining option fields:** blank on every row — no delivery-vs-pickup flag in this export

### Product signals (from Square line descriptions — messy naming)

Item names are inconsistent (`20`, `Item`, `45 bouquet`, `Bouquet`, `Touch of honey`). Equal-split revenue heuristic:

| Rough category | ~Share of net |
|----------------|---------------|
| Everyday arrangements | ~70% |
| Other / unclear SKUs | ~12% |
| Delivery fees | ~7% |
| Custom bouquets | ~6% |
| Gift certificates | ~2% |
| Wedding/event (incl. boutonnières) | &lt;1% tagged |
| Sympathy (named) | &lt;1% tagged |

**Implication:** Wedding and sympathy revenue is almost certainly **under-tagged** in POS (lives inside “Custom bouquet” / invoices). Don’t treat the &lt;1% figures as true channel size.

### Named bestsellers (noisy but useful)

High volume: generic **Bouquet**, price-named tiers (**20**, **45 bouquet**, **100 bouquet**, **50.00 Bouquet**), **Custom bouquet**, **Alameda delivery**, then named designs (**Touch of honey**, **Honey**, **Moon**, **Love / Love Poem**).

---

## 3. Customer & retention health

### Square customers (lifetime database)

| Metric | Value |
|--------|-------|
| Profiles | 17,526 |
| With lifetime spend | 17,411 · **$2.28M** lifetime |
| Median lifetime spend | $66.88 |
| Mean lifetime spend | $131 |
| Repeat buyers (2+ txs ever) | **31%** of buyers |
| One-time buyers | 69% |
| Active last visit in 2026 | **686** |
| **With email** | **1,316 (7.5%)** |
| With phone | 169 (1.0%) |
| Email subscribed | **2** (essentially unused) |
| Instant profiles (card-only) | 15,131 (86%) |

**2026 Square payment attachment:** 55% of transactions have a Customer ID; only 33% have a name. **~40% of YTD net sales is anonymous.**

### Stripe customers

- **100% email coverage** — this is the usable marketing list.
- Overlap with Square emails: only **129** people in both systems.
- Combined unique emails: **~5,350**.

### Concentration risk

- Top Square YTD named buyer (David Wendling) ~$2.7k / 22 visits — healthy regular, not dangerous concentration.
- **Anonymous + one-time holiday buyers** are the real concentration risk: peaks depend on walk-in/holiday traffic that doesn’t re-enter a CRM.

---

## 4. Baseline vs. plan targets

| Metric | Plan baseline (estimate) | **Measured now** | 90-day target |
|--------|--------------------------|------------------|---------------|
| Everyday AOV | ~$80–90 | **Square median $49 / mean $66**; Stripe proxy **~$103** | $95+ |
| Repeat customer rate | Unknown | Square lifetime **31%** (2+ txs); Stripe multi-pay **21%** | 35%+ |
| Gross margin | Unknown | **Still unknown** (no COGS) | 60%+ |
| Active subscriptions | Unknown | **Still unknown** | +10% |
| Online vs in-store mix | Unknown | Square solid; Stripe monthly incomplete | Track |

**Diagnosis from the four-lever framework:** primary problem is **AOV on everyday POS tickets**, second is **retention identity** (no email/phone at counter), third is **measurement gaps** (online monthly, subs, weddings, margin).

---

## 5. Prioritized growth levers (numeric)

### Lever A — Raise POS AOV from ~$49 median → $75–85 (P1)

**Why:** 40% of positive Square tickets are under $40; p75 is only ~$87. Online already clears $100 — in-store under-asks.

**Moves:**

1. Enforce a visible **good / better / best** ladder at the counter ($65 / $95 / $145+), not price-named SKUs like “20” and “45 bouquet”.
2. Default attach: card ($6.50) + vase/upgrade script; target **25%** card attach.
3. Bundle delivery into mid/high tiers so Alameda delivery isn’t a separate friction ask.

**Math sketch:** If half of the ~1,000 sub-$60 tickets lift by **$20**, that’s **~$10k** on the same traffic over a similar YTD window — before holiday peaks.

### Lever B — Capture identity on every paid order (P2)

**Why:** 40% of Square sales are anonymous; email list on Square is nearly unusable (2 subscribed). Stripe already proves online buyers will share email.

**Moves:**

1. Square checkout: require email **or** phone for all keyed/tapped payments (staff prompt + receipt SMS/email).
2. Sync Stripe + Square emails into one list (Mailchimp/Klaviyo); start with **~5,350** unique addresses.
3. Post-purchase: occasion capture (birthday/anniversary) — birthdays in Square today: **0**.

**Target (90 days):** ≥85% of Square txs with email or phone; ≥500 reachable 2026 buyers.

### Lever C — Build a holiday → everyday bridge (P2)

**Why:** Feb + May alone are ~46% of Square YTD. Without follow-up, those buyers vanish until the next holiday.

**Moves:**

1. After Valentine’s / Mother’s Day peaks: 7-day “thank you + next occasion” email/SMS to captured buyers.
2. Offer a **second-arrangement** or subscription trial to holiday buyers only.
3. Protect peak staffing/inventory — top single days already hit $4.5–6.5k.

**Target:** Convert **10%** of identifiable holiday buyers into a second purchase within 90 days.

---

## 6. Margin notes (limited by data)

- No COGS/wholesale file → **gross margin still unknown**.
- Processing fees (~3%) are fine; don’t optimize there first.
- Invoice AOV ($165 mean) and custom work look like the margin-friendly workstream — tag them (wedding / sympathy / corporate) so they can be priced and staffed deliberately.
- Catalog cleanup still matters: duplicate/ambiguous POS names hide true hero products and make recipe costing impossible.

**Next data ask for margin:** monthly wholesale stem spend + top 10 recipe costs.

---

## 7. 90-day action plan (data-backed)

| Window | Focus | Success metric |
|--------|-------|----------------|
| **Days 1–30** | Fix POS naming + price ladder; require email/phone at Square; export Stripe **payments**; fill scorecard monthly | Median POS ticket trending up; identity attach ≥70% |
| **Days 31–60** | Card/add-on default; merge email lists; win-back to 2026 Square buyers who have email | Card attach ≥15%; first retention campaign sent |
| **Days 61–90** | Occasion reminders live; subscription offer to multi-buyers; tag invoice types | Repeat rate among identified buyers ≥35%; scorecard complete for Q3 |

Ties to master plan Weeks 2–4 (AOV, capture/retain, measure/recost).

---

## 8. Data gaps still open

| Gap | Why it matters | Ask |
|-----|----------------|-----|
| Stripe payments by date | True online monthly revenue & seasonality | Stripe → Payments export (2024–2026) |
| Squarespace orders (if any beyond Stripe) | Confirm online = Stripe only | Commerce → Orders export |
| Subscriptions | MRR / churn / LTV | Active sub count + plan prices |
| Weddings | High-LTV pipeline | Annual events + average contract |
| COGS | Margin % | Wholesale spend monthly or QuickBooks |
| Delivery vs pickup | Ops cost | Enable dining/fulfillment fields or manual tag |
| Wire orders | Fee drag | FTD/Teleflora statements if used |

---

## Appendix — File checklist

| Provided | Status |
|----------|--------|
| Square transactions 2026 YTD | ✅ Ingested |
| Square customers | ✅ Ingested |
| Stripe customers | ✅ Ingested (lifetime only) |
| Duplicate Square transactions export | ✅ Deduped (identical) |
