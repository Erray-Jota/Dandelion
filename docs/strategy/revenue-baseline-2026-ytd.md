# Revenue Baseline — 2026 YTD (Square + Squarespace + Stripe)

**Analyzed:** July 26, 2026 (updated with Squarespace orders + Stripe payments)  
**Sources:** Square transactions (Jan 6–Jul 25, 2026), Square customers (lifetime), Squarespace orders (May 2015–Jul 24, 2026), Stripe payments (May 2015–Jul 25, 2026), Stripe customers (lifetime)  
**Raw files:** [`data/revenue/`](../../data/revenue/)

---

## TL;DR

1. **Two-channel business:** Square in-store ~**$112k** net YTD + Squarespace online ~**$90k** paid totals YTD ≈ **~$185–201k** combined depending on tax/shipping definition.
2. **AOV gap is the story:** Square median **$49** vs Squarespace median **$121** (total) / **$95** (product subtotal). Online already hits the plan’s $95 target; the counter does not.
3. **Online is rebounding in 2026** — YTD through Jul 24 is **+$26k / +41%** vs 2025 YTD — but full-year online peaked in 2021 ($150k) and drifted down through 2025.
4. **Card attach online is ~0.6%** despite a $6.50 add-on SKU. Hero catalog is concentrated: top 5 arrangements = **68%** of 2026 online product revenue.
5. **Stripe payments confirm Squarespace** — 9,339/9,346 orders match (99.9%); online processing fees ~**3.2%** in 2026 (~$2.9k YTD).
6. **Biggest unlocks:** raise POS AOV to match online ladder, default the card add-on, capture emails at Square, grow subscriptions off the holiday + multi-buyer base.

---

## 1. Revenue dashboard summary

### Combined 2026 YTD (through late July)

| Channel | Metric | Amount | Orders | AOV |
|---------|--------|--------|--------|-----|
| Square POS + invoices | Net sales | **$111,578** | 1,680 payments | mean $66 / median **$49** |
| Squarespace (Stripe) | Order total (incl. tax + shipping) | **$89,835** | 678 paid | mean $133 / median **$121** |
| Squarespace | Product subtotal (ex tax/ship) | **$73,212** | 678 | mean $108 / median **$95** |
| **Combined (approx.)** | Square net + SS subtotal | **~$185k** | — | — |
| **Combined (cash-ish)** | Square net + SS total | **~$201k** | — | — |

Definitions differ (Square net sales vs Squarespace checkout total). Use **Square net + SS subtotal (~$185k)** for product-mix comparisons; use cash-ish for “money in the door.”

### Square POS + invoices

| Month | Payments | Net sales | AOV (net) | POS net | Invoice net |
|-------|----------|-----------|-----------|---------|-------------|
| 2026-01 | 218 | $15,436 | $70.81 | $12,419 | $3,017 |
| 2026-02 | 334 | $23,844 | $71.39 | $23,025 | $819 |
| 2026-03 | 233 (+1 refund) | $13,224 | $56.75 | $11,820 | $1,404 |
| 2026-04 | 204 (+2 refunds) | $12,974 | $63.60 | $12,279 | $694 |
| 2026-05 | 372 (+2 refunds) | $27,529 | $74.00 | $26,418 | $1,111 |
| 2026-06 | 157 | $9,292 | $59.18 | $8,896 | $396 |
| 2026-07 (through 25th) | 162 | $9,280 | $57.28 | $8,966 | $313 |
| **YTD** | **1,680** (+5 refunds) | **$111,578** | **$66.22 / $48.87 med** | **93%** | **7%** |

Derived: [`square-monthly-summary-2026-ytd.csv`](../../data/revenue/square-monthly-summary-2026-ytd.csv)

**Seasonality (Square):** Valentine’s month 21% of YTD; Mother’s Day month ~25%. Closed Mondays. Friday strongest weekday. Card fees ~3% of collected.

### Squarespace online (order-level — primary online source)

All paid orders process via **Stripe**. Derived rollups: [`squarespace-monthly-summary.csv`](../../data/revenue/squarespace-monthly-summary.csv) · [`squarespace-yearly-summary.csv`](../../data/revenue/squarespace-yearly-summary.csv)

#### 2026 monthly

| Month | Paid orders | Total | Subtotal | Shipping | AOV (total) |
|-------|-------------|-------|----------|----------|-------------|
| 2026-01 | 79 | $9,901 | $7,964 | $1,100 | $125 |
| 2026-02 | 172 | $22,116 | $18,313 | $1,868 | $129 |
| 2026-03 | 83 | $12,133 | $9,864 | $1,216 | $146 |
| 2026-04 | 78 | $10,152 | $8,087 | $1,196 | $130 |
| 2026-05 | 168 | $22,521 | $18,496 | $2,044 | $134 |
| 2026-06 | 45 | $5,754 | $4,599 | $668 | $128 |
| 2026-07 (through 24th) | 53 | $7,258 | $5,891 | $744 | $137 |
| **YTD** | **678** | **$89,835** | **$73,212** | **$8,836** | **$133** |

#### Annual online history (paid totals)

| Year | Orders | Total | AOV |
|------|--------|-------|-----|
| 2015 (partial) | 191 | $16,670 | $87 |
| 2016 | 372 | $32,827 | $88 |
| 2017 | 381 | $35,618 | $93 |
| 2018 | 418 | $41,626 | $100 |
| 2019 | 509 | $50,315 | $99 |
| **2020** | **1,392** | **$127,431** | $92 |
| **2021 (peak)** | **1,525** | **$150,199** | $98 |
| 2022 | 1,214 | $136,357 | $112 |
| 2023 | 984 | $110,123 | $112 |
| 2024 | 853 | $107,984 | $127 |
| 2025 | 829 | $106,459 | $128 |
| 2026 YTD (to Jul 24) | 678 | $89,835 | $133 |

**Same-window YTD comparison (through Jul 24):**

| Year | Orders | Total | vs prior |
|------|--------|-------|----------|
| 2024 | 596 | $72,991 | — |
| 2025 | 512 | $63,586 | −13% |
| **2026** | **678** | **$89,835** | **+41% vs 2025 YTD** |

So 2026 online is **ahead of last two years’ YTD**, even though full-year 2024–2025 settled near ~$106–108k after the 2021 peak. AOV has climbed steadily ($87 → $133) while order count never recovered to 2020–21 levels.

#### Fulfillment mix 2026

| Method (normalized) | Orders | Total | Share |
|---------------------|--------|-------|-------|
| Alameda / Bay Farm delivery | 486 | $67,254 | 75% |
| “Dandelion Flowers & Gifts” (blank ship city — treat as **pickup**) | 139 | $14,996 | 17% |
| East Bay delivery (Oakland/Berkeley/etc.) | 53 | $7,586 | 8% |

Hyperlocal: **94501 + 94502** dominate ship zips; Alameda is the core delivery market.

### Stripe payments (confirms Squarespace + adds fees/refunds)

All Squarespace checkouts run through Stripe. Derived rollups: [`stripe-monthly-summary.csv`](../../data/revenue/stripe-monthly-summary.csv) · [`stripe-yearly-summary.csv`](../../data/revenue/stripe-yearly-summary.csv)

| Metric | Value |
|--------|-------|
| Paid charges (all-time) | 9,355 · **$1,006,544** gross |
| Matches Squarespace paid totals | **99.9%** by order ID (4 tiny mismatches / 7 edge-case orders) |
| 2026 YTD gross (through Jul 25) | **$90,094** on 680 charges (vs SS $89,835 on 678 orders — **+$259**) |
| 2026 processing fees | **$2,862** (**3.18%** of gross) |
| 2026 net after Stripe fees | **~$87,231** |
| Refunded charges (all-time) | 145 · **$14,521** |
| Failed payment attempts (all-time) | 317 · **$32,387** would-have (mostly CVC/decline) |

**2026 monthly (Stripe gross vs Squarespace total):**

| Month | SS total | Stripe gross | Diff |
|-------|----------|--------------|------|
| 2026-01 | $9,901 | $9,813 | −$88 |
| 2026-02 | $22,116 | $22,204 | +$88 |
| 2026-03 | $12,133 | $12,023 | −$110 |
| 2026-04 | $10,152 | $10,262 | +$110 |
| 2026-05 | $22,521 | $22,521 | $0 |
| 2026-06 | $5,754 | $5,754 | $0 |
| 2026-07 | $7,258 | $7,517 | +$259 |

Differences are timing/cutoff noise (Jul 25 Stripe vs Jul 24 SS) plus a handful of legacy orders. **Use Squarespace for product/shipping detail; use Stripe for fees, refunds, and failed-checkout diagnostics.**

### Stripe customers (identity file)

| Metric | Value |
|--------|-------|
| Customers | 4,202 (all with email) |
| Lifetime spend on file | $720,801 |
| Median spend/payment | $102.60 |

Customer lifetime spend ($721k) is lower than Squarespace/Stripe charge gross ($1.005M / $1.007M) because many checkouts don’t create a Stripe Customer object. **Prefer Squarespace order emails for CRM.**

---

## 2. Channel & product mix

### Channel split 2026 YTD

```
Square net sales     ████████████████████░░░░  ~55–60%  (in-store / invoice)
Squarespace subtotal ███████████████░░░░░░░░░  ~40–45%  (online)
```

Online is not a side channel — it’s nearly half of measurable product revenue.

### Squarespace heroes (clean SKUs)

**2026 line revenue leaders:**

| Product | Qty | Line revenue |
|---------|-----|--------------|
| To the Moon and Back | 128 | $12,160 |
| Love Poem | 135 | $11,475 |
| Touch of Honey | 153 | $9,945 |
| TLC | 65 | $9,100 |
| XoXo | 68 | $7,480 |
| The Sympathy | 51 | $5,618 |
| Darling | 29 | $5,220 |
| Deep in the Woods | 37 | $4,440 |

Top **5 = 68.5%** of 2026 online product revenue; top **8 = 89%**. Catalog is a tight hero set — protect and upsell these, don’t expand endlessly.

**All-time online heroes** are the same names (Moon, Love Poem, Touch of Honey, XoXo, TLC, Woods, Darling, Sympathy) plus **Monthly Flower Subscription** ($37.5k lifetime / 78 orders) and orchids/succulents.

**Card add-on:** “The Finishing Touch - Add a card!” — **4 orders in 2026 (0.6% attach)**. This is free money left on the table vs the 25% target.

**Subscriptions 2026:** 4 orders (~$2.7k) — tiny vs capacity.  
**Sympathy 2026 (named):** 50 orders / ~$6.9k online (material).  
**Wedding-tagged online:** ~0 (weddings likely offline / invoice / untagged).  
**Duplicate SKU proof:** `Touch of Honey (Copy)` sold once for $65 — delete it.

### Square POS product signals (messy naming)

Price-named SKUs (`20`, `45 bouquet`, `Item`) dominate. Everyday arrangements ~70% of equal-split heuristic; wedding/sympathy under-tagged. POS naming prevents recipe costing and hides the online hero ladder from counter staff.

---

## 3. Customer & retention health

### Squarespace (best online CRM)

| Metric | Value |
|--------|-------|
| Unique payer emails (all-time) | **5,986** |
| Repeat email rate (2+ orders) | **20.9%** |
| Revenue from repeat emails | **$517k** (~51% of all-time paid totals) |
| 2026 orders from pre-2026 emails | **43%** |
| 2026 new-email orders | **57%** |

Online retention is healthier than raw “21% repeat” suggests — nearly half of 2026 orders are from known emails, and repeat buyers drive half of lifetime online revenue.

### Square customers

| Metric | Value |
|--------|-------|
| Profiles | 17,526 · **$2.28M** lifetime |
| Repeat (2+ txs ever) | **31%** |
| With email | **7.5%** |
| Email subscribed | **2** |
| 2026 txs with customer ID | **55%** · ~**40% of YTD $ anonymous** |

### Identity universe

- Squarespace emails: ~5,986  
- Stripe customers: 4,202  
- Square emails: 1,316  
- Prior Square∩Stripe overlap: 129  

**Actionable list ≈ Squarespace order emails first** (richest, purchase-verified), then merge Square.

---

## 4. Baseline vs. plan targets

| Metric | Prior estimate | **Measured now** | 90-day target |
|--------|----------------|------------------|---------------|
| Everyday AOV | ~$80–90 | Square med **$49** / mean $66; **SS med total $121 / subtotal $95** | $95+ blend; **POS median → $75+** |
| Repeat rate | Unknown | Square **31%**; SS email **21%** (but 43% of 2026 SS orders from known emails) | 35%+ |
| Online mix | Unknown | **~40–45%** of measurable product $ | Track monthly |
| Card attach | ~0% | **0.6% online**; unknown in-store | **25%+** |
| Active subscriptions | Unknown | **~4 SS sub orders in 2026**; 78 lifetime | +10% |
| Gross margin | Unknown | Still unknown (no COGS) | 60%+ |
| Combined YTD | Unknown | **~$185k** product-ish / **~$201k** cash-ish | — |

**Diagnosis:** Online AOV and hero assortment are working. The gap is **in-store AOV + identity capture + add-on attach + subscription reactivation**. Post-2021 online order-count decline is the acquisition risk; 2026 YTD recovery is encouraging — protect it with CRO (popup removal, duplicate SKU cleanup) already in Week 1.

---

## 5. Prioritized growth levers (numeric)

### Lever A — Raise POS AOV toward the online ladder (P1)

**Why:** Same shop, same flowers: online median subtotal **$95** vs counter median **$49**.

**Moves:**

1. Put the **online hero ladder** on the counter (Touch of Honey / Love Poem / Moon / TLC / XoXo) with prices matching the site.
2. Kill price-named POS SKUs (`20`, `45 bouquet`) or map them to named designs.
3. Target: POS median **$75** within 90 days.

**Math:** Lifting half of ~1,000 sub-$60 Square tickets by $20 ≈ **+$10k** on similar YTD traffic.

### Lever B — Default the $6.50 card (and other add-ons) (P1)

**Why:** 0.6% online attach on an existing SKU. At 25% of 678 YTD online orders → ~170 cards × $6.50 ≈ **$1.1k YTD** just online; annualize and add POS for **$3–5k+/year** with almost no creative work.

**Moves:** Checkout checkbox default-on (or stronger UX); POS verbal prompt every wrapped order.

### Lever C — Capture Square identity + holiday → everyday bridge (P2)

**Why:** 40% of Square $ is anonymous; Feb+May dominate both channels.

**Moves:**

1. Require email or phone on Square payments.  
2. Merge SS + Square emails; post-holiday occasion follow-up.  
3. Offer **Monthly Flower Subscription** to multi-buyers and holiday buyers (only 4 sub orders YTD).

**Target:** ≥85% Square txs with contact; 10% of identifiable holiday buyers repurchase in 90 days; **+10 subscription orders** in 90 days.

---

## 6. Margin notes

- Still no COGS file.
- **Online processing fees:** ~3.2% of gross in 2026 ($2.9k YTD) — normal; not a strategic leak.
- **Square POS fees:** ~3.0% of collected — similar.
- Online shipping collected YTD: **$8,836** — compare to actual delivery labor/fuel.
- Hero concentration helps costing: recost the top 8 online SKUs first.  
- Delete `Touch of Honey (Copy)` (already sold once).  
- Sympathy is a real online line (~$7k YTD) — don’t underprice it.

---

## 7. 90-day action plan (updated)

| Window | Focus | Success metric |
|--------|-------|----------------|
| **Days 1–30** | POS price ladder = online heroes; delete duplicate SKUs; require Square email/phone; card UX online | POS median ↑; card attach ≥10% online |
| **Days 31–60** | Merge email lists; win-back to SS multi-buyers + 2026 holiday buyers; subscription offer | Card attach ≥20%; +5 new subs |
| **Days 61–90** | Occasion reminders; East Bay delivery packaging; scorecard both channels monthly | POS median ≥$70; scorecard complete |

---

## 8. Data gaps still open

| Gap | Status | Ask |
|-----|--------|-----|
| Squarespace orders | ✅ Ingested (2015–2026) | — |
| Stripe payments | ✅ Ingested (2015–2026) — confirms SS | — |
| Online monthly revenue | ✅ From Squarespace + Stripe | — |
| Subscriptions | Partial (78 lifetime SS orders) | Active subscriber count / churn |
| Weddings | Still missing | Invoices / contracts |
| COGS | ☐ | Wholesale monthly |
| Wire / FTD | ☐ | Statements if used |
| Square delivery vs pickup | ☐ | Still blank in Square export |

---

## Appendix — File checklist

| Provided | Status |
|----------|--------|
| Square transactions 2026 YTD | ✅ |
| Square customers | ✅ |
| Stripe customers | ✅ |
| Squarespace orders May 2015–Jul 2026 | ✅ |
| Stripe payments May 2015–Jul 2026 | ✅ |
| Stripe customers | ✅ |
| Duplicate Square transactions export | ✅ Deduped |
