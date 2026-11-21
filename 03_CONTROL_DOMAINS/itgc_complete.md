# IT General Controls (ITGC)

## 1. Logical access / IAM
Risks: unauthorized access, excessive privilege, orphan accounts, inappropriate access, SoD conflicts.
Typical controls: unique IDs, joiner-mover-leaver workflow, approvals, MFA, privileged access controls, periodic access reviews, timely termination, service-account governance.
Audit procedures: compare HR leavers to active accounts; inspect approvals; review role design and privileged access; test UAR completion and remediation; inspect authentication configuration.

## 2. Change management
Risks: unauthorized or inadequately tested changes affect production, processing, availability, or reporting.
Typical controls: documented request, impact/risk assessment, segregation of developer and deployer, approvals, testing, migration authorization, deployment logs, emergency process and retrospective review.
Audit procedures: obtain complete change population; sample normal/emergency changes; inspect approvals, testing, UAT, segregation, migration logs, emergency justification and post-implementation review.

## 3. IT operations
Risks: failed jobs, backups, monitoring, incidents, and capacity issues affect processing and availability.
Typical controls: job monitoring, backup monitoring, incident/problem management, batch reconciliation, alert escalation, restore testing, DR exercises.
Audit procedures: inspect failed jobs and resolution; test backup evidence and restore results; review incident SLAs; inspect batch exception handling.

## 4. Program development / SDLC
Risks: new systems or major changes are not securely designed, tested, approved, or migrated.
Typical controls: project governance, requirements, security design, testing, UAT, release approval, migration controls, post-implementation review.
Audit procedures: select projects/releases and trace lifecycle evidence.

## Common ITGC evidence
HR listings, identity exports, access tickets, role matrices, UAR attestations, privileged logs, change tickets, source-control/CI-CD logs, test results, deployment logs, backup logs, incident tickets, DR/restore reports.
