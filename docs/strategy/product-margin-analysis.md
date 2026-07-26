# Product Margin Estimates — Weekly COGS Allocation Model

**Prepared:** July 26, 2026  
**Method:** Allocate weekly COGS to weekly product sales (no inventory carry-over)  
**Data:** Accounts COGS ([`forensic-classification-review.csv`](../forensic-classification-review.csv)) · Squarespace line items · Square POS (2026)  
**Outputs:** [`product-margin-estimates.csv`](product-margin-estimates.csv) · [`weekly-revenue-cogs-2024-2026.csv`](../../data/revenue/weekly-revenue-cogs-2024-2026.csv)  
**Script:** [`scripts/estimate_product_margins.py`](../../scripts/estimate_product_margins.py)

---

## Methodology

### Assumptions

1. **No flower inventory week-to-week** — all wholesale stems purchased in week *W* are used for orders in week *W*.
2. **COGS timing is noisy** — Mayesh/Torchio purchases don’t always land the same week as the related sales, so we use a **4-week rolling COGS rate** as the primary model (strict same-week as sensitivity check).
3. **Product mix drives allocation** — within each week, total COGS is split across products by each product’s **share of that week’s attributed revenue**.
4. **Revenue denominator** = bank deposits (Square + Stripe + other) from accounts, matched to the same week as COGS.

### Formula

For week *W*:

```
rolling_cos_rate(W) = sum(COGS W-3..W) / sum(Revenue W-3..W)
allocated_cogs(product, W) = revenue(W) × rolling_cos_rate(W) × (product_rev / total_product_rev)
gross_margin%(product) = 1 - sum(allocated_cogs) / sum(product_rev)
```

### COGS definitions

| Model | COGS included | Best for |
|-------|---------------|----------|
| **Full COGS (rolling)** | Flowers + tax + materials + merchandise | P&L-consistent shop margin |
| **Flowers-only (rolling)** | Wholesale flowers/stems only | Arrangement product margin |
| **Strict same-week** | Full COGS, no smoothing | Stress test (understates peak weeks) |

### Data limitations

- **Product detail is online-heavy** — Squarespace has clean SKUs; Square POS is mostly an unattributed bucket until SKU cleanup.
- **Not recipe-level** — this is a statistical allocation, not stem-count costing.
- **Delivery/labor** — delivery fees and shop labor are not in product COGS; flowers-only model is closer for arrangements.
- **Tax in COGS** — CDTFA/sales tax payments in accounts reduce allocated product margin; flowers-only model excludes these.

---

## Headline results (2024–2026)

| Model | Blended GP% | Hero arrangements (9 SKUs) |
|-------|-------------|----------------------------|
| Full COGS, 4-week rolling | **33.3%** | **32.0%** |
| Full COGS, strict same-week | ~27–28% | **27.5%** |
| Flowers-only, 4-week rolling | ~38% shop-wide | **37.9%** |

**Interpretation:** Named arrangements likely run **~32% gross margin** on a full-cost basis and **~38%** on flowers-only — both below the 60% target and the 38% near-term goal from the master plan.

---

## Hero product margins (primary model: full COGS, rolling)

| Product | Revenue | Qty | ASP | GP% (rolling) | GP% (strict) | Flowers-only GP% |
|---------|---------|-----|-----|---------------|--------------|-------------------|
| Touch of Honey | $41,920 | 616 | $68 | **30.4%** | 27.0% | 36.6% |
| Love Poem | $38,287 | 420 | $91 | **31.1%** | 25.5% | 37.0% |
| To the Moon and Back | $36,315 | 360 | $101 | **33.7%** | 30.8% | 39.5% |
| TLC | $31,013 | 207 | $150 | **32.5%** | 28.3% | 38.1% |
| XoXo | $24,499 | 208 | $118 | **33.5%** | 30.2% | 39.4% |
| Deep in the Woods | $23,753 | 183 | $130 | **30.4%** | 26.3% | 36.3% |
| The Sympathy | $20,785 | 187 | $111 | **31.5%** | 22.8% | 38.0% |
| Darling | $12,723 | 67 | $190 | **37.2%** | 29.1% | 42.2% |
| Great Expectations | $7,719 | 25 | $309 | **27.3%** | 26.7% | 33.8% |

### Flags (rolling full COGS, revenue ≥ $2k)

**Below 38% GP — every hero except Darling:**

- Touch of Honey (30%) — highest volume, lowest ASP, worst margin
- Love Poem (31%), Sympathy (32%), TLC (33%), Moon (34%), XoXo (34%), Woods (30%)
- Great Expectations (27%) — premium price but weak margin (likely heavy stem count)
- Potted Orchids (27%), Succulents (29%)

**Above 45% GP (rolling):**

- Generic POS buckets (`100 bouquet`, `50.00 Bouquet`, `Eighty five`) — likely under-costed in allocation or higher price-per-stem
- Card add-on (`__ADDON_CARD__`) — minimal COGS if sold (few units)

---

## Margin by price band

| ASP band | Products | Revenue | Est. GP% (rolling) |
|----------|----------|---------|-------------------|
| $50–75 | 2 | $44,571 | **30.4%** |
| $75–100 | 9 | $44,406 | **34.4%** |
| $100–150 | 16 | $161,771 | **33.5%** |
| $150–250 | 8 | $41,251 | **40.3%** |
| $250+ | 8 | $68,636 | **41.6%** |

Higher price doesn’t automatically mean higher margin — **Touch of Honey at $68** is the volume leader and margin laggard. **Darling at $190** is the best hero margin.

---

## Weekly pattern (margin volatility)

When weekly revenue is high (Valentine’s, Mother’s Day), the rolling COGS rate drops and **implied product margins rise**. In slow weeks (Apr, Jun), COGS stays elevated while revenue falls → **negative or single-digit weekly shop GP%**, which drags product allocations down.

This confirms the Week 4 finding: margin is a **purchasing cadence** problem as much as a pricing problem.

---

## Pricing implications (predicted, not recipe-verified)

| Action | Product | Current ASP | Est. GP% | Suggested direction |
|--------|---------|-------------|----------|---------------------|
| **Raise or retire** | Touch of Honey | $68 | 30% | +$15–20 or push customers to Love Poem ($91) |
| **Protect** | Darling | $190 | 37% | Feature as mid-premium anchor |
| **Recost stems** | Great Expectations | $309 | 27% | Recipe audit — margin doesn’t match price |
| **Grow attach** | Card add-on | $6.50 | ~high 40s–50s% | Near-pure margin at scale |
| **Review** | TLC | $150 | 33% | Price OK; stem count may be high |

**To reach 38% full-COGS margin on Touch of Honey** at current cost structure: price needs ~**$78–80** (+15–18%), or stem count reduced ~12%.

**To reach 60% margin** on heroes (full COGS): would require roughly **2× current markup** or halving stem cost — not realistic without a full pricing reset.

---

## What this model cannot do

- Separate **labor, vessel, or delivery cost** per product
- Distinguish **sympathy vs everyday** recipe differences within the same SKU name
- Attribute **Square POS** tickets to named designs (until POS names match website)
- Replace a true **recipe cost sheet** — use this to **prioritize which 8 SKUs to recost first**

---

## Recommended next step

1. **Recipe-cost the 9 heroes** — compare predicted margin to actual stem sheets; largest gaps = data or recipe fix.
2. **Raise Touch of Honey** to $80–85 online and at counter (matches Love Poem ladder).
3. **Weekly stem-buy budget** = rolling 4-week revenue × flowers-COGS-rate (currently ~62% of revenue for flowers-only).

---

## Appendix — meta products

| Bucket | Revenue | Rolling GP% | Notes |
|--------|---------|-------------|-------|
| `__POS_UNATTRIBUTED__` | ~$112k (2026 only) | ~33% | Square tickets without clean SKU mapping |
| `__DELIVERY_FEE__` | ~$6k+ | ~40% | Mostly pass-through; labor not in COGS |
| `__SUBSCRIPTION__` | ~$37k lifetime | ~33% | 78 lifetime orders; high LTV, moderate margin |
| `__ADDON_CARD__` | <$500 | high | 0.6% attach rate — huge upside |
