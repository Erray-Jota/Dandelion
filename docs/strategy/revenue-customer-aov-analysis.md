# Revenue, Customer & AOV Analysis — Week 4 Deliverable

**Prepared:** July 26, 2026  
**Data:** Square POS (2026 YTD) · Squarespace orders (2015–2026) · Stripe payments · Bank/accounts COGS ([`forensic-classification-review.csv`](../forensic-classification-review.csv))  
**Companion:** [Revenue Baseline 2026 YTD](revenue-baseline-2026-ytd.md) · [Monthly Scorecard 2026](monthly-scorecard-2026.csv)

---

## Executive summary

Dandelion is a **two-channel shop** doing ~**$185k** in measurable product revenue YTD (Jan–Jul 2026), split roughly **60% in-store / 40% online**. Online is recovering (+41% YTD vs 2025) with healthy AOV; the counter is not.

The accounts data reveals a **margin problem**: gross profit ran **26–38%** over 2023–2025 (2026 YTD: **31.5%**) — well below the plan’s **60%+** target. Flowers/wholesale spend tracks revenue tightly; soft months (Apr, Jun) drop into **single-digit GP%** when stem buys don’t flex with volume.

**Top 3 priorities from the data:**

1. **Raise in-store AOV** from median **$49** toward online’s **$95** product median — same designs, different ticket.
2. **Protect gross margin in slow months** — stem spend is not scaling down when order volume drops 40–50%.
3. **Convert the online buyer base** — 5,986 payer emails, only 21% repeat lifetime, but 43% of 2026 orders already from known emails; subscriptions barely active (4 orders YTD).

---

## 1. Revenue analysis

### 1.1 Total revenue & channel mix (2026 YTD)

| Source | Amount | Orders | Notes |
|--------|--------|--------|-------|
| Square POS + invoices (net sales) | **$111,578** | 1,680 | Jan 6–Jul 25 |
| Squarespace (paid total) | **$89,835** | 678 | Through Jul 24 |
| Squarespace (product subtotal) | **$73,212** | 678 | Ex tax + shipping |
| **Combined product-ish** | **~$185k** | 2,358 | Square net + SS subtotal |
| Bank deposits (accounts) | **$184,160** | — | Square $93k + Stripe $86k + other |

Bank revenue and export totals reconcile within **~1%** — the books and POS/commerce exports tell the same story.

### 1.2 Monthly revenue & seasonality

| Month | Square net | SS total | Combined subtotal-ish | Bank revenue | GP% |
|-------|------------|----------|----------------------|--------------|-----|
| Jan | $15,436 | $9,901 | $23,399 | $19,631 | **16%** |
| Feb | $23,844 | $22,116 | $42,157 | $44,644 | **43%** |
| Mar | $13,224 | $12,133 | $23,087 | $25,032 | **25%** |
| Apr | $12,974 | $10,152 | $21,060 | $19,910 | **9%** |
| May | $27,529 | $22,521 | $46,025 | $45,339 | **48%** |
| Jun | $9,292 | $5,754 | $13,891 | $14,582 | **11%** |
| Jul (partial) | $9,280 | $7,258 | $15,170 | $15,022 | **29%** |

**Pattern:** Valentine’s (Feb) and Mother’s Day (May) drive **~46%** of YTD revenue and the **best margins**. April and June are double hits — low volume **and** thin GP%.

### 1.3 Annual trend (online + books)

| Year | SS paid total | Bank total revenue | Gross margin % |
|------|---------------|-------------------|----------------|
| 2023 | $110,123 | $333,737 | 38.1% |
| 2024 | $107,984 | $282,530 | 34.3% |
| 2025 | $106,459 | $276,591 | **25.8%** |
| 2026 YTD | $89,835 | $184,160 | **31.5%** |

Online order count never recovered from the 2021 peak (1,525 orders → ~830/year), but **AOV climbed** ($98 → $133). Revenue stability has come from charging more per order, not more orders.

2026 online YTD is **+41% vs 2025** same window — a real recovery worth protecting with CRO fixes (popup, duplicates) already in the Week 1 plan.

### 1.4 COGS / gross margin (from accounts)

**Cost of sales categories:** Flowers (wholesale) · Tax · Materials · Merchandise

| Year | Revenue | COS | Gross profit | GP% |
|------|---------|-----|--------------|-----|
| 2023 | $333,737 | $206,549 | $127,188 | 38.1% |
| 2024 | $282,530 | $185,572 | $96,958 | 34.3% |
| 2025 | $276,591 | $205,248 | $71,343 | **25.8%** |
| 2026 YTD | $184,160 | $126,112 | $58,047 | **31.5%** |

**2026 COS breakdown (YTD):**

| Category | Amount | % of COS |
|----------|--------|----------|
| Flowers (wholesale) | $116,419 | 92% |
| Tax | $4,888 | 4% |
| Merchandise | $4,631 | 4% |
| Materials | $174 | <1% |

**Diagnosis:** Margin is overwhelmingly a **stem-buy vs revenue** problem. Merchandise/materials are minor. The 60%+ GP target requires either (a) meaningfully higher prices/AOV without proportional stem increases, or (b) tighter wholesale purchasing aligned to weekly order volume — especially in slow months.

**Margin alert months:** Jan (16%), Apr (9%), Jun (11%) — stem spend stays high while revenue drops.

---

## 2. AOV analysis

### 2.1 Channel AOV comparison (2026 YTD)

| Segment | Orders | Mean | Median | P75 |
|---------|--------|------|--------|-----|
| **Square POS** | 1,633 | $64 | **$49** | $87 |
| Square invoices | 47 | $165 | $95 | $159 |
| **Squarespace total** | 678 | $133 | **$121** | $142 |
| Squarespace subtotal (product) | 678 | $108 | **$95** | $111 |
| SS delivery | 539 | $139 | $121 | $149 |
| SS pickup | 139 | $108 | $94 | $122 |

**The gap:** In-store median is **half** of online product median. Customers buy the same hero designs online at $95–140; at the counter they buy “20” and “45 bouquet” SKUs at $40–60.

### 2.2 AOV distribution (Square POS)

| Bucket | % of POS tickets |
|--------|------------------|
| Under $40 | **40%** |
| $40–60 | 18% |
| $60–80 | 13% |
| $80–100 | 10% |
| $100–150 | 12% |
| $150+ | 7% |

**Target path to $75 median:** Shift half of sub-$60 tickets up one tier (+$20–30). On ~1,000 tickets over a similar YTD window → **~$10–15k** additional revenue before holiday peaks.

### 2.3 Product-level AOV (online heroes, 2026)

| Product | Qty | Revenue | Avg price |
|---------|-----|---------|-----------|
| To the Moon and Back | 128 | $12,160 | $95 |
| Love Poem | 135 | $11,475 | $85 |
| Touch of Honey | 153 | $9,945 | **$65** |
| TLC | 65 | $9,100 | $140 |
| XoXo | 68 | $7,480 | $110 |
| The Sympathy | 51 | $5,618 | $110 |
| Darling | 29 | $5,220 | **$180** |
| Great Expectations | 29 | $2,791 | **$310** |
| Monthly Flower Subscription | 4 | $2,340 | **$585** |

**Ladder is working online** when customers see named designs. Touch of Honey underperforms on price ($65 avg) — likely the entry tier. Darling and Great Expectations prove willingness to pay $180–310.

**Card add-on:** 4 orders (0.6% attach) on a $6.50 SKU → **~$1.1k/year left on the table** at 25% attach on current online volume alone.

### 2.4 AOV trend (online, all-time)

| Year | SS AOV (total) | SS AOV (subtotal) |
|------|----------------|-------------------|
| 2019 | $99 | $80 |
| 2021 (peak volume) | $98 | $79 |
| 2024 | $127 | $113 |
| 2025 | $128 | $114 |
| **2026 YTD** | **$133** | **$108** |

AOV strategy is working. Volume strategy is not — order count still ~45% below 2021.

---

## 3. Customer analysis

### 3.1 Online customers (Squarespace — best CRM)

| Metric | Value |
|--------|-------|
| Unique payer emails (all-time) | **5,986** |
| Repeat buyers (2+ orders ever) | **1,253 (20.9%)** |
| 2026 orders from returning emails | **291 (42.9%)** |
| 2026 orders from new emails | **387 (57.1%)** |
| Revenue from repeat-email buyers (lifetime) | **$517k (51% of all SS revenue)** |

Repeat rate looks low (21%) but **half of all lifetime online revenue** comes from repeat buyers. The 2026 mix (43% returning) is healthier than the lifetime average — holiday peaks are bringing back known customers.

### 3.2 Customer value tiers (online, lifetime spend)

| Tier | Customers | % of base | Revenue share |
|------|-----------|-----------|---------------|
| VIP ($1,000+) | 85 | 1.4% | **14.6%** |
| Regular ($300–999) | 477 | 8.0% | ~25% |
| Occasional ($100–299) | 2,745 | 45.9% | ~35% |
| Light (<$100) | 2,679 | 44.8% | ~25% |

**Concentration:** Top 10% of customers (598) = **39% of lifetime online revenue**.

**Biggest pool:** 2,745 occasional buyers ($100–299) — prime win-back / occasion-reminder targets.

### 3.3 In-store customers (Square)

| Metric | Value |
|--------|-------|
| Profiles with spend | 17,411 |
| Repeat (2+ transactions ever) | **5,417 (31.1%)** |
| With email on file | **1,294 (7.4%)** |
| Email subscribed | **2** |
| Active in 2026 (last visit) | 686 |
| 2026 transactions with customer ID | 55% |
| Anonymous 2026 sales | **~40% of $** |

Square has more repeat behavior (31%) but almost **no marketing reach** — email capture is the bottleneck.

### 3.4 Cross-channel identity

| List | Size |
|------|------|
| Squarespace payer emails | 5,986 |
| Stripe customer emails | 4,202 |
| Square emails | 1,294 |
| **Overlap SS ∩ Square** | **167** |

Channels are siloed. The actionable list is **Squarespace emails first** (purchase-verified, richest history).

### 3.5 High-value segments

| Segment | 2026 orders | 2026 revenue | AOV | Notes |
|---------|-------------|--------------|-----|-------|
| Sympathy (named) | 50 | $6,941 | $139 | Material online line |
| Subscriptions | 4 | $2,656 | $664 | 54 lifetime sub-buyer emails; huge gap |
| In-store invoices | 47 | $7,754 | $165 | Custom / larger work |
| Corporate (Square company field) | — | — | — | Only 6 profiles tagged |

### 3.6 Retention health vs plan targets

| Metric | Measured | 90-day target | Gap |
|--------|----------|---------------|-----|
| Repeat rate (online email) | 21% lifetime / 43% of 2026 orders | 35%+ | Win-back + occasion capture |
| Repeat rate (Square) | 31% lifetime | 35%+ | Close if identity captured |
| Active subscriptions | 4 orders YTD | +10% growth | Reactivate 54 past sub-buyers |
| Email capture (Square) | 7.4% | ≥85% of txs | Staff process change |

---

## 4. Synthesis — what the plan should prioritize

### Revenue lever ranking (data-backed)

| Rank | Lever | Evidence | Est. impact |
|------|-------|----------|-------------|
| **1** | Raise POS AOV to online ladder | Median $49 vs $95; 40% of tickets under $40 | **+$10–15k** per similar YTD window |
| **2** | Align stem buys to weekly volume | Apr/Jun GP% 9–11% vs Feb/May 43–48% | **+$8–15k** GP if COS flexes 5–10 pts in slow months |
| **3** | Default card add-on + upsell | 0.6% attach online | **+$3–5k/yr** low effort |
| **4** | Win-back occasional buyers (2,745 emails) | 43% of 2026 orders already returning | **+$25–35k/yr** at 8% reorder rate |
| **5** | Reactivate subscriptions | 54 past buyers, 4 orders YTD | **+$5–15k ARR** |
| **6** | Capture Square email/phone | 40% anonymous sales | Unlocks all retention plays |

### Channel investment split

```
In-store:  Fix AOV + identity capture (not more traffic)
Online:    Protect 2026 recovery; CRO + card attach + hero focus
Margin:    Weekly stem-buy discipline; recost top 8 SKUs
Retention: SS email list → occasion reminders → sub offer
```

### Products to recost first (online revenue concentration)

1. To the Moon and Back  
2. Love Poem  
3. Touch of Honey  
4. TLC  
5. XoXo  
6. The Sympathy  
7. Darling  
8. Deep in the Woods  

These 8 = **~89%** of 2026 online product revenue. Recipe-level COGS on these alone would clarify whether the 60% GP target is realistic per SKU.

---

## 5. Updated targets (measured baselines)

| Metric | Was (estimate) | **Now measured** | 90-day target |
|--------|----------------|------------------|---------------|
| Combined YTD revenue | Unknown | **~$185k** product / **$184k** bank | Track monthly |
| Everyday AOV | ~$80–90 | POS med **$49** / SS med **$95** | **$75+ POS median** |
| Gross margin % | Unknown | **31.5%** YTD (25.8% in 2025) | **38%+** near-term; 60% requires repricing |
| Repeat rate | Unknown | SS 21% / Square 31% | **35%+** |
| Online mix | Unknown | **~40%** of product $ | Maintain + grow |
| Card attach | ~0% | **0.6%** | **25%** |
| Active subs | Unknown | **4 orders YTD** | **+10 orders** in 90 days |

---

## 6. 90-day action plan (Weeks 2–4 from master plan)

| Week | Focus | Actions | Success metric |
|------|-------|---------|----------------|
| **2** | AOV | POS hero ladder = online names/prices; delete price-named SKUs; card default-on online | POS median → $60+ |
| **3** | Retention | Merge SS emails; post-holiday win-back to occasional tier; sub offer to 54 past buyers | 1 campaign sent; +5 subs |
| **4** | Margin | Recost top 8 SKUs; weekly stem-buy vs order forecast; flag SKUs below 38% GP | Recost sheet done; Apr/Jun GP% improved |

---

## 7. Data notes & remaining gaps

- **COGS:** From bank/CC forensic classification ([`forensic-classification-review.csv`](../forensic-classification-review.csv)). Flowers = Mayesh, Torchio, Rafa's, checks, etc. Delivery/labor not separately classified in COS — may be understating true COGS.
- **Revenue:** Bank deposits lag POS/export slightly; monthly alignment is directionally correct.
- **Per-SKU margin:** Not yet available — needs recipe costs for top 8 heroes.
- **Weddings:** Still not tagged in commerce data; invoice channel ($7.8k YTD) likely includes some.
- **Active subscription count:** Need manual count of current recurring deliveries.

---

## Appendix — file references

| File | Use |
|------|-----|
| [`data/revenue/square-transactions-2026-ytd.csv`](../../data/revenue/square-transactions-2026-ytd.csv) | In-store revenue + AOV |
| [`data/revenue/squarespace-orders-2015-2026.csv`](../../data/revenue/squarespace-orders-2015-2026.csv) | Online revenue + customers + products |
| [`data/revenue/stripe-payments-all.csv`](../../data/revenue/stripe-payments-all.csv) | Fee/refund confirmation |
| [`docs/forensic-classification-review.csv`](../forensic-classification-review.csv) | COGS + bank revenue |
| [`docs/strategy/monthly-scorecard-2026.csv`](monthly-scorecard-2026.csv) | Updated with GP% |
