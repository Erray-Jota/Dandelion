# Revenue Data Exports

Source files for the Week 1 revenue baseline (July 26, 2026).

| File | Source | Contents |
|------|--------|----------|
| `square-transactions-2026-ytd.csv` | Square → Transactions | 1,685 rows · Jan 6–Jul 25, 2026 · POS + invoices |
| `square-customers.csv` | Square → Customers | 17,526 profiles (lifetime) |
| `stripe-customers.csv` | Stripe → Customers | 4,202 profiles (lifetime spend) |
| `squarespace-orders-2015-2026.csv` | Squarespace Commerce → Orders | 9,494 orders · May 16, 2015–Jul 24, 2026 (Stripe checkout) |
| `square-monthly-summary-2026-ytd.csv` | Derived | Monthly rollup of Square transactions |
| `squarespace-monthly-summary.csv` | Derived | Monthly rollup of paid Squarespace orders |
| `squarespace-yearly-summary.csv` | Derived | Annual rollup of paid Squarespace orders |

**Notes**

- Two Square transaction exports were identical; one copy kept.
- Online revenue: prefer **Squarespace orders**. Stripe customer file is identity/lifetime support only.
- Squarespace shipping method `Dandelion Flowers & Gifts` (blank ship city) is treated as **pickup**.

**Still needed** (see [revenue data intake](../../docs/strategy/revenue-data-intake.md)):

- COGS / wholesale spend for margin
- Active subscription count + wedding revenue tags
- Wire / FTD statements if used

Analysis: [Revenue Baseline 2026 YTD](../../docs/strategy/revenue-baseline-2026-ytd.md)
