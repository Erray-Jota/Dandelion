#!/usr/bin/env python3
"""Build forensic classification spreadsheet with monthly P&L tabs."""
import re
import pandas as pd
import numpy as np
from pathlib import Path

UPLOAD = Path("/home/ubuntu/.cursor/projects/workspace/uploads")
OUT = Path("/workspace/docs/forensic-classification-review.xlsx")

CODE_NAMES = {
    1: "Square", 2: "Stripe", 3: "Deposits", 4: "Other Income",
    11: "Flowers", 12: "Tax", 13: "Delivery", 14: "Materials", 15: "Merchandise",
    21: "Shop Labor", 22: "Venmo", 23: "Ads & Subscriptions",
    31: "Car (shop)", 32: "Rent (shop)", 33: "Utilities", 34: "Insurance", 35: "SBA / Admin",
    41: "Need to Stop", 42: "Misc", 43: "Food", 44: "Car", 45: "Furniture",
    51: "House / Rent", 52: "Utilities (home)", 53: "Health", 61: "Subscriptions",
    62: "Amazon", 63: "Groceries", 64: "Car (personal)", 65: "Entertainment",
    66: "Clothing", 67: "Travel", 68: "Household", 71: "Transfer (exclude)",
}

PL_SECTIONS = [
    ("REVENUE", None),
    (1, "Square"), (2, "Stripe"), (3, "Deposits"), (4, "Other Income"),
    ("TOTAL_REVENUE", "Total Revenue"),
    ("COS", None),
    (11, "Flowers"), (12, "Tax"), (14, "Materials"), (15, "Merchandise"),
    ("TOTAL_COS", "Total Cost of Sales"),
    ("GROSS_PROFIT", "Gross Profit"),
    ("GP_PCT", "GP %"),
    ("STORE", None),
    (22, "Venmo"), (23, "Ads & Subscriptions"), (31, "Car (shop)"), (33, "Utilities"),
    (34, "Insurance"), (35, "SBA / Admin"), (43, "Food"), (44, "Car"), (45, "Furniture"),
    (41, "Need to Stop"), (42, "Misc"),
    ("TOTAL_STORE", "Total Store Expenses"),
    ("NET_OPS", "Net Profit (ops)"),
    ("NP_OPS_PCT", "NP % (ops)"),
    ("PERSONAL", None),
    (51, "House / Rent"), (53, "Health"), (61, "Subscriptions"), (62, "Amazon"),
    (64, "Car (personal)"), (65, "Entertainment"), (66, "Clothing"), (67, "Travel"), (68, "Household"),
    ("TOTAL_PERSONAL", "Total Personal"),
    ("NET_TOTAL", "Total Net Profit"),
    ("NET_PCT", "Total NP %"),
]

REVENUE_CODES = {1, 2, 3, 4}
COS_CODES = {11, 12, 13, 14, 15}
STORE_CODES = {22, 23, 31, 32, 33, 34, 35, 41, 42, 43, 44, 45}
PERSONAL_CODES = {51, 52, 53, 61, 62, 63, 64, 65, 66, 67, 68}
EXCLUDE_CODES = {71}

FLOWER_KW = [
    "mayesh", "torchio", "rafas", "floral supply", "grace nursery", "miguel flowers",
    "encinal nursery", "neve bros", "mt eden", "wholesale flower", "nursery compan",
    "faire", "lupe farm", "floral supply synd", "wholesale", "miguel flower",
]

# 2024.xlsx Marin clean Class -> P&L code (user's original 2024 mapping)
MARIN_CLASS_TO_CODE = {
    "Income": 4, "Square": 1, "Stripe": 2,
    "State Tax": 12, "Federal Tax": 12,
    "Credit Card Payment": 71, "Transfer": 71,
    "Business Services": 35, "Utilities": 33, "Bills & Utilities": 33,
    "Health Insurance": 53, "Food & Dining": 43, "Fast Food": 43, "Coffee Shops": 43,
    "Auto & Transport": 44, "Gas": 31, "Shopping": 14, "Check": 11,
    "Financial": 34, "Entertainment": 65, "Clothing": 66,
    "Uncategorized": 42, "Office Supplies": 14, "Electronics & Software": 14,
    "Gym": 53, "Pharmacy": 53, "Rental Car & Taxi": 67, "Home Improvement": 45,
    "Fees & Charges": 42, "Charity": 42, "Service & Parts": 31,
    "Eyecare": 53, "Groceries": 63, "Movies & DVDs": 65, "Parking": 64,
    "Personal Care": 68, "Public Transportation": 67, "Shipping": 14,
    "Travel": 67, "Alcohol & Bars": 43, "Service Fee": 42, "Health & Fitness": 53,
}

# 2024.xlsx Capital 1 Clean Class -> code
CC_CLASS_TO_CODE = {
    "Payment/Credit": 71, "Dining": 43, "Entertainment": 65,
    "Gas/Automotive": 31, "Airfare": 67, "Other Travel": 67, "Lodging": 67,
    "Professional Services": 23, "Insurance": 34, "Phone/Cable": 61, "Internet": 61,
    "Other Services": 14, "Health Care": 53, "Other": 42, "Fee/Interest Charge": 42,
    "Merchandise": 15,  # refined by vendor below
}


def is_flower_vendor(desc):
    dl = str(desc).lower()
    return any(k in dl for k in FLOWER_KW)


def get_recipient(desc):
    desc = str(desc).strip()
    dl = desc.lower()
    if "check #" in dl:
        return f"Check #{desc.split('#')[1].strip()} — PAYEE UNKNOWN"
    mapping = [
        ("cerda zein", "Cerda Zein Real Estate (home rent)"),
        ("mayesh", "Mayesh Wholesale Flowers"),
        ("torchio", "Torchio Nursery"),
        ("rafas", "Rafa's Wholesale Flowers"),
        ("grace nursery", "Grace Nursery"),
        ("miguel", "Miguel Flowers"),
        ("lupe farm", "Lupe Farm"),
        ("venmo", "Venmo — RECIPIENT UNKNOWN"),
        ("cdtfa", "CA Dept of Tax (CDTFA)"),
        ("volvo", "Volvo Car Finance"),
        ("capital one", "Capital One CC payment"),
    ]
    for kw, name in mapping:
        if kw in dl:
            return name
    return desc


def classify_original(desc, source_class, source="bank", is_credit=False):
    """User/original classification."""
    dl = str(desc).lower()
    if is_credit:
        if desc == "Square" or (source_class == "Income" and "square" in dl):
            return 1
        if desc == "Stripe" or (source_class == "Income" and "stripe" in dl):
            return 2
        if desc in ("Deposit", "Mobile Deposit", "Deposits") or "deposit" in dl:
            return 3
        if source_class == "Income":
            return 4
        if "refund" in dl:
            return 4
        return 71

    if source_class in (None, "", "nan"):
        source_class = ""

    if source == "cc2024":
        if source_class == "Merchandise":
            return 11 if is_flower_vendor(desc) else 15
        return CC_CLASS_TO_CODE.get(source_class, 42)

    if source == "marin2024":
        if source_class == "Check":
            return 11
        if source_class == "Uncategorized" and "cerda zein" in dl:
            return 51
        if "venmo" in dl:
            return 22
        return MARIN_CLASS_TO_CODE.get(source_class, 42)

    # Generic bank / CC from 2025 mapping
    if "venmo" in dl:
        return 22
    if "cerda zein" in dl:
        return 51
    if "cdtfa" in dl or source_class == "State Tax":
        return 12
    if is_flower_vendor(desc):
        return 11
    if source_class in ("Credit Card Payment", "Transfer") or "capital one" in dl:
        return 71
    if source_class == "Merchandise" or (source == "cc" and source_class == "Merchandise"):
        return 11 if is_flower_vendor(desc) else 15
    bank_map = {
        "State Tax": 12, "Business Services": 35, "Utilities": 33, "Health Insurance": 53,
        "Food & Dining": 43, "Auto & Transport": 44, "Shopping": 14, "Check": 11,
        "Financial": 34, "Gas": 31, "Entertainment": 65, "Clothing": 66,
        "Uncategorized": 42, "Office Supplies": 62 if "amazon" in dl else 14,
        "Income": 4, "Bills & Utilities": 33, "Federal Tax": 12,
        "Dining": 43, "Gas/Automotive": 31, "Airfare": 67, "Professional Services": 23,
        "Phone/Cable": 61, "Other Services": 14, "Payment/Credit": 71,
    }
    if source_class in bank_map:
        return bank_map[source_class]
    if desc == "Square":
        return 1
    if desc == "Stripe":
        return 2
    return 42


def classify_corrected(desc, source_class, source="bank", is_credit=False, amount=0):
    """Forensic reclassification."""
    dl = str(desc).lower()
    if is_credit:
        if "square" in dl or desc == "Square":
            return 1
        if "stripe" in dl or desc == "Stripe":
            return 2
        if "deposit" in dl or desc in ("Deposit", "Mobile Deposit"):
            return 3
        if "refund" in dl or desc == "CA State Tax Refund":
            return 4
        return 71

    rules = [
        (r"cerda zein", 51), (r"volvo", 64), (r"venmo", 22),
        (r"cdtfa|state tax", 12), (r"farmers ins", 34),
        (r"small business admin|u\.s\. small business", 35),
        (r"fastrak", 31), (r"google ads", 23), (r"hostrocket", 41),
        (r"lupe farm", 11),
        (r"prime video|spotify|netflix|hulu", 61),
        (r"depop|zara|goodwill|free people|anthropologie|tiffany|williams-sonoma|nordstrom|macys|shopgoodwill", 66),
        (r"aeromexico|caribeantravel|caribbean travel", 67),
        (r"capital one", 71),
    ]
    for pat, code in rules:
        if re.search(pat, dl):
            return code

    if is_flower_vendor(desc):
        return 11
    if "amazon" in dl or "amzn" in dl:
        return 62
    if source_class in ("Credit Card Payment", "Transfer", "Payment/Credit"):
        return 71
    if source_class in ("Dining", "Food & Dining", "Fast Food", "Coffee Shops", "Alcohol & Bars"):
        return 43
    if source_class == "Merchandise":
        return 11 if is_flower_vendor(desc) else 15
    if "check #" in dl:
        if amount in (2249.67, 2249.37, 2382.0, 2382, 2250, 2450, 2446.38, 2446, 2446.46, 2382.0):
            return 51
        return 11
    if source_class == "Uncategorized" and amount > 2000:
        return 51

    orig = classify_original(desc, source_class, source, is_credit)
    # Flip clearly personal items that were in business codes
    if orig in (11, 14, 15) and any(k in dl for k in ["depop", "zara", "goodwill", "tiffany", "williams-sonoma", "verizon wrls"]):
        return 66
    return orig


def load_all_transactions():
    rows = []

    # --- 2024.xlsx clean sheets (authoritative for 2024) ---
    p2024 = UPLOAD / "2024_1070.xlsx"
    marin = pd.read_excel(p2024, sheet_name="Marin clean")
    marin["Date"] = pd.to_datetime(marin["Date"])
    for _, r in marin.iterrows():
        credit = float(r["Credit"]) if pd.notna(r["Credit"]) else 0
        debit = float(r["Debit"]) if pd.notna(r["Debit"]) else 0
        if credit > 0:
            amt, is_credit = credit, True
        elif debit != 0:
            amt, is_credit = debit, False  # debit already negative
        else:
            amt = -abs(float(r["Amount"])) if r["Class"] != "Income" else abs(float(r["Amount"]))
            is_credit = amt > 0
        rows.append({
            "Date": r["Date"], "Source": "Bank of Marin",
            "Description": r["Details"], "Raw_Class": r["Class"],
            "Amount": amt, "Is_Credit": is_credit,
            "Data_Source": "2024.xlsx Marin clean",
            "Workbook_Code": None,
        })

    cc24 = pd.read_excel(p2024, sheet_name="Capital 1 Clean")
    cc24["Date"] = pd.to_datetime(cc24["Date"])
    for _, r in cc24.iterrows():
        if r["Class"] == "Payment/Credit":
            continue
        debit = float(r["Debit"]) if pd.notna(r["Debit"]) else 0
        amt = debit if debit != 0 else -abs(float(r["Amount"]))
        rows.append({
            "Date": r["Date"], "Source": "Capital One CC",
            "Description": r["Details"], "Raw_Class": r["Class"],
            "Amount": amt, "Is_Credit": False,
            "Data_Source": "2024.xlsx Capital 1 Clean",
            "Workbook_Code": None,
        })

    # --- 2025 v3.xlsx combined sheet (authoritative for 2025) ---
    s2025 = pd.read_excel(UPLOAD / "2025_v3_66b0.xlsx", sheet_name="2025")
    s2025["Date"] = pd.to_datetime(s2025["Post Date"])
    for _, r in s2025.iterrows():
        rows.append({
            "Date": r["Date"],
            "Source": "Capital One CC" if r["Account"] == "Capital One" else "Bank of Marin",
            "Description": r["Description"],
            "Raw_Class": r.get("Categoty", r.get("Classification", "")),
            "Amount": float(r["Amount"]),
            "Is_Credit": float(r["Amount"]) > 0,
            "Data_Source": "2025 v3.xlsx",
            "Workbook_Code": int(r["Class Code"]) if pd.notna(r["Class Code"]) else None,
        })

    # --- Bank: 2023 and 2026 only (2024/2025 covered above) ---
    bom = pd.read_excel(UPLOAD / "Bank_of_Marin_1-18-2019_to_7-24-2026_91f1.xls", engine="xlrd")
    bom.columns = ["Account Number", "Date", "Check", "Description", "Debit", "Credit", "Status", "Bank_Class"]
    bom["Date"] = pd.to_datetime(bom["Date"])
    bom_other = bom[bom["Date"].dt.year.isin([2023, 2026])]
    for _, r in bom_other.iterrows():
        credit = float(r["Credit"]) if pd.notna(r["Credit"]) else 0
        debit = float(r["Debit"]) if pd.notna(r["Debit"]) else 0
        if credit == 0 and debit == 0:
            continue
        rows.append({
            "Date": r["Date"], "Source": "Bank of Marin",
            "Description": r["Description"], "Raw_Class": r["Bank_Class"],
            "Amount": credit - debit, "Is_Credit": credit > 0,
            "Data_Source": "BoM master",
            "Workbook_Code": None,
        })

    # --- CC: 2023 and 2026 only (2024/2025 covered above) ---
    cc_dfs = []
    for sheet, df in pd.read_excel(UPLOAD / "Capital_One_3947.xlsx", sheet_name=None).items():
        cc_dfs.append(df)
    for name in ["Capital_One_7-26-24_to_7-25-25_dd04.csv", "Capital_One_7-26-25_to_7-25-26_ff5e.csv"]:
        cc_dfs.append(pd.read_csv(UPLOAD / name))
    cc_all = pd.concat(cc_dfs, ignore_index=True)
    cc_all["Date"] = pd.to_datetime(cc_all["Transaction Date"])
    cc_all = cc_all.drop_duplicates(subset=["Transaction Date", "Posted Date", "Card No.", "Description", "Debit", "Credit"])
    # Exclude 2024/2025 (covered by workbooks) and payments
    cc_other = cc_all[(cc_all["Date"].dt.year.isin([2023, 2026])) & (cc_all["Category"] != "Payment/Credit")]
    for _, r in cc_other.iterrows():
        rows.append({
            "Date": r["Date"], "Source": "Capital One CC",
            "Description": r["Description"], "Raw_Class": r["Category"],
            "Amount": -float(r["Debit"]) if pd.notna(r["Debit"]) else 0,
            "Is_Credit": False,
            "Data_Source": "CC uploads",
            "Workbook_Code": None,
        })

    df = pd.DataFrame(rows)
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["YM"] = df["Date"].dt.to_period("M")
    return df


def apply_classifications(df):
    orig_codes, corr_codes = [], []
    for _, r in df.iterrows():
        wb_code = r.get("Workbook_Code")
        if pd.notna(wb_code) and wb_code is not None:
            oc = int(wb_code)
        else:
            src = "marin2024" if r["Data_Source"] == "2024.xlsx Marin clean" else (
                "cc2024" if r["Data_Source"] == "2024.xlsx Capital 1 Clean" else (
                    "cc" if r["Source"] == "Capital One CC" else "bank"))
            oc = classify_original(r["Description"], r["Raw_Class"], src, r["Is_Credit"])

        src = "marin2024" if r["Data_Source"] == "2024.xlsx Marin clean" else (
            "cc2024" if r["Data_Source"] == "2024.xlsx Capital 1 Clean" else (
                "cc" if r["Source"] == "Capital One CC" else "bank"))
        amt_abs = abs(r["Amount"])
        cc = classify_corrected(r["Description"], r["Raw_Class"], src, r["Is_Credit"], amt_abs)
        orig_codes.append(oc)
        corr_codes.append(cc)
    df["Orig_Code"] = orig_codes
    df["Corr_Code"] = corr_codes
    df["Orig_Label"] = df["Orig_Code"].map(CODE_NAMES)
    df["Corr_Label"] = df["Corr_Code"].map(CODE_NAMES)
    df["Orig_Entity"] = df["Orig_Code"].apply(lambda c: "Exclude" if c in EXCLUDE_CODES else (
        "Revenue" if c in REVENUE_CODES else "Business" if c in COS_CODES | STORE_CODES else "Personal"))
    df["Corr_Entity"] = df["Corr_Code"].apply(lambda c: "Exclude" if c in EXCLUDE_CODES else (
        "Revenue" if c in REVENUE_CODES else "Business" if c in COS_CODES | STORE_CODES else "Personal"))
    return df


def build_monthly_pl(df, code_col, years=(2023, 2024, 2025, 2026)):
    """Build monthly P&L pivot. Amounts: revenue positive, expenses negative."""
    pl_df = df[df[code_col] != 71].copy()
    months = []
    for y in years:
        ydf = pl_df[pl_df["Year"] == y]
        max_m = 12 if y < 2026 else ydf["Month"].max() if len(ydf) else 7
        for m in range(1, int(max_m) + 1):
            months.append((y, m))

    col_keys = [f"{y}-{m:02d}" for y, m in months]
    col_labels = [pd.Period(year=y, month=m, freq="M").strftime("%b %Y") for y, m in months]

    data = {}
    for key, (y, m) in zip(col_keys, months):
        sub = pl_df[(pl_df["Year"] == y) & (pl_df["Month"] == m)]
        by_code = sub.groupby(code_col)["Amount"].sum()
        data[key] = by_code

    rows_out = []
    for item in PL_SECTIONS:
        if item[1] is None:
            rows_out.append({"Line": item[0], **{k: "" for k in col_keys}})
            continue
        code, label = item
        if isinstance(code, str):
            # computed rows
            row = {"Line": label}
            for key in col_keys:
                by = data[key]
                rev = sum(by.get(c, 0) for c in REVENUE_CODES)
                cos = sum(by.get(c, 0) for c in COS_CODES)
                store = sum(by.get(c, 0) for c in STORE_CODES)
                pers = sum(by.get(c, 0) for c in PERSONAL_CODES)
                gp = rev + cos
                np_ops = gp + store
                net = np_ops + pers
                if code == "TOTAL_REVENUE":
                    row[key] = rev
                elif code == "TOTAL_COS":
                    row[key] = cos
                elif code == "GROSS_PROFIT":
                    row[key] = gp
                elif code == "GP_PCT":
                    row[key] = gp / rev if rev else ""
                elif code == "TOTAL_STORE":
                    row[key] = store
                elif code == "NET_OPS":
                    row[key] = np_ops
                elif code == "NP_OPS_PCT":
                    row[key] = np_ops / rev if rev else ""
                elif code == "TOTAL_PERSONAL":
                    row[key] = pers
                elif code == "NET_TOTAL":
                    row[key] = net
                elif code == "NET_PCT":
                    row[key] = net / rev if rev else ""
            rows_out.append(row)
        else:
            row = {"Line": label}
            for key in col_keys:
                row[key] = data[key].get(code, 0)
            rows_out.append(row)

    result = pd.DataFrame(rows_out)
    result.columns = ["Line"] + col_labels
    return result


def build_review_sheet(df):
    review = df[df["Year"].isin([2023, 2024, 2025, 2026])].copy()
    review = review[review["Orig_Code"] != 71]
    out = review[[
        "Date", "Year", "Month", "Source", "Data_Source",
        "Description", "Raw_Class", "Amount",
        "Orig_Code", "Orig_Label", "Orig_Entity",
        "Corr_Code", "Corr_Label", "Corr_Entity",
    ]].copy()
    out["Recipient / Details"] = out["Description"].apply(get_recipient)
    out["Changed?"] = np.where(out["Orig_Code"] != out["Corr_Code"], "YES", "")
    out["Reason"] = np.where(
        out["Changed?"] == "YES",
        out["Orig_Label"] + " → " + out["Corr_Label"],
        "",
    )
    out["Your Verified Entity"] = ""
    out["Your Verified Category"] = ""
    out["Your Notes"] = ""
    out = out.sort_values(["Changed?", "Amount"], ascending=[True, False],
                          key=lambda c: c.map({"YES": 0, "": 1}) if c.name == "Changed?" else c)
    cols = [
        "Date", "Year", "Month", "Source", "Data_Source", "Recipient / Details",
        "Description", "Amount", "Orig_Code", "Orig_Label", "Orig_Entity",
        "Corr_Code", "Corr_Label", "Corr_Entity", "Changed?", "Reason",
        "Your Verified Entity", "Your Verified Category", "Your Notes",
    ]
    return out[cols]


def main():
    print("Loading transactions...")
    df = load_all_transactions()
    print(f"  {len(df):,} raw rows")

    df = apply_classifications(df)
    pl_df = df[df["Year"].between(2023, 2026)]

    print("Building monthly P&L...")
    pl_orig = build_monthly_pl(pl_df, "Orig_Code")
    pl_corr = build_monthly_pl(pl_df, "Corr_Code")

    review = build_review_sheet(pl_df)
    changed = review[review["Changed?"] == "YES"]
    checks = review[review["Description"].str.contains("check #", case=False, na=False)]
    needs_review = review[review["Corr_Entity"].isin(["Personal", "Business"]) & (review["Changed?"] == "YES")]

    # Annual summaries
    def annual_summary(pl_df, code_col):
        rows = []
        for y in [2023, 2024, 2025, 2026]:
            sub = pl_df[(pl_df["Year"] == y) & (pl_df[code_col] != 71)]
            rev = sub[sub[code_col].isin(REVENUE_CODES)]["Amount"].sum()
            cos = sub[sub[code_col].isin(COS_CODES)]["Amount"].sum()
            store = sub[sub[code_col].isin(STORE_CODES)]["Amount"].sum()
            pers = sub[sub[code_col].isin(PERSONAL_CODES)]["Amount"].sum()
            gp = rev + cos
            np_ops = gp + store
            rows.append({
                "Year": y, "Revenue": rev, "COS": cos, "Gross Profit": gp,
                "Store Exp": store, "Net Ops": np_ops, "Personal": pers,
                "Net Profit": np_ops + pers,
            })
        return pd.DataFrame(rows)

    annual_orig = annual_summary(pl_df, "Orig_Code")
    annual_corr = annual_summary(pl_df, "Corr_Code")

    ref = pd.DataFrame([{"Code": k, "Category": v} for k, v in CODE_NAMES.items()])

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(OUT, engine="openpyxl") as w:
        pl_orig.to_excel(w, sheet_name="P&L Monthly Original", index=False)
        pl_corr.to_excel(w, sheet_name="P&L Monthly Reclassified", index=False)
        review.to_excel(w, sheet_name="All Transactions", index=False)
        changed.to_excel(w, sheet_name="Changed Only", index=False)
        checks.to_excel(w, sheet_name="Checks - Need Payee", index=False)
        needs_review.to_excel(w, sheet_name="Needs Review", index=False)
        annual_orig.to_excel(w, sheet_name="Annual Summary Original", index=False)
        annual_corr.to_excel(w, sheet_name="Annual Summary Reclassified", index=False)
        ref.to_excel(w, sheet_name="Category Reference", index=False)

    review.to_csv(OUT.with_suffix(".csv"), index=False)
    print(f"Saved {OUT}")
    print(f"  Transactions: {len(review):,}")
    print(f"  Changed: {len(changed):,}")
    print(f"  Monthly cols: {len(pl_orig.columns)-1}")
    print("\nAnnual Summary (Original):")
    print(annual_orig.to_string(index=False))
    print("\nAnnual Summary (Reclassified):")
    print(annual_corr.to_string(index=False))


if __name__ == "__main__":
    main()
