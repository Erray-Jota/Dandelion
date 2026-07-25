# AI Agents for Revenue & Margin Growth

**Purpose:** Map AI agent concepts to Dandelion's target financial metrics — what to build, what it moves, and where humans stay in the loop.  
**Last updated:** July 25, 2026  
**Related:** [Revenue Growth Framework](revenue-growth-framework.md) · [Industry Benchmarks](industry-benchmarks.md) · [Physical vs. Digital](physical-vs-digital-strategy.md)

---

## Executive Summary

AI agents won't replace flower design or delivery — but they can **automate the revenue leaks** that independent florists usually handle manually: missed follow-ups, untracked occasions, slow wedding responses, unmonitored margins, and inconsistent upselling.

**Highest-ROI agents for Dandelion (small team, Squarespace + likely Square):**

| Priority | Agent | Primary metric | Build complexity |
|----------|-------|----------------|------------------|
| 1 | **Occasion Reminder Agent** | Repeat rate, order volume | Medium |
| 2 | **Post-Delivery Growth Agent** | Repeat rate, reviews, subs | Low–Medium |
| 3 | **Checkout Upsell Agent** | AOV | Low (rules) / Medium (AI) |
| 4 | **Wedding Inquiry Triage Agent** | Wedding revenue, close rate | Medium |
| 5 | **Margin Watchdog Agent** | Gross margin % | Medium |
| 6 | **Revenue Analyst Agent** | All metrics (decision support) | Low (once data flows) |
| 7 | **Corporate Prospecting Agent** | B2B pipeline | Medium–High |
| 8 | **Sympathy Order Intake Agent** | Memorial revenue, error rate | Medium |

Agents fall into three roles:
- **Revenue agents** — drive orders, AOV, repeat purchases
- **Margin agents** — protect profit, flag pricing/waste issues
- **Intelligence agents** — analyze data, recommend priorities (feeds your monthly scorecard)

---

## Agent Map by Financial Metric

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         TARGET METRICS                                   │
├──────────────┬──────────────┬──────────────┬────────────────────────────┤
│     AOV      │    REPEAT    │   MARGIN %   │      REVENUE MIX           │
│  $85–$115    │    40%+      │   62–68%     │  direct > wire             │
├──────────────┼──────────────┼──────────────┼────────────────────────────┤
│ Checkout     │ Occasion     │ Margin       │ Wire Profitability         │
│ Upsell       │ Reminder     │ Watchdog     │ Analyzer                   │
│ Bundle       │ Post-Delivery│ Waste        │ Channel Mix                │
│ Recommender  │ Growth       │ Predictor    │ Advisor                    │
│ Premium      │ Sub Churn    │ Recipe Cost  │ Corporate Prospector       │
│ Merchandiser │ Predictor    │ Tracker      │                            │
└──────────────┴──────────────┴──────────────┴────────────────────────────┘
```

---

## Tier 1 — Build First (High ROI, Lower Risk)

These agents mostly use **existing customer and order data** and run with human approval on outbound messages.

### 1. Occasion Reminder Agent

**Moves:** Repeat customer rate (22–35% → 40%+), order volume  
**Type:** Revenue · Digital  
**Human in loop:** Approves message templates; reviews edge cases (sympathy, breakups)

**What it does:**
- Ingests customer records from Square / Squarespace orders
- Extracts occasion dates from checkout fields, order notes, and gift messages ("Happy 40th birthday Mom")
- Schedules reminders 7–14 days before birthdays, anniversaries, Mother's Day, Valentine's Day
- Drafts personalized email/SMS: *"Last year you sent Touch of Honey to Oakland — need help again?"*
- Escalates high-value lapsed customers to owner for personal outreach

**Triggers:** Weekly scan of upcoming occasions; daily send queue  
**Integrations:** Squarespace Commerce API or order export · Mailchimp / Klaviyo / SMS (Twilio)  
**KPI target:** +0.5 orders/customer/year → ~15–20% repeat rate lift

**Example workflow:**
```
Order placed → extract recipient + occasion from gift message
            → store in customer profile
            → 11 months later: draft reminder email
            → human approves batch (or auto-send if confidence high)
            → track open/click/order conversion
```

---

### 2. Post-Delivery Growth Agent

**Moves:** Repeat rate, subscription signups, review rate, AOV on return visits  
**Type:** Revenue · Digital  
**Human in loop:** Reviews negative-sentiment replies; approves subscription offers

**What it does:**
- Fires 24–48 hours after delivery confirmation
- Sends thank-you + photo request (UGC for Instagram)
- Asks for Google/Yelp review (links pre-filled)
- For first-time buyers: soft subscription pitch (*"Make every Tuesday special — $195/mo"*)
- For sympathy orders: **no upsell** — only compassionate follow-up
- Flags delivery complaints to owner immediately

**Triggers:** Order status = delivered  
**Integrations:** Squarespace order webhook · email/SMS · Google review link  
**KPI target:** Review rate 2% → 5%; sub conversion 2–5% of first-time buyers

---

### 3. Checkout Upsell Agent

**Moves:** AOV ($85 → $95+), add-on attach rate (target 30%+)  
**Type:** Revenue · Digital  
**Human in loop:** Merchandising rules set quarterly; AI suggests rule changes from data

**Two implementation levels:**

| Level | Approach | Complexity |
|-------|----------|------------|
| **Rules-based** | If cart < $80 → suggest card; if sympathy SKU → no upsell; if subscription → skip | Low — Squarespace extensions or custom code |
| **AI-assisted** | Analyze cart + recipient occasion + past purchases → rank 1–3 add-ons | Medium — needs order history API |

**Upsell logic for Dandelion:**
- Default: greeting card ($6.50)
- Cart $65–$95: suggest vase upgrade or "Darling" tier
- Cart $100+: suggest chocolates or premium card
- Sympathy/memorial: **never** push celebratory add-ons
- Pickup orders: suggest in-store add-on at confirmation email instead

**KPI target:** +$8–12 AOV → ~$4,000–$8,000/year at 80 orders/week

---

### 4. Revenue Analyst Agent

**Moves:** All metrics — decision support, not direct revenue  
**Type:** Intelligence · Digital  
**Human in loop:** Owner reviews monthly brief; agent does not change prices autonomously

**What it does:**
- Ingests monthly CSV exports (Square, Squarespace, bank)
- Computes AOV, margin estimates, channel mix, seasonality
- Compares actuals vs. [industry benchmarks](industry-benchmarks.md) and Alameda targets
- Flags anomalies: *"March AOV dropped 18% — mix shifted to $65 SKUs"*
- Recommends 2–3 priorities for next month
- Updates [monthly scorecard](monthly-scorecard-template.csv)

**Triggers:** Monthly on data upload; ad-hoc when user asks  
**Integrations:** Repo CSV files · Google Sheets · future Square API  
**KPI target:** Faster diagnosis → better priority choices (indirect revenue lift)

*This is the agent pattern you're using in Cursor today — formalize it with scheduled runs once data flows.*

---

## Tier 2 — Build Next (Higher Value, More Integration)

### 5. Wedding Inquiry Triage Agent

**Moves:** Wedding revenue ($5,500–$8,000 contracts), close rate (20–35%)  
**Type:** Revenue · Hybrid (digital intake → human consult)  
**Human in loop:** All proposals and pricing; agent qualifies and drafts only

**What it does:**
- Monitors wedding form submissions, emails, DMs
- Extracts: date, venue, guest count, budget range, style preferences
- Scores lead quality (date within service area, budget above minimum, date available)
- Drafts personalized reply within 1 hour: availability, portfolio links, consultation booking
- Prepares pre-consult brief for Karim: *"150 guests, Lake Merritt, budget $6–8K, likes garden roses"*
- Follows up at 48h / 7d if no response

**Triggers:** New inquiry webhook or email parse  
**Integrations:** Squarespace form · Gmail · Calendly · CRM spreadsheet  
**KPI target:** Response time < 1 hour; close rate +5–10%

**Does NOT:** Quote final prices, commit to dates, or send contracts without approval.

---

### 6. Margin Watchdog Agent

**Moves:** Gross margin (45–58% → 62–68%), waste reduction  
**Type:** Margin · Operations  
**Human in loop:** Approves price changes; validates wholesale data

**What it does:**
- Tracks wholesale invoices (manual upload or vendor email parse)
- Maintains recipe cost sheet for top 10 SKUs
- Alerts when stem prices shift >10%: *"Rose cost up 14% — Touch of Honey margin now 58%, was 66%"*
- Recommends price adjustments with exact dollar impact
- Flags wire orders below margin threshold
- Weekly waste log analysis if shop enters shrink data

**Triggers:** New invoice uploaded; weekly margin report  
**Integrations:** CSV upload · QuickBooks export (future) · spreadsheet  
**KPI target:** Prevent 2–3 margin points erosion (~$6K–$15K/year on $300K revenue)

---

### 7. Subscription Churn Predictor Agent

**Moves:** Subscription retention (65–75%), MRR stability  
**Type:** Revenue · Digital  
**Human in loop:** Owner calls at-risk subscribers; agent flags only

**What it does:**
- Monitors subscription payment failures, skip requests, delivery complaints
- Scores churn risk: missed payment + support email + seasonal pause pattern
- Triggers save offer: pause instead of cancel, discount on next month, personal call task
- Reports MRR, churn rate, LTV monthly

**Triggers:** Payment event · support ticket keyword · 90-day inactivity  
**Integrations:** Squarespace Subscriptions · Stripe · email  
**KPI target:** Reduce churn 2–3 percentage points

---

### 8. Sympathy Order Intake Agent

**Moves:** Memorial revenue, order error rate (<1%), on-time delivery (98%+)  
**Type:** Revenue · Hybrid  
**Human in loop:** All sensitive communication; agent validates completeness

**What it does:**
- Validates required fields: service date, time, location/funeral home
- Checks delivery window against Tue–Sat schedule
- Flags conflicts: Sunday service → suggests Saturday delivery to funeral home
- Confirms spelling of deceased name and card message
- Sends internal checklist to designer: colors, size, delivery window
- Post-delivery: compassionate follow-up only (no marketing)

**Triggers:** Sympathy SKU in cart or memorial category order  
**Integrations:** Squarespace checkout fields · Slack/email to shop  
**KPI target:** Zero failed sympathy deliveries from missing info

---

## Tier 3 — Outbound & Growth (Agent-Assisted, Human Closes)

These agents **reduce research and drafting labor** for physical/outbound strategies — they don't replace the handshake.

### 9. Corporate Prospecting Agent

**Moves:** Corporate revenue pipeline, B2B repeat rate (50%+)  
**Type:** Revenue · Agent-assisted outbound  
**Human in loop:** All visits, samples, contracts

**What it does:**
- Builds target list: law firms, dental offices, hotels, restaurants within 3 miles of Webster St
- Enriches with contact info, company size, Google reviews mentioning "lobby"
- Drafts personalized cold emails: *"We deliver weekly arrangements to offices on Park St..."*
- Tracks outreach sequence: email → follow-up → task for in-person drop-in
- Schedules quarterly check-in reminders for active accounts

**Triggers:** Weekly prospecting batch · quarterly account review  
**Integrations:** ZoomInfo / Apollo (if available) · Gmail · CRM sheet  
**KPI target:** 5–10 qualified meetings → 2–3 accounts at $150–250/week

---

### 10. Funeral Home Relationship Agent

**Moves:** Memorial order volume, referral consistency  
**Type:** Revenue · Agent-assisted outbound  
**Human in loop:** All relationship visits; agent prepares materials

**What it does:**
- Maintains database of Alameda/Oakland/Berkeley funeral homes
- Tracks order history per partner, last contact date, preferred styles
- Drafts quarterly check-in emails with reliability stats (*"100% on-time sympathy deliveries Q2"*)
- Prepares one-page sympathy menu PDF for director meetings
- Alerts when a partner hasn't referred in 60+ days

**KPI target:** 3–5 active referral partners with steady order flow

---

### 11. Local SEO Content Agent

**Moves:** Traffic / order volume (acquisition)  
**Type:** Revenue · Digital  
**Human in loop:** Reviews all published content for brand voice and accuracy

**What it does:**
- Drafts localized landing pages: "Flower Delivery Oakland," "Sympathy Flowers Berkeley"
- Generates FAQ blocks aligned to real delivery rules (Tue–Sat, ZIP codes)
- Produces Google Business Profile posts weekly (seasonal, occasions)
- Monitors ranking for target keywords vs. competitors
- Suggests meta title/description updates from [SEO copy](../copy/seo-titles-and-meta.md)

**KPI target:** Move "alameda florist" from #5 toward #3; grow non-branded organic orders 15–25%

---

### 12. Social & UGC Agent

**Moves:** Acquisition, brand trust (supports conversion)  
**Type:** Revenue · Digital  
**Human in loop:** Approves posts; never auto-posts without review initially

**What it does:**
- Drafts Instagram captions from recent delivery photos
- Repurposes post-delivery customer photos (with permission) into social content
- Suggests weekly content calendar tied to occasions (graduation, sympathy season, weddings)
- Drafts responses to DMs and comments; escalates order intents to human

**KPI target:** Consistent 3–4 posts/week without owner writing from scratch

---

## What AI Should NOT Autonomously Do

| Domain | Why human required |
|--------|-------------------|
| Sympathy messaging to grieving families | Tone, sensitivity, liability |
| Final wedding quotes and contracts | Custom pricing, creative scope |
| Price changes on live products | Business judgment, margin validation |
| Delivery promise commitments | Operational capacity unknown to agent |
| Negative review responses | Reputation risk |
| Wire order acceptance/rejection | Margin may be negative |
| Substitutions on sympathy/wedding orders | Design and emotional stakes |

**Design principle:** Agents **draft, flag, schedule, and analyze** — humans **approve, price, promise, and design**.

---

## Architecture Options for Dandelion

### Option A — No-code stack (fastest start)

| Component | Tool | Agents enabled |
|-----------|------|----------------|
| Triggers | Zapier / Make | Post-delivery email, form alerts |
| Email | Mailchimp / Klaviyo | Occasion reminders, win-back |
| SMS | Twilio | High-intent reminders |
| AI layer | ChatGPT / Claude via Zapier | Draft emails, triage inquiries |
| Data | Google Sheets | Scorecard, CRM, prospect lists |

**Best for:** Post-Delivery Growth, basic Occasion Reminders, Wedding alert-to-human  
**Cost:** ~$50–150/mo  
**Time to first agent:** 1–2 weeks

### Option B — Cursor / custom agents (this repo)

| Component | Tool | Agents enabled |
|-----------|------|----------------|
| Analysis | Cursor Cloud Agent + repo data | Revenue Analyst, Margin Watchdog |
| Docs | This GitHub repo | Strategy, benchmarks, scorecard |
| Automation | Python scripts + scheduled runs | CSV ingestion, monthly reports |
| Integrations | Composio MCP (Gmail, Sheets) | Email drafts, outreach sequences |

**Best for:** Revenue Analyst, Margin Watchdog, strategic analysis when you upload data  
**Cost:** Cursor + minimal infra  
**Time to first agent:** Immediate for analyst; 2–4 weeks for automated pipelines

### Option C — Integrated florist stack (longer term)

| Component | Tool | Agents enabled |
|-----------|------|----------------|
| POS + CRM | Hana / FloristWare / Details | Native KPI + customer tags |
| E-commerce | Squarespace + API | Checkout upsell, order webhooks |
| AI orchestration | Custom agent server | All Tier 1–2 agents unified |

**Best for:** Full agent suite at scale  
**Cost:** $200–500+/mo  
**Time:** 2–3 months

**Recommendation for Dandelion:** Start **Option A** for customer-facing automation (reminders, post-delivery) + **Option B** for financial analysis when data arrives. Evaluate Option C if revenue exceeds $500K and agent maintenance becomes a bottleneck.

---

## Phased Rollout Plan

### Phase 1 — Weeks 1–4 (Digital revenue agents)

| Agent | Effort | Expected metric impact |
|-------|--------|------------------------|
| Post-Delivery Growth | 4–8 hrs setup | Reviews + sub leads |
| Checkout Upsell (rules) | 2–4 hrs | AOV +$5–8 |
| Revenue Analyst (manual upload) | Ongoing | Decision clarity |
| Wedding inquiry auto-acknowledge | 2–4 hrs | Faster response time |

### Phase 2 — Weeks 5–8 (Retention agents)

| Agent | Effort | Expected metric impact |
|-------|--------|------------------------|
| Occasion Reminder | 8–12 hrs | Repeat rate +5–10 pts |
| Sympathy intake validation | 4–6 hrs | Error rate down |
| SEO content drafts | 4 hrs/mo | Organic traffic |

### Phase 3 — Weeks 9–12 (Margin + outbound assist)

| Agent | Effort | Expected metric impact |
|-------|--------|------------------------|
| Margin Watchdog | 8 hrs + invoice habit | Margin +2–3 pts |
| Corporate prospector | 4 hrs/week assist | Pipeline building |
| Funeral home CRM | 4 hrs setup | Memorial referrals |
| Sub churn predictor | After 20+ subs | Retention lift |

---

## Agent ROI Estimation (Conservative)

Assumptions: ~80 orders/week, $90 AOV, $400K annual revenue

| Agent | Mechanism | Est. annual impact |
|-------|-----------|-------------------|
| Checkout Upsell | +$8 AOV × 4,000 orders | **+$32,000 revenue** (~$19K gross profit at 60%) |
| Occasion Reminder | 8% of customers reorder once @ $95 | **+$30,000 revenue** |
| Post-Delivery → Reviews | SEO + conversion lift (indirect) | **+$5–15K** (harder to isolate) |
| Wedding Triage | +2 weddings @ $6,500 | **+$13,000 revenue** |
| Margin Watchdog | +2 margin points on $400K | **+$8,000 gross profit** |
| Corporate Prospector | 2 accounts @ $200/week | **+$20,800 revenue** |

**Combined realistic range:** $50K–$100K revenue/profit impact in year one if agents are deployed and humans maintain the loops.

---

## Data Requirements by Agent

| Agent | Minimum data needed |
|-------|---------------------|
| Revenue Analyst | Monthly revenue + order count CSV |
| Occasion Reminder | Customer email + order history + gift messages |
| Checkout Upsell | Product catalog + cart rules |
| Margin Watchdog | Wholesale invoices + recipe sheet |
| Wedding Triage | Form submissions or email inbox access |
| Sub Churn | Subscription status export |
| Corporate Prospector | Target list (can start from Google Maps) |

See [Revenue Data Intake](revenue-data-intake.md) — the same exports power both human analysis and agent automation.

---

## Next Steps

1. **When you're at your desktop:** Upload order/revenue exports → activates **Revenue Analyst Agent** immediately
2. **Quick win:** Configure **Post-Delivery Growth** + rules-based **Checkout Upsell** in Squarespace/Zapier
3. **Decide:** Occasion capture field at checkout (enables Reminder Agent)
4. **Optional:** Pick one outbound agent (Corporate or Funeral Home) for Phase 3

Want to go deeper on any single agent — architecture, prompts, or Zapier wiring — say which one to spec first.
