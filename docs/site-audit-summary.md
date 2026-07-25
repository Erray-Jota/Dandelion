# Site Audit Summary

**Site:** https://www.dandelionflowershop.com/  
**Platform:** Squarespace  
**Last audited:** July 25, 2026

Prior audit documents referenced: Design Analysis.docx, Design Analysis 3.docx, SEO.docx (June 29, 2026).

---

## Critical Issues

| Issue | Impact | Fix |
|-------|--------|-----|
| Duplicate product: Touch of Honey (Copy) | Confuses shoppers, splits SEO equity | Delete in Commerce → Products |
| 6 competing H1 tags on homepage | Weak local SEO signal | One H1: Flower Delivery in Alameda, Oakland & Berkeley |
| Homepage popup blocks products, no CTA | Bounce + lost first-visit conversions | Remove popup; keep announcement bar |
| Generic SEO titles | Misses "alameda florist" (720/mo) and delivery keywords | See `docs/copy/seo-titles-and-meta.md` |
| Services page claims same-day delivery | Trust damage vs Tue–Sat schedule | Align all copy to actual delivery windows |
| Raw URLs visible on Services page | Unprofessional broken embeds | Re-embed product blocks; remove pasted URLs |

---

## SEO Snapshot

| Page | Current Title | Recommended Title | Priority |
|------|---------------|-------------------|----------|
| Homepage | Dandelion Flowers and Gifts | Flower Delivery Alameda & East Bay \| Dandelion Flowers | P0 |
| Shop | Shop — Dandelion Flowers and Gifts | Order Flowers Online \| Alameda Florist Shop | P0 |
| Weddings | Wedding Flowers — Dandelion... | Wedding Florist Alameda & East Bay \| Dandelion Flowers | P1 |
| Memorial Services | Memorial Flowers — Dandelion... | Sympathy & Funeral Flowers Alameda \| Dandelion | P1 |
| About | About — Dandelion Flowers and Gifts | About Karim Preuss \| Alameda Florist Since 2010 | P2 |
| Contact | Contact Us — Dandelion... | Visit Dandelion Flowers \| 1548 Webster St, Alameda | P1 |

**Keyword context (from SEO.docx):** ~259 tracked keywords, #1 for branded terms, #5 for "alameda florist" (720/mo). Competitors: directories + jamescressflorist.com. Not yet cited by ChatGPT/Perplexity for local delivery queries.

---

## CRO Opportunities (Week 2+)

| Action | Effort | Expected Lift |
|--------|--------|---------------|
| Sticky header CTA: Order Flowers + (510) 522-2275 | Low | High |
| Hero section: photo + H1 + Shop Arrangements + See Subscriptions | Medium | High |
| Shop by occasion row: Birthday, Sympathy, Love, Subscription | Medium | High |
| Post-add-to-cart upsell: greeting card ($6.50) | Low | Medium |
| Trust bar: Since 2010 · Local farm flowers · Yelp rating | Low | Medium |
| Wedding inquiry form (not phone-only) | Medium | Medium |

---

## Design Direction (Weeks 5–6)

| Area | Current | Proposed |
|------|---------|----------|
| Logo | Thin script, low contrast | Larger wordmark; dark green or charcoal |
| Homepage hero | Marquee text + product grid | Full-width hero image, clear CTA, category chips |
| Typography | Mixed caps, decorative separators (〰️ * 〰️) | One serif display + one sans body |
| Product grid | Uniform squares, small titles | Larger cards, occasion tags, hover state |
| Color | Mostly black/white | Sage green + warm cream accent (1920s garden feel) |
| Popup | Full-screen overlay, no action | Remove or convert to slim announcement bar |

---

## Implementation Phases

1. **Week 1** — Fix critical SEO & catalog (sitemap, duplicates, meta titles, H1) → `docs/week-1-implementation-guide.md`
2. **Week 2** — CRO quick wins (remove popup, sticky CTA, trust bar, delivery info)
3. **Week 3** — New homepage hero + shop-by-occasion sections
4. **Week 4** — Local SEO (Google Business, schema, location pages)
5. **Weeks 5–6** — Design refresh (logo, typography, color system)
