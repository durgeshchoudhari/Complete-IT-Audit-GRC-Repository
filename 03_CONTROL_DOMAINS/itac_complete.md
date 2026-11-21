# IT Application Controls (ITAC)

ITACs are controls embedded in or closely associated with business applications. They help ensure transactions are valid, complete, accurate, authorized, and processed as intended.

## Main categories
- **Input controls:** mandatory fields, format/range checks, duplicate detection, authorization, validation against master data.
- **Processing controls:** automated calculations, configured business rules, sequence checks, tolerance checks, batch totals.
- **Output controls:** report accuracy/completeness, restricted report distribution, review and follow-up of exception reports.
- **Interface controls:** record counts, control totals, error queues, rejected records, reconciliation between sending and receiving systems.
- **Workflow controls:** configured approvals, delegation rules, thresholds, and audit trails.

## Audit procedures
1. Understand process and transaction flow.
2. Identify the risk and control objective.
3. Inspect configuration and design documentation.
4. Test configuration against approved requirements.
5. Reperform calculations or validations using controlled test cases where authorized.
6. Inspect logs, rejected transactions, exception handling, and reconciliation.
7. Consider reliance on ITGCs supporting the application.

An automated control may be consistent but still wrong if configuration, program logic, master data, or access to change the rule is not controlled.
