# Week 4 — P&L Analysis & Benchmark Comparison

**Prepared:** July 26, 2026  
**Plan reference:** [Week 4 — Measure & Recost](master-plan-weekly-priorities.md#week-4--measure--recost-foundation)  
**Benchmarks:** [industry-benchmarks.md](strategy/industry-benchmarks.md) · [revenue-baseline-2026-ytd.md](strategy/revenue-baseline-2026-ytd.md)

---

## Executive Summary

Dandelion is a **~$300K independent florist** — right in the healthy revenue band — with a **two-channel business** (Square in-store ~55% / Squarespace online ~45%). The numbers tell a clear story:

| Finding | Detail |
|---------|--------|
| **Gross margin is the #1 gap** | 38–44% actual vs **62–68%** Alameda target. Wholesale/flowers spend is **49–55% of revenue** vs **28–35%** benchmark. |
| **Ops profit is healthy** | Net ops margin **12–19%** (2023–2025) vs **10–14%** target — overhead is lean at 22.5% of revenue. |
| **Online AOV is on target** | Squarespace median **$121** total / **$95** subtotal — already hits the $95+ goal. |
| **In-store AOV is the leak** | Square median **$49** vs online **$121**. Same shop, same flowers — counter is leaving ~$40/order on the table. |
| **Card attach is ~0%** | 0.2–0.6% online attach on a $6.50 SKU vs **25–30%** target. |
| **Repeat rate below target** | 21% (Squarespace emails) / 31% (Square) vs **40%+** Alameda goal. |

### Two focus metrics for the next 8 weeks

1. **Gross margin %** (product COGS) — move from ~40% toward **50%+** via recosting top SKUs, pricing fixes, and cleaner COGS coding
2. **In-store AOV** (Square median) — move from **$49** toward **$75+** by mirroring the online hero price ladder at the counter

---

## 1. Annual P&L (Bank + CC — Original Classification)

Sources: Bank of Marin, Capital One, `2024.xlsx`, `2025 v3.xlsx`  
Rebuild: `python3 scripts/build_forensic_pl.py`

| Year | Revenue | Gross Profit | GP % | Net Ops | Net Ops % | Total Net | Total NP % |
|------|---------|-------------|------|---------|-----------|-----------|------------|
| **2023** | $333,737 | $115,032 | 34.5% | $61,715 | **18.5%** | $53,032 | **15.9%** |
| **2024** | $282,530 | $116,579 | 41.3% | $34,619 | **12.3%** | ($23,134) | **-8.2%** |
| **2025** | $299,115 | $114,045 | 38.1% | $46,609 | **15.6%** | ($1,845) | **-0.6%** |
| **2026 YTD** | $184,160 | $53,680 | 29.1% | $20,794 | **11.3%** | $2,054 | **1.1%** |

*2025 workbook cross-check: Revenue $299,115 · GP $97,485 (32.6%) · Net Ops $46,609 (15.6%) — matches bank P&L.*

### Product margin (excludes sales tax from COGS)

Industry benchmarks measure flowers + materials + merchandise only — not CDTFA remittances.

| Year | Product COGS | % of Rev | Adjusted GP % | vs. 62–68% target |
|------|-------------|----------|---------------|-------------------|
| 2023 | $199,962 | 59.9% | **40.1%** | −22 to −28 pts |
| 2024 | $158,992 | 56.3% | **43.7%** | −18 to −24 pts |
| 2025 | $179,275 | 59.9% | **40.1%** | −22 to −28 pts |

### Reclassified view (2025 stress test)

Forensic reclassification removes $22.5K transfers miscoded as income and reassigns personal/non-flower items. See [forensic-classification-review.xlsx](forensic-classification-review.xlsx).

| Metric | Original | Reclassified |
|--------|----------|--------------|
| Revenue | $299,115 | $276,591 |
| GP % | 38.1% | **25.8%** |
| Net Ops % | 15.6% | **5.6%** |

Use original for day-to-day ops; use reclassified to stress-test worst-case margin.

---

## 2. Benchmark Scorecard — Actuals vs. Alameda Targets

Full table: [strategy/benchmark-comparison.csv](strategy/benchmark-comparison.csv)

| Metric | National | Alameda target | 90-day plan | **2025 actual** | Status |
|--------|----------|----------------|-------------|-----------------|--------|
| Annual revenue | $300–500K healthy | — | — | **$299K** | ✓ On scale |
| **Gross margin** | 65–72% | **62–68%** | 60%+ | **38–44%** | 🔴 Critical |
| **Net ops margin** | 8–15% | **10–14%** | — | **15.6%** | ✓ Above target |
| **Total net margin** | 8–15% | **10–14%** | — | **−0.6%** | 🔴 Personal bleed |
| Wholesale/flowers % rev | 28–35% | **28–35%** | — | **54.5%** | 🔴 ~2× benchmark |
| **Online AOV** | $65–90 | **$85–115** | $95+ | **$128** total / **$114** subtotal | ✓ Above target |
| **In-store AOV** | $65–90 | **$85–115** | $95+ blend | **~$66** mean / **$49** median (2026) | 🔴 Well below |
| **Blended AOV** | — | **$95+** | $95+ | **~$82** est. | 🟡 Below target |
| Repeat customer rate | 22–35% | **40%+** | 35%+ | **21%** SS / **31%** Sq | 🟡 Below target |
| Card attach rate | 25–40% | **30%+** | 25%+ | **0.2%** | 🔴 Critical |
| Active subscriptions | — | Grow 20% YoY | +10% | **9 orders** (2025) | 🔴 Minimal |
| Payroll % revenue | 28–35% | 28–35% | — | **6.8%** (Venmo only) | ⚠️ Under-reported |

---

## 3. Channel Analysis (Order-Level Data)

Sources: [data/revenue/](../data/revenue/) · [revenue-baseline-2026-ytd.md](strategy/revenue-baseline-2026-ytd.md)

### 2026 YTD channel split

| Channel | Net sales | Orders | Mean AOV | Median AOV |
|---------|-----------|--------|----------|------------|
| Square (in-store + invoices) | $111,578 | 1,680 | $66 | **$49** |
| Squarespace (online via Stripe) | $89,835 total | 678 | $133 | **$121** |
| Squarespace product subtotal | $73,212 | 678 | $108 | **$95** |
| **Combined** | **~$185K** product-ish | — | — | — |

Online is **~40–45%** of measurable product revenue — not a side channel.

### 2025 full-year online (Squarespace)

| Metric | Value | vs. benchmark |
|--------|-------|---------------|
| Paid orders | 829 | — |
| Order total | $106,459 | — |
| AOV (total) | **$128** | Above $85–115 ✓ |
| AOV (subtotal) | **$114** | On target ✓ |
| Card attach | **0.2%** (2 orders) | vs 30% target 🔴 |
| Subscription orders | 9 (~$4K) | Minimal 🔴 |
| Sympathy orders | ~50 named SKUs | Material channel |

### In-store vs. online — the AOV gap

```
Online median AOV    ████████████████████████  $121
Alameda target       ██████████████████        $95
In-store median AOV  ██████████                $49
```

Same flowers, same shop — the counter is selling at roughly **half** the online ticket. The online hero ladder (Touch of Honey $65 → Love Poem $85 → Moon $95 → TLC $140) is not reflected in POS naming (price-named SKUs like "20" and "45 bouquet" dominate).

**Impact math:** Lifting half of ~1,000 sub-$60 Square tickets by $20 ≈ **+$10K** on similar YTD traffic.

### Payment channel mix (2025 bank P&L)

| Channel | Amount | % of revenue |
|---------|--------|-------------|
| Square | $161,980 | 54.2% |
| Stripe | $102,823 | 34.4% |
| Deposits + other | $34,312 | 11.5% |

Stripe ≈ Squarespace online. The ~$56K gap between Square bank deposits ($162K) and Squarespace total ($106K) is in-store POS + invoices.

---

## 4. Seasonality

### Monthly revenue index (bank P&L, 2023–2025 average)

| Month | Avg revenue | Index* | Avg GP % | Peak event |
|-------|------------|--------|----------|------------|
| Jan | $14,629 | 58 | 8.8% | Post-holiday trough |
| **Feb** | **$37,049** | **146** | 48.7% | Valentine's |
| Mar | $24,024 | 95 | 30.9% | — |
| Apr | $30,422 | 120 | 45.3% | Easter |
| **May** | **$45,468** | **179** | 44.6% | **Mother's Day** |
| Jun | $25,472 | 100 | 42.5% | Baseline |
| Jul | $16,495 | 65 | 14.2% | Summer slow |
| Aug | $18,830 | 74 | 25.5% | — |
| Sep–Dec | $20–28K | 80–108 | 19–44% | Thanksgiving / holidays |

*Index: 100 = average month (~$25,500)*

**2025 peak months:** May ($39,878), Feb ($29,595), Oct ($27,100)  
**2025 trough months:** Aug ($20,720), Apr ($20,247), Jun ($21,178)

Plan inventory and stem buying around Feb/May peaks; Jul/Aug average **14–26% GP** — protect margin in slow months by reducing wholesale orders.

### Quarterly P&L trend

| Quarter | Revenue | GP % | Net Ops % |
|---------|---------|------|-----------|
| 2025 Q1 | $78,380 | 43.2% | 15.9% |
| 2025 Q2 | $81,303 | 35.4% | 12.2% |
| 2025 Q3 | $67,628 | 36.3% | 17.2% |
| 2025 Q4 | $71,804 | 37.4% | 17.6% |

Trailing 12 months (Aug 2025 – Jul 2026): Revenue $299K · GP **30.9%** · Net ops **12.4%** — gross margin compressing vs prior years.

---

## 5. Customer & Retention

| Source | Repeat rate | Notes |
|--------|------------|-------|
| Squarespace emails (all-time) | **20.7%** (2+ orders) | 5,630 unique emails; repeat buyers = 51% of lifetime online revenue |
| Square customers (all-time) | **31%** (2+ transactions) | 17,526 profiles but only **7.5%** have email |
| 2026 SS orders from known emails | **43%** | Healthier than raw repeat rate suggests |
| 2025 cohort (same-year repeat) | **11.8%** | 83 of 704 emails ordered 2+ times in 2025 |

**Gap vs. 40%+ Alameda target:** Need occasion reminders, post-holiday win-back, and subscription offers. Nearly half of 2026 online orders come from existing emails — retention infrastructure exists but isn't being activated.

**Identity gap:** ~40% of Square YTD revenue is anonymous (no customer ID). Requiring email/phone at POS is prerequisite for repeat-rate improvement.

---

## 6. Product Mix & Margin Levers

### Online hero concentration (2026 YTD)

| Product | Line revenue | Share |
|---------|-------------|-------|
| To the Moon and Back | $12,160 | — |
| Love Poem | $11,475 | — |
| Touch of Honey | $9,945 | — |
| TLC | $9,100 | — |
| XoXo | $7,480 | Top 5 = **68.5%** of online product $ |
| The Sympathy | $5,618 | Sympathy is material (~$7K YTD) |
| Darling | $5,220 | Premium anchor |

**Recost priority:** Top 8 online SKUs first — they represent 89% of online product revenue. Flag any below 60% product margin.

### Store expense breakdown (2025)

| Category | Amount | % rev | Benchmark |
|----------|--------|-------|-----------|
| Venmo (labor proxy) | $20,330 | 6.8% | Payroll 28–35% |
| Food | $6,380 | 2.1% | Review personal mix |
| SBA / Admin | $7,561 | 2.5% | OK |
| Utilities + insurance + car | $12,191 | 4.1% | OK |
| **Total store** | **$67,436** | **22.5%** | Lean |

The margin problem is **COGS**, not overhead.

---

## 7. Why Gross Margin Is Low — Root Causes

1. **Flowers category inflated** — 54.5% of revenue vs 28–35% benchmark. Forensic review found ~$162K undocumented checks and ~$42K non-flower items coded as Flowers.
2. **Pricing vs. stem cost** — Even with clean COGS, ~40% product margin implies underpricing, waste, or over-buying in slow months.
3. **In-store undercharging** — $49 median POS ticket vs $95+ online subtotal on the same designs.
4. **Owner labor not captured** — Venmo at 6.8% vs 28–35% payroll benchmark; true fully-loaded accounting would reduce net ops.
5. **Sales tax in COGS** — Depresses reported GP ~2 pts (adjust by tracking tax separately).

---

## 8. 90-Day Targets (Calibrated to Actuals)

| Metric | Plan default | **Recommended** | Rationale |
|--------|-------------|-----------------|-----------|
| Everyday AOV (blended) | $95+ | **$85+** interim → $95 | Online already there; need POS lift |
| In-store AOV median | — | **$49 → $75+** | Biggest revenue-per-hour lever |
| Gross margin | 60%+ | **50%+** interim → 55% | 60% is stretch; requires recost + pricing |
| Wholesale % rev | — | **< 42%** | Down from 55% |
| Repeat customer rate | 35%+ | **Track → 30%+** | Need POS email capture first |
| Card attach | 25%+ | **10% → 25%** | Currently 0.2%; quick win available |
| Net ops margin | — | **Maintain 12%+** | Already on target |

---

## 9. Prioritized Actions

### Week 4 (now)

| # | Action | Impact | Time |
|---|--------|--------|------|
| 1 | Recost top 8 online SKUs + top 5 POS items | Gross margin | 2–3 hrs |
| 2 | Flag SKUs below 55% product margin | Pricing decisions | 30 min |
| 3 | Map POS SKUs to online hero names | In-store AOV | 1 hr |
| 4 | Clean Flowers category in forensic spreadsheet | Accurate COGS % | Ongoing |

### Weeks 5–10

| # | Action | Impact |
|---|--------|--------|
| 5 | Default $6.50 card at online checkout + POS verbal prompt | Card attach → $3–5K/yr |
| 6 | Require email/phone on every Square payment | Repeat rate tracking |
| 7 | Post-Valentine/Mother's Day win-back to SS email list | Repeat rate → 30%+ |
| 8 | Subscription offer to multi-buyers (only 4 sub orders YTD) | LTV 3.4× multiplier |
| 9 | Reduce stem orders Jul/Aug to match seasonality index | COGS % reduction |
| 10 | Separate sales tax from COGS in monthly tracking | Benchmark accuracy |

---

## 10. Deliverables & Files

| File | Contents |
|------|----------|
| **[week-4-pl-analysis.md](week-4-pl-analysis.md)** | This document |
| [strategy/benchmark-comparison.csv](strategy/benchmark-comparison.csv) | Annual actuals vs benchmarks |
| [strategy/monthly-scorecard-2023-2026.csv](strategy/monthly-scorecard-2023-2026.csv) | Month-by-month P&L metrics |
| [strategy/monthly-scorecard-2026.csv](strategy/monthly-scorecard-2026.csv) | 2026 YTD order-level scorecard |
| [forensic-classification-review.xlsx](forensic-classification-review.xlsx) | Full P&L + transaction detail |
| [strategy/revenue-baseline-2026-ytd.md](strategy/revenue-baseline-2026-ytd.md) | Order-level channel analysis |
| [strategy/industry-benchmarks.md](strategy/industry-benchmarks.md) | Alameda benchmark reference |

---

## Week 4 Success Criteria Checklist

- [x] Scorecard filled with real baseline (P&L + order data)
- [x] Compare actuals vs. Alameda benchmarks
- [x] Choose 2 focus metrics for next 8 weeks: **Gross margin %** + **In-store AOV**
- [ ] Week 1 website QA complete (separate track)
- [ ] Margin issues list created → see §9 actions + forensic spreadsheet
