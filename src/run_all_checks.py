"""Run all beginner audit analytics and create a summary."""
from audit_checks import run_all
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"


def main():
    results = run_all()
    OUT.mkdir(exist_ok=True)
    lines = [
        "COMPLETE IT AUDIT & GRC REPOSITORY — SAMPLE ANALYTICS",
        "=====================================================",
        "",
        "IMPORTANT: flagged records are leads for auditor investigation, not confirmed findings.",
        ""
    ]
    for area, count in results.items():
        lines.append(f"{area}: {count} record(s) flagged")
    lines += [
        "",
        "Review the CSV exception reports. Validate source population, criteria, evidence,",
        "timing, false positives, and compensating controls before reaching conclusions."
    ]
    summary = "\n".join(lines)
    (OUT / "summary.txt").write_text(summary, encoding="utf-8")
    print(summary)
    print(f"\nReports written to: {OUT}")


if __name__ == "__main__":
    main()
