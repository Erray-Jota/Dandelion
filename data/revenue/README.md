# Revenue Data Exports

Source files for the Week 1 revenue baseline (July 26, 2026).

| File | Source | Contents |
|------|--------|----------|
| `square-transactions-2026-ytd.csv` | Square → Transactions | 1,685 rows · Jan 6–Jul 25, 2026 · POS + invoices |
| `square-customers.csv` | Square → Customers | 17,526 profiles (lifetime) |
| `stripe-customers.csv` | Stripe → Customers | 4,202 profiles (lifetime spend) |
| `stripe-payments-all.csv` | Stripe → Payments | 9,823 charges · May 18, 2015–Jul 25, 2026 |
| `squarespace-orders-2015-2026.csv` | Squarespace Commerce → Orders | 9,494 orders · May 16, 2015–Jul 24, 2026 |
| `square-monthly-summary-2026-ytd.csv` | Derived | Monthly rollup of Square transactions |
| `squarespace-monthly-summary.csv` | Derived | Monthly rollup of paid Squarespace orders |
| `squarespace-yearly-summary.csv` | Derived | Annual rollup of paid Squarespace orders |
| `stripe-monthly-summary.csv` | Derived | Monthly Stripe charges, fees, refunds, failures |
| `stripe-yearly-summary.csv` | Derived | Annual Stripe charges and fees |

**Notes**

- Two Square transaction exports were identical; one copy kept.
- **Online revenue:** Squarespace orders (product/shipping detail). **Stripe payments** confirm totals and add fees/refunds/failed attempts.
- Squarespace shipping method `Dandelion Flowers & Gifts` (blank ship city) is treated as **pickup**.
- Stripe customer file matches the earlier upload (identical).

**Still needed** (see [revenue data intake](../../docs/strategy/revenue-data-intake.md)):

- Per-SKU **recipe** costs (to validate predicted margins)
- Active subscription count + wedding revenue tags
- Wire / FTD statements if used

Analysis: [Revenue Baseline 2026 YTD](../../docs/strategy/revenue-baseline-2026-ytd.md) · [Customer & AOV Analysis](../../docs/strategy/revenue-customer-aov-analysis.md)
