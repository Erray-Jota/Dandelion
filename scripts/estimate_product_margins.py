#!/usr/bin/env python3
"""Estimate product gross margins by allocating weekly COGS to weekly product sales.

Assumption: no flower inventory carried week-to-week (all stems bought in week W
are consumed by sales in week W, after smoothing purchase timing with a 4-week
rolling COGS rate).

Inputs:
  - docs/forensic-classification-review.csv (weekly revenue + COGS)
  - data/revenue/squarespace-orders-2015-2026.csv (product-level online sales)
  - data/revenue/square-transactions-2026-ytd.csv (POS revenue, 2026 only)

Outputs:
  - docs/strategy/product-margin-estimates.csv
  - data/revenue/weekly-revenue-cogs-2024-2026.csv
"""
from __future__ import annotations

import csv
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "revenue"
FORENSIC = ROOT / "docs" / "forensic-classification-review.csv"

COS_CODES = {11, 12, 13, 14, 15}
FLOWERS = 11
REV_CODES = {1, 2, 3, 4}
CARD_RE = re.compile(r"card|finishing touch|greeting", re.I)
DELIV_RE = re.compile(r"deliver", re.I)
SUB_RE = re.compile(r"subscri|month", re.I)
HEROES = {
    "To the Moon and Back", "Love Poem", "Touch of Honey", "TLC", "XoXo",
    "The Sympathy", "Darling", "Deep in the Woods", "Great Expectations",
}


def money(x: str) -> float:
    s = str(x or "").strip().replace("$", "").replace(",", "")
    if s in ("", "-"):
        return 0.0
    try:
        return float(s)
    except ValueError:
        return 0.0


def parse_dt(s: str, fmts: list[str]) -> datetime | None:
    s = (s or "").strip()
    for fmt in fmts:
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass
    return None


def week_key(dt: datetime) -> str:
    y, w, _ = dt.isocalendar()
    return f"{y}-W{w:02d}"


def normalize_product(name: str) -> str:
    n = (name or "").strip()
    if not n:
        return ""
    if CARD_RE.search(n):
        return "__ADDON_CARD__"
    if DELIV_RE.search(n) and "bouquet" not in n.lower():
        return "__DELIVERY_FEE__"
    if SUB_RE.search(n):
        return "__SUBSCRIPTION__"
    n = re.sub(r"\s+", " ", n)
    return re.sub(r"\s*\(copy\)\s*", "", n, flags=re.I)


def load_weekly_pl() -> tuple[dict[str, float], dict[str, float], dict[str, float]]:
    wk_rev: dict[str, float] = defaultdict(float)
    wk_cos: dict[str, float] = defaultdict(float)
    wk_flowers: dict[str, float] = defaultdict(float)
    with FORENSIC.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            code = int(float(row["Corr_Code"] or row["Orig_Code"]))
            if code == 71:
                continue
            dt = datetime.strptime(row["Date"][:10], "%Y-%m-%d")
            wk = week_key(dt)
            amt = float(row["Amount"])
            if code in REV_CODES:
                wk_rev[wk] += amt
            elif code in COS_CODES:
                wk_cos[wk] += abs(amt)
                if code == FLOWERS:
                    wk_flowers[wk] += abs(amt)
    return wk_rev, wk_cos, wk_flowers


def load_squarespace_weekly() -> tuple[dict, dict]:
    wk_prod: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
    wk_qty: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    ss_by: dict[str, list] = defaultdict(list)
    with (DATA / "squarespace-orders-2015-2026.csv").open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            ss_by[row["Order ID"].strip()].append(row)
    for rs in ss_by.values():
        primary = next((r for r in rs if (r.get("Total") or "").strip()), rs[0])
        if (primary.get("Financial Status") or "").upper() != "PAID":
            continue
        dt = parse_dt(primary.get("Paid at"), ["%m/%d/%Y %H:%M", "%m/%d/%Y"])
        if not dt or dt.year < 2024:
            continue
        wk = week_key(dt)
        for r in rs:
            prod = normalize_product(r.get("Lineitem name"))
            if not prod:
                continue
            qty = int(float(r.get("Lineitem quantity") or 1) or 1)
            rev = qty * money(r.get("Lineitem price"))
            wk_prod[wk][prod] += rev
            wk_qty[wk][prod] += qty
    return wk_prod, wk_qty


def load_square_weekly() -> dict[str, float]:
    wk_sq: dict[str, float] = defaultdict(float)
    path = DATA / "square-transactions-2026-ytd.csv"
    if not path.exists():
        return wk_sq
    with path.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            if row.get("Event Type") == "Refund":
                continue
            dt = parse_dt(row["Date"], ["%Y-%m-%d"])
            if not dt:
                continue
            wk_sq[week_key(dt)] += money(row["Net Sales"])
    return wk_sq


def rolling_rate(weeks: list[str], numer: dict[str, float], denom: dict[str, float], idx: int) -> float:
    window = weeks[max(0, idx - 3) : idx + 1]
    rev = sum(denom[w] for w in window)
    cos = sum(numer[w] for w in window)
    return cos / rev if rev else 0.0


def allocate(
    weeks: list[str],
    wk_rev: dict[str, float],
    wk_cos: dict[str, float],
    wk_flowers: dict[str, float],
    wk_prod: dict,
    wk_qty: dict,
    wk_sq: dict[str, float],
) -> tuple[list[dict], list[dict]]:
    week_rows: list[dict] = []
    stats: dict[str, dict] = defaultdict(lambda: {
        "rev": 0.0, "cos_roll": 0.0, "cos_strict": 0.0, "cos_flowers": 0.0, "qty": 0, "weeks": 0,
    })

    for i, wk in enumerate(weeks):
        rev = wk_rev[wk]
        if rev < 200:
            continue
        rate_roll = rolling_rate(weeks, wk_cos, wk_rev, i)
        rate_strict = wk_cos[wk] / rev if rev else 0.0
        rate_flowers = rolling_rate(weeks, wk_flowers, wk_rev, i)

        prods = dict(wk_prod[wk])
        if wk_sq.get(wk):
            prods["__POS_UNATTRIBUTED__"] = prods.get("__POS_UNATTRIBUTED__", 0) + wk_sq[wk]
        total = sum(prods.values()) or rev
        residual = max(0.0, rev - total)
        if residual:
            prods["__UNATTRIBUTED_REVENUE__"] = prods.get("__UNATTRIBUTED_REVENUE__", 0) + residual
            total = sum(prods.values())

        for prod, pr in prods.items():
            if pr <= 0:
                continue
            share = pr / total
            s = stats[prod]
            s["rev"] += pr
            s["cos_roll"] += rev * rate_roll * share
            s["cos_strict"] += rev * rate_strict * share
            s["cos_flowers"] += rev * rate_flowers * share
            s["qty"] += wk_qty[wk].get(prod, 0)
            s["weeks"] += 1

        week_rows.append({
            "week": wk,
            "revenue": round(rev, 2),
            "cogs_total": round(wk_cos[wk], 2),
            "cogs_flowers": round(wk_flowers[wk], 2),
            "strict_gp_pct": round((rev - wk_cos[wk]) / rev * 100, 1) if rev else "",
            "rolling_cos_rate_pct": round(rate_roll * 100, 1),
            "flowers_cos_rate_pct": round(rate_flowers * 100, 1),
        })

    products = []
    for prod, s in stats.items():
        if s["rev"] < 100:
            continue
        products.append({
            "product": prod,
            "revenue": round(s["rev"], 2),
            "qty": s["qty"],
            "weeks_active": s["weeks"],
            "allocated_cogs_rolling": round(s["cos_roll"], 2),
            "allocated_cogs_strict": round(s["cos_strict"], 2),
            "allocated_flowers_cogs": round(s["cos_flowers"], 2),
            "gross_margin_pct_rolling": round((s["rev"] - s["cos_roll"]) / s["rev"] * 100, 1),
            "gross_margin_pct_strict": round((s["rev"] - s["cos_strict"]) / s["rev"] * 100, 1),
            "flowers_only_margin_pct": round((s["rev"] - s["cos_flowers"]) / s["rev"] * 100, 1),
            "avg_selling_price": round(s["rev"] / s["qty"], 2) if s["qty"] else "",
            "is_hero": prod in HEROES,
        })
    products.sort(key=lambda x: -x["revenue"])
    return week_rows, products


def main() -> None:
    wk_rev, wk_cos, wk_flowers = load_weekly_pl()
    wk_prod, wk_qty = load_squarespace_weekly()
    wk_sq = load_square_weekly()
    weeks = sorted(w for w in wk_rev if w.startswith(("2024", "2025", "2026")))

    week_rows, products = allocate(weeks, wk_rev, wk_cos, wk_flowers, wk_prod, wk_qty, wk_sq)

    out_products = ROOT / "docs" / "strategy" / "product-margin-estimates.csv"
    out_weeks = DATA / "weekly-revenue-cogs-2024-2026.csv"
    out_products.parent.mkdir(parents=True, exist_ok=True)

    with out_products.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(products[0].keys()) if products else [])
        w.writeheader()
        w.writerows(products)

    with out_weeks.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(week_rows[0].keys()) if week_rows else [])
        w.writeheader()
        w.writerows(week_rows)

    print(f"Wrote {len(products)} products -> {out_products}")
    print(f"Wrote {len(week_rows)} weeks -> {out_weeks}")


if __name__ == "__main__":
    main()
