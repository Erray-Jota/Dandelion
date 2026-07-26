# Revenue Data Intake — What to Share

Use this checklist when feeding financial data into the revenue analysis. Share whatever you have — partial data is fine; we'll note gaps.

---

## Priority 1 — Minimum to Start (30 min to export)

| Data | Source | Format | Status |
|------|--------|--------|--------|
| Monthly revenue, last 12–24 months | Square / Squarespace / bank | CSV or Excel | ✅ Square Jan–Jul 2026 + Squarespace monthly 2015–2026 (see [baseline](revenue-baseline-2026-ytd.md)) |
| Monthly order count | Square / Squarespace orders export | CSV | ✅ Both channels |
| Annual total revenue (2024 vs 2025) | Tax records / P&L | Number or spreadsheet | 🟡 Online known (SS/Stripe 2024 $108k / 2025 $106k); Square full-year + P&L still open |

---

## Priority 2 — Channel & Product Detail

| Data | Source | What it unlocks | Status |
|------|--------|-----------------|--------|
| Sales by product (SKU/name) | Squarespace Commerce export | Hero products, margin focus, catalog pruning | ✅ Squarespace line items clean; Square POS names still messy |
| Sales by category | POS or manual tags | Everyday vs. sympathy vs. sub vs. wedding | 🟡 SS sympathy/subs visible; weddings still under-tagged |
| Online vs. in-store vs. phone | Square / manual estimate | Channel investment priority | ✅ Square vs Squarespace (~55/45 product-ish) |
| Subscription revenue separately | Square recurring or manual | MRR, churn, LTV | 🟡 78 lifetime SS “Monthly Flower Subscription” orders; active count unknown |
| Wedding revenue (annual) | Invoices / deposits | Event pipeline value | ☐ |
| Wire / third-party orders | FTD / Teleflora statements | Fee drag analysis | ☐ |

---

## Priority 3 — Margin & Operations

| Data | Source | What it unlocks | Status |
|------|--------|-----------------|--------|
| COGS or wholesale spend (monthly) | Vendor invoices / QuickBooks | Gross margin % | ✅ Accounts forensic classification (flowers, tax, materials, merch) |
| Top product recipe costs | Internal costing sheet | Pricing corrections | ☐ |
| Delivery count per week | Driver log / dispatch | Cost per delivery | ☐ |
| Waste / shrink notes | Shop estimate | Margin leak identification | ☐ |
| Labor hours (design + delivery) | Payroll / estimate | True cost per order | ☐ |

---

## Priority 4 — Customer & Retention

| Data | Source | What it unlocks | Status |
|------|--------|-----------------|--------|
| Customer email list size | Squarespace / Mailchimp | Retention campaign reach | ✅ ~5,986 Squarespace payer emails (+ Square 1,316; Stripe 4,202) |
| Repeat purchase rate | Square customer report | Retention health | ✅ Square 31% (2+ txs); SS email repeat 21%; 43% of 2026 SS orders from known emails |
| Active subscription count | Manual / POS | Recurring base size | ☐ |
| Corporate accounts (if any) | AR / invoice list | B2B expansion baseline | 🟡 Only 6 Square profiles with company name |

---

## Export How-To (Squarespace + Square)

### Squarespace Commerce

1. **Commerce → Orders → Export** — includes date, product, total, customer
2. **Commerce → Analytics → Revenue** — screenshot or note monthly totals
3. **Commerce → Subscriptions** — active count and plans if enabled

### Square POS (if used in-shop)

1. **Square Dashboard → Reports → Sales Summary** — by month
2. **Items → Sales by Item** — top products
3. **Customers → Frequent customers** — repeat signal

### What to name files

```
data/revenue/monthly-revenue-2024-2025.csv
data/revenue/orders-export-2025.csv
data/revenue/products-by-revenue.csv
data/revenue/subscriptions.csv
```

Place files in a `data/revenue/` folder in this repo, or attach in chat.

---

## Quick Questions (Answer in Chat if Easier)

1. What was **total revenue** in 2024 and 2025 (approximate is fine)?
2. What **percentage** of orders are: delivery vs. pickup vs. walk-in?
3. How many **active subscriptions** do you have?
4. Roughly how many **weddings** per year, and average contract value?
5. Do you take **wire orders** (FTD, Teleflora, etc.)? Rough % of revenue?
6. What's your sense of **busiest vs. slowest** months?
7. Biggest **margin pain** right now — stems, labor, delivery, or discounts?

---

## What You'll Get Back

Once data is shared:

1. **Revenue dashboard summary** — trends, seasonality, concentration risk
2. **Channel mix chart** — where money comes from today
3. **2–3 prioritized growth levers** with numeric targets
4. **Margin recommendations** — pricing, product mix, cost controls
5. **90-day action plan** tied to measurable outcomes

### Latest delivery

- **[Revenue Baseline 2026 YTD](revenue-baseline-2026-ytd.md)** — channel dashboard from commerce exports
- **[Revenue, Customer & AOV Analysis](revenue-customer-aov-analysis.md)** — Week 4 deliverable with COGS/margin from accounts
