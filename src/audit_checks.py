"""Beginner audit analytics over synthetic CSV data. Flags are investigation leads only."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "09_SAMPLE_DATA"
OUT = ROOT / "outputs"


def read_rows(name):
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_rows(name, rows, fields):
    OUT.mkdir(exist_ok=True)
    with (OUT / name).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def access_check():
    out = []
    for r in read_rows("access_review.csv"):
        reasons = []
        if r["employment_status"] == "Terminated" and r["account_status"] == "Enabled":
            reasons.append("Terminated user account is enabled")
        if r["account_status"] == "Enabled" and r["manager_approval"] != "Yes":
            reasons.append("No manager approval recorded")
        if r["privileged"] == "Yes" and r["review_completed"] != "Yes":
            reasons.append("Privileged access review not completed")
        if reasons:
            out.append({"record_id": r["user_id"], "area": "IAM", "exceptions": "; ".join(reasons)})
    write_rows("iam_exceptions.csv", out, ["record_id", "area", "exceptions"])
    return len(out)


def change_check():
    out = []
    for r in read_rows("change_requests.csv"):
        reasons = []
        if r["approval_before_implementation"] != "Yes":
            reasons.append("Required approval not recorded before implementation")
        if r["testing_completed"] != "Yes":
            reasons.append("Testing not recorded as completed")
        if r["implementation_evidence"] != "Yes":
            reasons.append("Implementation evidence missing")
        if r["change_type"] == "Emergency" and r["post_implementation_review"] != "Yes":
            reasons.append("Emergency post-implementation review not recorded")
        if reasons:
            out.append({"record_id": r["change_id"], "area": "Change Management", "exceptions": "; ".join(reasons)})
    write_rows("change_exceptions.csv", out, ["record_id", "area", "exceptions"])
    return len(out)


def backup_check():
    out = []
    for r in read_rows("backup_jobs.csv"):
        reasons = []
        if r["status"] == "Failed":
            if r["alert_raised"] != "Yes":
                reasons.append("No alert recorded")
            if r["incident_ticket"] != "Yes":
                reasons.append("No incident ticket recorded")
            if r["rerun_successful"] != "Yes":
                reasons.append("No successful rerun recorded")
        if reasons:
            out.append({"record_id": r["job_id"], "area": "IT Operations", "exceptions": "; ".join(reasons)})
    write_rows("backup_exceptions.csv", out, ["record_id", "area", "exceptions"])
    return len(out)


def tprm_check():
    out = []
    for r in read_rows("vendors.csv"):
        reasons = []
        if r["inherent_risk"] in ("High", "Critical"):
            if r["soc_report_reviewed"] != "Yes":
                reasons.append("SOC report review not recorded")
            if r["security_assessment"] != "Yes":
                reasons.append("Security assessment not recorded")
            if r["incident_clause"] != "Yes":
                reasons.append("Incident notification clause not recorded")
            if r["bc_dr_evidence"] != "Yes":
                reasons.append("BC/DR evidence not recorded")
        if reasons:
            out.append({"record_id": r["vendor_id"], "area": "TPRM", "exceptions": "; ".join(reasons)})
    write_rows("tprm_exceptions.csv", out, ["record_id", "area", "exceptions"])
    return len(out)


def itac_check():
    out = []
    for r in read_rows("itac_transactions.csv"):
        reasons = []
        try:
            if float(r["amount"]) < 0:
                reasons.append("Negative transaction amount")
        except ValueError:
            reasons.append("Amount is not numeric")
        if not r["customer_id"].strip():
            reasons.append("Missing customer reference")
        if r["processing_status"] == "Processed" and r["approval_status"] != "Approved":
            reasons.append("Processed transaction not marked approved")
        if r["duplicate_flag"] == "Yes":
            reasons.append("Duplicate indicator is Yes")
        if reasons:
            out.append({"record_id": r["transaction_id"], "area": "ITAC", "exceptions": "; ".join(reasons)})
    write_rows("itac_exceptions.csv", out, ["record_id", "area", "exceptions"])
    return len(out)


def run_all():
    return {
        "IAM": access_check(),
        "Change Management": change_check(),
        "IT Operations / Backup": backup_check(),
        "TPRM": tprm_check(),
        "ITAC": itac_check(),
    }
