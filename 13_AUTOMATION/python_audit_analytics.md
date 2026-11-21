# Python Audit Analytics

This repository uses Python's standard library to read fictional CSV files and flag records matching simple rules.

## Checks included
- IAM: terminated employee with enabled account; enabled access without approval; privileged review incomplete.
- Change: approval/testing/implementation evidence gaps; emergency review not recorded.
- Backup: failed job without alert, incident ticket, or successful rerun.
- TPRM: high/critical vendor due diligence or reassessment indicators.
- ITAC: negative amount, missing customer reference, pending approval on processed transaction, duplicate indicator.

## Run

```bash
python src/run_all_checks.py
```

## Auditor responsibilities
Validate data source and population, understand policy criteria, investigate false positives, assess compensating controls, and document conclusions. Do not use the script to make autonomous compliance or audit decisions.
