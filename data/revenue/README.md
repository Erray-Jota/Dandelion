# Revenue Data Exports

Source files shared for the Week 1 revenue baseline (July 26, 2026).

| File | Source | Contents |
|------|--------|----------|
| `square-transactions-2026-ytd.csv` | Square Dashboard → Transactions | 1,685 rows · Jan 6–Jul 25, 2026 · POS + invoices |
| `square-customers.csv` | Square → Customers export | 17,526 profiles (lifetime) |
| `stripe-customers.csv` | Stripe → Customers export | 4,202 profiles (lifetime spend; likely Squarespace online) |
| `square-monthly-summary-2026-ytd.csv` | Derived | Monthly rollup of Square transactions |

**Note:** Two Square transaction exports were provided (`Square 2026-01-01-2027-01-01` and `Squares-2026-01-01-2026-07-25`); they were identical, so only one copy is kept.

**Still needed** (see [revenue data intake](../../docs/strategy/revenue-data-intake.md)):

- Stripe **payments/charges** export (customer file is lifetime, not monthly revenue)
- Squarespace Commerce **orders** export (if separate from Stripe)
- COGS / wholesale spend for margin
- Subscription active count + wedding revenue tags

Analysis write-up: [Revenue Baseline 2026 YTD](../../docs/strategy/revenue-baseline-2026-ytd.md)
