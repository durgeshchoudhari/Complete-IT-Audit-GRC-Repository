# Complete IT Audit & GRC Repository

**One practical learning and interview-preparation repository** covering Governance, Risk & Compliance (GRC), IT Audit, ITGC, ITAC, SOC 1/SOC 2, SOX, TPRM, NIST, COSO, COBIT, internal audit, external audit, audit lifecycle, evidence, testing, reporting, remediation, and scenario-based interview questions.

> Educational portfolio only. All sample organizations, people, transactions, systems, findings, and evidence are fictional. This repository is not legal, regulatory, accounting, or certification advice. Framework applicability and control requirements must be confirmed against current authoritative publications, contracts, laws, and organizational policy.

## Start here

1. Read `00_START_HERE/learning_roadmap.md`.
2. Read `01_AUDIT_FOUNDATIONS/complete_audit_lifecycle.md`.
3. Review `02_FRAMEWORKS/` and `03_CONTROL_DOMAINS/`.
4. Open the templates in `08_AUDIT_TEMPLATES/`.
5. Run the sample audit analytics: `python src/run_all_checks.py`.
6. Work through the scenarios in `10_PRACTICAL_SCENARIOS/`.
7. Practice interview questions in `11_INTERVIEW_QUESTION_BANK/`.

## Repository map

```text
Complete-IT-Audit-GRC-Repository/
├── 00_START_HERE/              Roadmap, repo map, ethical use
├── 01_AUDIT_FOUNDATIONS/        Audit lifecycle, planning, evidence, sampling, reporting
├── 02_FRAMEWORKS/               NIST, COSO, COBIT, ISO, SOC, SOX overview and mapping
├── 03_CONTROL_DOMAINS/          ITGC, ITAC, IAM, change, operations, SDLC, cyber
├── 04_GRC/                      Governance, risk, compliance, policies, KRIs, RCSA
├── 05_SOX/                      ICFR, scoping, walkthroughs, testing, deficiency evaluation
├── 06_SOC/                      SOC 1, SOC 2, Type I/II, CUECs, subservice organizations
├── 07_TPRM/                     Third-party lifecycle, due diligence, monitoring
├── 08_AUDIT_TEMPLATES/          Audit plan, RCM, walkthrough, testing, evidence, findings
├── 09_SAMPLE_DATA/              Fictional CSV datasets
├── 10_PRACTICAL_SCENARIOS/      End-to-end audit case studies and exercises
├── 11_INTERVIEW_QUESTION_BANK/  Scenario questions and model answer frameworks
├── 12_REPORTING/                Sample report, issue rating, remediation
├── 13_AUTOMATION/               Python audit analytics
├── src/                         Runnable standard-library Python checks
└── outputs/                     Generated exception reports
```

## Coverage at a glance

| Area | Included |
|---|---|
| Complete audit process | Planning through follow-up |
| Internal audit | Independence, risk-based plan, assurance/advisory |
| External audit | Financial statement audit interface, reliance boundaries, evidence |
| GRC | Governance, risk appetite, RCSA, KRIs, policies, compliance |
| ITGC | Access, change, IT operations, program development |
| ITAC | Input, processing, output, interface, automated workflow controls |
| SOX | ICFR, ITGC dependencies, walkthroughs, testing, deficiencies |
| SOC | SOC 1 / SOC 2, Type I / Type II, scope, CUECs |
| TPRM | Inherent risk, due diligence, contracts, SOC review, monitoring, exit |
| NIST | CSF 2.0 and control assessment concepts |
| COSO | Internal Control—Integrated Framework concepts |
| COBIT | Governance and management objectives concepts |
| Automation | CSV screening checks; flags are leads, not audit conclusions |

## Run the automation

Python 3.9+ is recommended. No third-party packages are required.

```bash
python src/run_all_checks.py
```

The program reads fictional CSVs under `09_SAMPLE_DATA/` and writes exception files to `outputs/`. It checks:
- terminated users with enabled accounts and access review gaps;
- change tickets missing recorded approvals, testing, or implementation evidence;
- failed backups without alert, ticket, or successful rerun;
- vendors with overdue reassessment or missing due diligence fields;
- sample ITAC transactions with invalid or missing reference data.

**Important:** a flagged row is an item for investigation. It is not automatically a confirmed control failure. Validate population completeness and accuracy, criteria, timing, evidence reliability, compensating controls, and context before reaching an audit conclusion.

## How to publish to GitHub

```bash
git init
git add .
git commit -m "Build complete IT Audit and GRC learning repository"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Complete-IT-Audit-GRC-Repository.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Before making the repository public, inspect all files and ensure no employer/client information, credentials, personal data, or proprietary material is included.

## How to present this in an interview

Be transparent: distinguish professional experience from practice completed in this portfolio. Explain one scenario in this order: **risk → control objective → control activity → population → sample → evidence → test procedure → exception → impact → conclusion → remediation**.
