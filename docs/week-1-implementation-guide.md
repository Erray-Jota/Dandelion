# Dandelion Flowers — Week 1 Implementation Guide

**Site:** https://www.dandelionflowershop.com/  
**Started:** July 18, 2026  
**Last audited:** July 25, 2026

This guide continues the website optimization work from the prior Cursor audit. Tasks are organized by day with copy-paste assets in `docs/copy/` and checklists in `docs/checklists/`.

---

## Live Site Status (July 25, 2026)

| Task | Status | Notes |
|------|--------|-------|
| Sitemap loads | ✅ Done | `https://www.dandelionflowershop.com/sitemap.xml` returns HTTP 200 |
| Product page "HOW TO ORDER" copy | ✅ Done | Live on Touch of Honey product page |
| Old "REMEMBER TO SELECT..." warning removed | ✅ Done | Not present on product pages |
| Delete duplicate products | ❌ Open | "Touch of Honey" still appears twice on homepage |
| Fix subscription typo (!2 → 12 Months) | ❓ Verify | Check Commerce → Products → Subscription variants |
| Homepage SEO title | ❌ Open | Still "Dandelion Flowers and Gifts" (target: see `docs/copy/seo-titles-and-meta.md`) |
| Shop SEO title | ❌ Open | Still "Shop — Dandelion Flowers and Gifts" |
| Single homepage H1 | ❌ Open | 6 H1 tags found (marquee blocks use H1) |
| Remove homepage popup | ❌ Open | Popup/lightbox code still present |
| Checkout gift message field | ❓ Verify | Copy references it; confirm in Settings → Checkout |
| Memorial checkout fields | ❓ Verify | Service date/time/location — confirm in checkout settings |
| Pickup + local delivery settings | ❓ Verify | Confirm in Settings → Selling |

---

## Monday — Catalog Cleanup & Sitemap (30–45 min)

### Delete these products (Commerce → Products)

| Product | Reason | Status |
|---------|--------|--------|
| Touch of Honey (Copy) | Live duplicate | ❌ Delete |
| The Sympathy (Copy) | Hidden duplicate | ❌ Delete |
| rf6vwz9wsaz7mupq5knnpdfzf308ld | No title | ❌ Delete |
| rf6vwz9wsaz7mupq5knnpdfzf308ld-gkwj9 | No title | ❌ Delete |
| vday2, vday3, vday4 | Old seasonal | ❌ Delete |

### Fix

- **Subscription variant:** Change "!2 Months Alameda Delivery" → "12 Months Alameda Delivery"

### Sitemap

- Go to **Settings → SEO**
- Confirm sitemap URL loads: https://www.dandelionflowershop.com/sitemap.xml
- If 500 error returns, contact Squarespace support

---

## Tuesday — Checkout Copy & Delivery Settings (1–2 hrs)

### Product page copy

Paste the content from `docs/copy/product-page-how-to-order.txt` above **Add to Cart** on every arrangement.

**Remove** this old text if it reappears anywhere:

> REMEMBER TO SELECT DELIVERY OR PICKUP AFTER SUBMITTING YOUR ADDRESS

### Squarespace delivery settings

**Settings → Selling → Checkout → Pickup**

- Enable pickup at: 1548 Webster St, Alameda, CA 94501

**Settings → Selling → Shipping → Local Delivery**

- Delivery zone: Alameda, Oakland, Berkeley ZIP codes
- Delivery days: Tuesday–Saturday only

---

## Wednesday — SEO Titles & H1 (45 min)

Copy from `docs/copy/seo-titles-and-meta.md` into each page's SEO panel.

### Homepage structure

- Remove or disable the 3 scrolling marquee H1 blocks
- Use **one H1 only:** Flower Delivery in Alameda, Oakland & Berkeley

---

## Thursday — Popup & Gift Message (45 min)

### Remove homepage popup

- **Pages → Home → Edit**
- Find the popup/lightbox block → delete or disable
- Keep the top announcement bar only

### Add gift message at checkout

- **Settings → Selling → Checkout → Form Fields**
- Add custom field: "Gift message" (text area, optional)
- Label: `Gift message (we'll handwrite this on your card)`

---

## Friday — Memorial Fields & QA (1 hr)

### Memorial product checkout fields

For The Sympathy, Floating Gardenia, and similar memorial products:

- Add **required** field: "Service date"
- Add **required** field: "Service time"
- Add **required** field: "Service location or funeral home name"

Use **Settings → Selling → Checkout → Form Fields** with product-specific rules, or Easify Product Options if you need per-product fields.

### Week 1 QA checklist

See `docs/checklists/week-1-qa.md`

---

## Squarespace Admin Quick Links

| Area | Path |
|------|------|
| Products | Commerce → Products |
| Homepage editor | Pages → Home → Edit |
| SEO settings | Settings → SEO |
| Checkout fields | Settings → Selling → Checkout |
| Pickup | Settings → Selling → Checkout → Pickup |
| Local delivery | Settings → Selling → Shipping → Local Delivery |
