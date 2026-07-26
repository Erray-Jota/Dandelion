# Dandelion Flowers — Consolidated Business Analysis

**Prepared:** July 26, 2026 (Week 4 deliverable)  
**Scope:** Bank/accounts P&L · Commerce exports (Square, Squarespace, Stripe) · Industry benchmarks  
**Replaces:** [Week 4 P&L Analysis](week-4-pl-analysis.md) · [Revenue Analysis vs Benchmarks](strategy/revenue-analysis-benchmarks.md) · [Revenue, Customer & AOV Analysis](strategy/revenue-customer-aov-analysis.md)  
**Companion docs:** [Revenue Baseline 2026 YTD](strategy/revenue-baseline-2026-ytd.md) · [Product Margin Analysis](strategy/product-margin-analysis.md) · [Industry Benchmarks](strategy/industry-benchmarks.md)

---

## Executive summary

Dandelion is a **~$316K independent florist** (2026 annualized pace) in the healthy $300K–$500K revenue band — a **two-channel shop** split roughly **60% in-store / 40% online**. The business is **not revenue-starved; it is margin- and mix-starved.**

| Verdict | Metric | Actual | Alameda target | Gap |
|---------|--------|--------|----------------|-----|
| ✅ **Winning** | Online AOV | $95–$133 | $85–$115 | At or above |
| ✅ **Winning** | Online channel share | 49% | 42–48% | At target |
| ✅ **Winning** | 2026 online growth | +41% YTD vs 2025 | Protect recovery | Ahead |
| ✅ **Winning** | Net ops margin | 12–16% (2023–25) | 10–14% | Above target |
| ⚠️ **Mixed** | Repeat rate | 21–31% | 40%+ | Below strong performer |
| ❌ **Losing** | POS median AOV | **$49** | $85–$115 | **−$36 to −$66** |
| ❌ **Losing** | Gross margin | **31.5%** | 62–68% | **−31 pts** |
| ❌ **Losing** | Wholesale spend / revenue | **63%** | 28–35% | **~2× benchmark** |
| ❌ **Losing** | Card attach | **0.6%** | 30%+ | Near zero |
| ❌ **Losing** | Email capture (Square) | **7.4%** | 85%+ txs | Critical |

**Market context:** Alameda median household income is **$137,697** (+39% vs California). Customers can afford premium floral. Online pricing proves it; the counter does not.

### Two focus metrics for the next 8 weeks

1. **POS median AOV:** $49 → **$75** by end of Q3  
2. **Shop gross margin %:** 31.5% → **38%** by end of Q3  

Everything else (SEO, weddings, corporate) is secondary until these move.

### Top 3 priorities from the data

1. **Raise in-store AOV** from median **$49** toward online's **$95** product median — same designs, different ticket.
2. **Protect gross margin in slow months** — stem spend does not flex when order volume drops 40–50% (Apr/Jun hit single-digit GP%).
3. **Convert the online buyer base** — 5,986 payer emails, only 21% repeat lifetime, but 43% of 2026 orders already from known emails; subscriptions barely active (4 orders YTD).

---

## 1. Financial health — P&L & profitability

*Sources: Bank of Marin, Capital One, `2024.xlsx`, `2025 v3.xlsx` · Rebuild: `python3 scripts/build_forensic_pl.py`*

### 1.1 Annual P&L (original classification)

| Year | Revenue | Gross profit | GP % | Net ops | Net ops % | Total net | Total NP % |
|------|---------|-------------|------|---------|-----------|-----------|------------|
| **2023** | $333,737 | $115,032 | 34.5% | $61,715 | **18.5%** | $53,032 | **15.9%** |
| **2024** | $282,530 | $116,579 | 41.3% | $34,619 | **12.3%** | ($23,134) | **-8.2%** |
| **2025** | $299,115 | $114,045 | 38.1% | $46,609 | **15.6%** | ($1,845) | **-0.6%** |
| **2026 YTD** | $184,160 | $53,680 | 29.1% | $20,794 | **11.3%** | $2,054 | **1.1%** |

**Key insight:** Ops profit is healthy (net ops **12–19%** vs 10–14% target) — overhead is lean at **22.5%** of revenue. The margin problem is **COGS**, not overhead.

### 1.2 Product margin (excludes sales tax from COGS)

Industry benchmarks measure flowers + materials + merchandise only — not CDTFA remittances.

| Year | Product COGS | % of rev | Adjusted GP % | vs. 62–68% target |
|------|-------------|----------|---------------|-------------------|
| 2023 | $199,962 | 59.9% | **40.1%** | −22 to −28 pts |
| 2024 | $158,992 | 56.3% | **43.7%** | −18 to −24 pts |
| 2025 | $179,275 | 59.9% | **40.1%** | −22 to −28 pts |
| 2026 YTD | $126,112 | 68.5% | **31.5%** | −31 to −37 pts |

### 1.3 Reclassified view (2025 stress test)

Forensic reclassification removes $22.5K transfers miscoded as income and reassigns personal/non-flower items. See [forensic-classification-review.xlsx](forensic-classification-review.xlsx).

| Metric | Original | Reclassified |
|--------|----------|--------------|
| Revenue | $299,115 | $276,591 |
| GP % | 38.1% | **25.8%** |
| Net ops % | 15.6% | **5.6%** |

Use original for day-to-day ops; use reclassified to stress-test worst-case margin.

### 1.4 Store expense breakdown (2025)

| Category | Amount | % rev | Benchmark |
|----------|--------|-------|-----------|
| Venmo (labor proxy) | $20,330 | 6.8% | Payroll 28–35% |
| Food | $6,380 | 2.1% | Review personal mix |
| SBA / Admin | $7,561 | 2.5% | OK |
| Utilities + insurance + car | $12,191 | 4.1% | OK |
| **Total store** | **$67,436** | **22.5%** | Lean |

Owner labor is under-reported (Venmo at 6.8% vs 28–35% payroll benchmark). True fully-loaded accounting would reduce net ops.

### 1.5 Quarterly P&L trend (2025)

| Quarter | Revenue | GP % | Net ops % |
|---------|---------|------|-----------|
| Q1 | $78,380 | 43.2% | 15.9% |
| Q2 | $81,303 | 35.4% | 12.2% |
| Q3 | $67,628 | 36.3% | 17.2% |
| Q4 | $71,804 | 37.4% | 17.6% |

Trailing 12 months (Aug 2025 – Jul 2026): Revenue $299K · GP **30.9%** · Net ops **12.4%** — gross margin compressing vs prior years.

---

## 2. Revenue & channel performance

*Sources: Square POS (2026 YTD) · Squarespace orders (2015–2026) · Stripe payments · Bank deposits*

### 2.1 2026 YTD channel mix

| Source | Amount | Orders | Share | Notes |
|--------|--------|--------|-------|-------|
| Square POS + invoices (net sales) | **$111,578** | 1,680 | 60% product $ | Jan 6–Jul 25 |
| Squarespace (paid total) | **$89,835** | 678 | 40% product $ | Through Jul 24 |
| Squarespace (product subtotal) | **$73,212** | 678 | — | Ex tax + shipping |
| **Combined product-ish** | **~$185k** | 2,358 | — | Square net + SS subtotal |
| Bank deposits (accounts) | **$184,160** | — | 49% online | Square $93k + Stripe $86k + other |

Bank revenue and export totals reconcile within **~1%** — the books and POS/commerce exports tell the same story.

### 2.2 Annual revenue trend

| Year | Bank revenue | SS online | Online % | GP% | Shop-size context |
|------|-------------|-----------|----------|-----|-------------------|
| 2023 | $333,737 | $110,123 | 33% | 38.1% | Above $300K — healthy band |
| 2024 | $282,530 | $107,984 | 38% | 34.3% | Declining; margin slipping |
| 2025 | $276,591 | $106,459 | 38% | **25.8%** | Below $300K; margin crisis |
| **2026 YTD** (7 mo) | $184,160 | $89,835 | **49%** | **31.5%** | Recovering |
| **2026 annualized** | **~$316K** | **~$154K** | ~49% | ~31.5% | Back in $300K–$500K band |

2025 slipped into the "fix margin before growth" zone ($277K, 26% GP). 2026 volume recovery is real but **margin must recover with it** or the extra revenue is mostly stem cost.

### 2.3 Online recovery

Online order count never recovered from the 2021 peak (1,525 orders → ~830/year), but **AOV climbed** ($98 → $133). Revenue stability has come from charging more per order, not more orders.

2026 online YTD is **+41% vs 2025** same window — a real recovery worth protecting with CRO fixes (popup, duplicates) already in the Week 1 plan.

### 2.4 Payment channel mix (2025 bank P&L)

| Channel | Amount | % of revenue |
|---------|--------|-------------|
| Square | $161,980 | 54.2% |
| Stripe | $102,823 | 34.4% |
| Deposits + other | $34,312 | 11.5% |

Stripe ≈ Squarespace online. The ~$56K gap between Square bank deposits ($162K) and Squarespace total ($106K) is in-store POS + invoices.

---

## 3. Gross margin deep dive

*Source: Bank/CC forensic classification ([`forensic-classification-review.csv`](forensic-classification-review.csv))*

### 3.1 Margin scorecard vs benchmarks

| Metric | Dandelion | National healthy | Alameda target | Status |
|--------|-----------|------------------|----------------|--------|
| Gross margin % (2026 YTD) | **31.5%** | 65–72% (fresh arrangements) | **62–68%** | ❌ Critical |
| Gross margin % (2025) | **25.8%** | 45–58% (many independents) | 62–68% | ❌ Deteriorating |
| Wholesale/flowers as % of revenue | **63.2%** | **28–35%** | Under 40% | ❌ ~2× benchmark |
| COGS as % of retail (per arrangement) | ~69% implied | 20–33% max | — | ❌ Double the SAF ceiling |

### 3.2 Margin trend — the core financial story

| Year | Revenue | GP% | Wholesale % of rev | What happened |
|------|---------|-----|-------------------|---------------|
| 2023 | $334K | 38.1% | 54% | Highest revenue + best margin in period |
| 2024 | $283K | 34.3% | 59% | Revenue −15%; margin slipping |
| 2025 | $277K | **25.8%** | **68%** | Revenue flat; **stem spend up, prices flat** |
| 2026 YTD | $184K (7 mo) | 31.5% | 63% | Volume recovering; margin still broken |

**2025 was the warning year:** revenue barely moved but wholesale spend rose to **68% of revenue**. That is incompatible with a 62–68% gross margin target (which implies ~32–38% COGS, not 68%).

### 3.3 2026 COGS breakdown (YTD)

| Category | Amount | % of COS |
|----------|--------|----------|
| Flowers (wholesale) | $116,419 | 92% |
| Tax | $4,888 | 4% |
| Merchandise | $4,631 | 4% |
| Materials | $174 | <1% |

Margin is overwhelmingly a **stem-buy vs revenue** problem. Merchandise/materials are minor.

### 3.4 Monthly revenue & margin (2026)

| Month | Square net | SS total | Combined | Bank revenue | GP% | Benchmark read |
|-------|------------|----------|----------|--------------|-----|----------------|
| Jan | $15,436 | $9,901 | $23,399 | $19,631 | **16%** | Post-holiday trough |
| Feb | $23,844 | $22,116 | $42,157 | $44,644 | **43%** | Valentine's peak |
| Mar | $13,224 | $12,133 | $23,087 | $25,032 | **25%** | — |
| Apr | $12,974 | $10,152 | $21,060 | $19,910 | **9%** | ❌ Revenue down; stems not cut |
| May | $27,529 | $22,521 | $46,025 | $45,339 | **48%** | Mother's Day peak |
| Jun | $9,292 | $5,754 | $13,891 | $14,582 | **11%** | ❌ Same pattern |
| Jul (partial) | $9,280 | $7,258 | $15,170 | $15,022 | **29%** | Summer slow |

**Pattern:** Valentine's (Feb) and Mother's Day (May) drive **~46%** of YTD revenue and the **best margins**. April and June are double hits — low volume **and** thin GP%.

**Dandelion's unique failure mode:** Apr/Jun revenue drops AND wholesale spend doesn't → single-digit GP%.

### 3.5 Path from 31.5% → 38% (90-day) vs 62% (12-month)

| Lever | GP impact (est.) | Feasibility |
|-------|------------------|-------------|
| Raise Touch of Honey +$15 | +2–3 pts on hero mix | High — online already supports |
| Weekly stem-buy budget tied to forecast | +3–5 pts in slow months | Medium — operational discipline |
| POS AOV +$20 median (fewer sub-$40 tickets) | +4–6 pts blended | High — same stems, more revenue |
| Card attach 25% | +0.5 pt | High — nearly free |
| **Combined near-term** | **→ ~38–42%** | Realistic in 90 days |
| Full repricing to 62% GM | +30 pts | Requires **~2× markup** or halving stem cost — structural reset |

---

## 4. AOV analysis

### 4.1 Channel AOV scorecard (2026 YTD)

| Segment | Orders | Mean | Median | P75 | Alameda target | Status |
|---------|--------|------|--------|-----|----------------|--------|
| **Square POS** | 1,633 | $64 | **$49** | $87 | $85–$115 | ❌ |
| Square invoices | 47 | $165 | $95 | $159 | Track separately | ⚠️ |
| **Squarespace total** | 678 | $133 | **$121** | $142 | $85–$115 | ✅ |
| Squarespace subtotal (product) | 678 | $108 | **$95** | $111 | $85–$115 | ✅ |
| SS delivery | 539 | $139 | $121 | $149 | — | Premium |
| SS pickup | 139 | $108 | $94 | $122 | — | Above POS |
| **Blended all channels** | 2,358 | — | **$78** | — | $85–$115 | ❌ |

**The gap:** In-store median is **half** of online product median. Customers buy the same hero designs online at $95–140; at the counter they buy "20" and "45 bouquet" SKUs at $40–60.

### 4.2 Dollar impact

Alameda target blended AOV ≈ **$95**. Actual blended ≈ **$78**. On ~2,358 orders YTD:

```
($95 − $78) × 2,358 orders ≈ $40,000 left on table (annualized ~$69K)
```

**40% of POS tickets are under $40** — in a market where median household income is $137K and online customers happily pay $95–$133.

### 4.3 POS AOV distribution

| Bucket | % of POS tickets |
|--------|------------------|
| Under $40 | **40%** |
| $40–60 | 18% |
| $60–80 | 13% |
| $80–100 | 10% |
| $100–150 | 12% |
| $150+ | 7% |

**Target path to $75 median:** Shift half of sub-$60 tickets up one tier (+$20–30). On ~1,000 tickets over a similar YTD window → **~$10–15k** additional revenue before holiday peaks.

### 4.4 Price ladder vs market positioning

| Tier | Online (working) | POS (broken) |
|------|------------------|--------------|
| Entry | Touch of Honey ~$65–68 | "20", "45 bouquet" ~$40–60 |
| Mid | Love Poem, Moon ~$85–101 | Generic "Bouquet" |
| Premium | Darling ~$180, Great Expectations ~$309 | Rarely sold at counter |

### 4.5 Product-level AOV (online heroes, 2026)

| Product | Qty | Revenue | Avg price | Est. GP% |
|---------|-----|---------|-----------|----------|
| To the Moon and Back | 128 | $12,160 | $95 | 33.7% |
| Love Poem | 135 | $11,475 | $85 | 31.1% |
| Touch of Honey | 153 | $9,945 | **$65** | 30.4% |
| TLC | 65 | $9,100 | $140 | 32.5% |
| XoXo | 68 | $7,480 | $110 | 33.5% |
| The Sympathy | 51 | $5,618 | $110 | 31.5% |
| Darling | 29 | $5,220 | **$180** | 37.2% |
| Great Expectations | 29 | $2,791 | **$310** | 27.3% |
| Monthly Flower Subscription | 4 | $2,340 | **$585** | — |

These 8 heroes = **~89%** of 2026 online product revenue. All are below 38% GP on full COGS allocation.

### 4.6 Add-on attach

| Metric | Actual | Alameda target | Industry example |
|--------|--------|----------------|------------------|
| Card attach (online) | **0.6%** (4/678) | **30%+** | 80 orders/wk × $15 × 52 ≈ $62K/yr potential |
| Card price | $6.50 | — | Low-friction upsell |

At **25% attach** on current online volume alone: ~170 cards × $6.50 × annualized ≈ **$3–5K/year**.

### 4.7 AOV trend (online, all-time)

| Year | SS AOV (total) | SS AOV (subtotal) |
|------|----------------|-------------------|
| 2019 | $99 | $80 |
| 2021 (peak volume) | $98 | $79 |
| 2024 | $127 | $113 |
| 2025 | $128 | $114 |
| **2026 YTD** | **$133** | **$108** |

AOV strategy is working. Volume strategy is not — order count still ~45% below 2021.

---

## 5. Customer & retention

### 5.1 Scorecard vs benchmarks

| Metric | Dandelion | Typical independent | Alameda target | Status |
|--------|-----------|--------------------|--------------------|--------|
| Repeat rate (online email, lifetime) | **20.9%** | 22–35% | **40%+** | ❌ Below |
| Repeat rate (Square, lifetime) | **31.1%** | 22–35% | 40%+ | ⚠️ Typical |
| 2026 orders from returning emails | **42.9%** | — | — | ✅ Improving |
| Orders per customer / year | **1.56** | 2.5–4.0 | **3.0+** | ❌ |
| Email capture (Square) | **7.4%** | — | 85%+ txs | ❌ Critical |
| Active subscriptions | 4 orders YTD | — | +10% growth | ❌ |

### 5.2 Online customers (Squarespace — best CRM)

| Metric | Value |
|--------|-------|
| Unique payer emails (all-time) | **5,986** |
| Repeat buyers (2+ orders ever) | **1,253 (20.9%)** |
| 2026 orders from returning emails | **291 (42.9%)** |
| 2026 orders from new emails | **387 (57.1%)** |
| Revenue from repeat-email buyers (lifetime) | **$517k (51% of all SS revenue)** |

Repeat rate looks low (21%) but **half of all lifetime online revenue** comes from repeat buyers. The 2026 mix (43% returning) is healthier than the lifetime average.

### 5.3 Customer value tiers (online, lifetime spend)

| Tier | Customers | % of base | Revenue share | Strategic note |
|------|-----------|-----------|---------------|----------------|
| VIP ($1,000+) | 85 | 1.4% | **14.6%** | Protect |
| Regular ($300–999) | 477 | 8.0% | ~25% | Best sub/win-back candidates |
| Occasional ($100–299) | 2,745 | 45.9% | ~35% | **Largest pool** — occasion reminders |
| Light (<$100) | 2,679 | 44.8% | ~25% | One-time / holiday buyers |

**Concentration:** Top 10% of customers (598) = **39% of lifetime online revenue**.

### 5.4 In-store customers (Square)

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

### 5.5 Cross-channel identity

| List | Size |
|------|------|
| Squarespace payer emails | 5,986 |
| Stripe customer emails | 4,202 |
| Square emails | 1,294 |
| **Overlap SS ∩ Square** | **167** |

Channels are siloed. The actionable list is **Squarespace emails first** (purchase-verified, richest history).

### 5.6 Alameda demographic fit

| Factor | Data | Implication |
|--------|------|-------------|
| Median HH income | $137,697 | Supports $85–$115+ everyday AOV |
| 65+ population | 31.4% | Sympathy/memorial channel structurally important |
| Subscription demographic | Ages 28–45, HH $75K+ | Alameda median $137K — **strong sub fit** |
| Online purchase share (national) | 42–48% | Dandelion at 49% — digital maturity |

**Paradox:** Market fit is excellent; execution on POS pricing, margin discipline, and retention systems is not.

---

## 6. High-LTV channels

### 6.1 Subscriptions

| Metric | Dandelion | Industry | Alameda |
|--------|-----------|----------|---------|
| 2026 sub orders | **4** | 18% of online rev (long-term mix) | Grow 20% YoY |
| Lifetime sub orders | 78 | — | — |
| Price | **$195–200/mo** | $65–120/mo typical | Premium — appropriate for Alameda |
| Past sub-buyer emails | 54 | — | Reactivation target |

At $195/mo, **10 active subs = $23K ARR** — one of the highest-leverage retention plays. Currently near zero.

### 6.2 Weddings

| Metric | Benchmark (East Bay) | Dandelion |
|--------|---------------------|-----------|
| Avg full wedding contract | **$5,500–$8,000** | Not tracked |
| Inquiry → close rate | 20–35% | No pipeline |
| Invoice channel 2026 | — | $7,754 (47 orders, $165 avg) |

One incremental wedding/year = **$6.5–16K** (master plan estimate).

### 6.3 Sympathy / memorial

| Metric | Dandelion 2026 | Benchmark context |
|--------|----------------|-------------------|
| Named sympathy orders (online) | 50 orders, **$6,941**, $139 AOV | Above everyday AOV |
| Alameda 65+ demographic | 31.4% of population | Structural demand |
| Funeral home channel | Not started | 2–4 partners × 2–4 orders/mo = **$6–23K/yr** |

### 6.4 Corporate

| Metric | Industry reference | Dandelion |
|--------|-------------------|-----------|
| 20 accounts × $185/week | **~$192K/year** predictable | 6 company-tagged Square profiles |
| Master plan target | 2+ B2B accounts | Not started |

---

## 7. Gap analysis — where Dandelion over- and under-indexes

```
                    UNDER-index (fix first)          OVER-index (protect)
                    ─────────────────────          ────────────────────
Revenue             POS AOV ($49)                  Online share (49%)
                    Gross margin (31.5%)             Holiday peak execution
                    Card attach (0.6%)               Online AOV ($95–133)
                    Subscriptions (4 YTD)            Alameda market fit (income)
                    Email capture (7.4%)             Brand/catalog breadth
                    Orders/customer (1.56/yr)
                    Wholesale spend ratio (63%)
```

---

## 8. Root causes — why gross margin is low

1. **Flowers category inflated** — 54–63% of revenue vs 28–35% benchmark. Forensic review found ~$162K undocumented checks and ~$42K non-flower items coded as Flowers.
2. **Pricing vs. stem cost** — Even with clean COGS, ~31–40% product margin implies underpricing, waste, or over-buying in slow months.
3. **In-store undercharging** — $49 median POS ticket vs $95+ online subtotal on the same designs.
4. **Stem buys don't flex with volume** — Apr/Jun GP% drops to 9–11% when revenue falls but wholesale spend stays high.
5. **Owner labor not captured** — Venmo at 6.8% vs 28–35% payroll benchmark.
6. **Sales tax in COGS** — Depresses reported GP ~2–4 pts (adjust by tracking tax separately).

---

## 9. Prioritized action plan

### Revenue lever ranking (data-backed)

| Rank | Lever | Evidence | Est. impact |
|------|-------|----------|-------------|
| **1** | Raise POS AOV to online ladder | Median $49 vs $95; 40% of tickets under $40 | **+$10–15k** per similar YTD window |
| **2** | Align stem buys to weekly volume | Apr/Jun GP% 9–11% vs Feb/May 43–48% | **+$8–15k** GP if COS flexes 5–10 pts |
| **3** | Default card add-on + upsell | 0.6% attach online | **+$3–5k/yr** low effort |
| **4** | Win-back occasional buyers (2,745 emails) | 43% of 2026 orders already returning | **+$25–35k/yr** at 8% reorder rate |
| **5** | Reactivate subscriptions | 54 past buyers, 4 orders YTD | **+$5–15k ARR** |
| **6** | Capture Square email/phone | 40% anonymous sales | Unlocks all retention plays |

### Tier 1 — Close the AOV gap (Weeks 2–3)

| Action | Target | Est. impact |
|--------|--------|-------------|
| POS hero ladder = online names/prices | POS median $75 | **+$40–69K/yr** |
| Delete price-named SKUs ("20", "45 bouquet") | Enable ladder | — |
| Default card add-on at checkout | 25% attach | **+$3–5K/yr** |

### Tier 2 — Close the margin gap (Weeks 4, 10)

| Action | Target | Est. impact |
|--------|--------|-------------|
| Weekly stem-buy budget = forecast × 62% | Wholesale under 45% | **+$8–15K GP/yr** |
| Raise Touch of Honey to $80–85 | 38% hero GP | Protect volume leader |
| Recost top 8 SKUs (recipe vs predicted) | Flag below 38% | Pricing discipline |

### Tier 3 — Retention (Weeks 3, 7)

| Action | Target | Est. impact |
|--------|--------|-------------|
| Merge 5,986 SS emails; occasion capture | 35% repeat in 90 days | **+$25–35K/yr** at scale |
| Sub offer to 54 past sub-buyers | +10 active subs | **+$23K ARR** |
| Square email/phone on every tx | 70% capture in 90 days | Unlocks CRM |

### Tier 4 — High-LTV channels (Weeks 5–9) — only after Tier 1–2 moving

Weddings, sympathy funeral homes, corporate — all benchmark-positive but **don't fix POS AOV or margin**.

### Channel investment split

```
In-store:  Fix AOV + identity capture (not more traffic)
Online:    Protect 2026 recovery; CRO + card attach + hero focus
Margin:    Weekly stem-buy discipline; recost top 8 SKUs
Retention: SS email list → occasion reminders → sub offer
```

### 90-day weekly plan

| Week | Focus | Actions | Success metric |
|------|-------|---------|----------------|
| **2** | AOV | POS hero ladder = online names/prices; delete price-named SKUs; card default-on online | POS median → $60+ |
| **3** | Retention | Merge SS emails; post-holiday win-back to occasional tier; sub offer to 54 past buyers | 1 campaign sent; +5 subs |
| **4** | Margin | Recost top 8 SKUs; weekly stem-buy vs order forecast; flag SKUs below 38% GP | Recost sheet done; Apr/Jun GP% improved |

---

## 10. Targets & monthly tracking

### 90-day targets (revised from benchmarks)

| Metric | Baseline | 90-day (Q3 end) | 12-month (Alameda) |
|--------|----------|-----------------|---------------------|
| POS median AOV | $49 | **$75** | $95+ |
| Blended AOV | $78 | **$90** | $110+ |
| Gross margin % | 31.5% | **38%** | 45% → 62% path |
| Wholesale % of revenue | 63% | **<55%** | <40% |
| Card attach | 0.6% | **20%** | 30%+ |
| Repeat rate (email) | 21% | **30%** | 40%+ |
| Active subscriptions | ~0 | **10** | +20% YoY |
| Online YTD growth | +41% | Maintain | — |

### What to measure monthly

Use [`monthly-scorecard-2026.csv`](strategy/monthly-scorecard-2026.csv) + [`benchmark-scorecard-2026.csv`](strategy/benchmark-scorecard-2026.csv):

1. **Revenue** — Square net + SS total + bank deposits
2. **GP%** — from accounts (target: never below 25% in any month)
3. **AOV** — POS median, SS median, blended
4. **Online %** — maintain 45–50%+
5. **Card attach %** — target 25%+
6. **New vs returning email orders** — target 45%+ returning
7. **Sub active count** — manual until POS tracks

---

## 11. Data notes & remaining gaps

| Data point | Source | Confidence |
|------------|--------|------------|
| Revenue, GP%, wholesale % | Accounts forensic CSV | High |
| AOV, channel mix, seasonality | Square + Squarespace exports | High |
| Product margins | Weekly COGS allocation model | Medium (predicted) |
| Wedding / corporate | Not in exports | Low — needs tagging |
| Benchmarks | [industry-benchmarks.md](strategy/industry-benchmarks.md) | Reference only |

**Remaining gaps:**
- **COGS:** Delivery/labor not separately classified in COS — may be understating true COGS.
- **Per-SKU margin:** Needs recipe costs for top 8 heroes (compare to [product-margin-analysis.md](strategy/product-margin-analysis.md)).
- **Weddings:** Still not tagged in commerce data; invoice channel ($7.8k YTD) likely includes some.
- **Active subscription count:** Need manual count of current recurring deliveries.

---

## Appendix — file references

| File | Use |
|------|-----|
| [`data/revenue/square-transactions-2026-ytd.csv`](../data/revenue/square-transactions-2026-ytd.csv) | In-store revenue + AOV |
| [`data/revenue/squarespace-orders-2015-2026.csv`](../data/revenue/squarespace-orders-2015-2026.csv) | Online revenue + customers + products |
| [`data/revenue/stripe-payments-all.csv`](../data/revenue/stripe-payments-all.csv) | Fee/refund confirmation |
| [`docs/forensic-classification-review.csv`](forensic-classification-review.csv) | COGS + bank revenue |
| [`docs/strategy/monthly-scorecard-2026.csv`](strategy/monthly-scorecard-2026.csv) | Updated with GP% |
| [`docs/strategy/benchmark-comparison.csv`](strategy/benchmark-comparison.csv) | Annual actuals vs benchmarks |
| [`docs/strategy/benchmark-scorecard-2026.csv`](strategy/benchmark-scorecard-2026.csv) | Full benchmark scorecard |
