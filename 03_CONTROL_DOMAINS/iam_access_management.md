# IAM Audit Program

## Key risks
- Leavers retain access.
- Users receive access without business need or approval.
- Privileged access is excessive or unmonitored.
- Conflicting roles create SoD risk.
- Shared, generic, service, or dormant accounts are not governed.

## Key controls
- HR-triggered JML workflow with defined SLA.
- Manager/application owner approval before provisioning.
- Role-based access and least privilege.
- Privileged access approval, time-bound elevation, logging, and review.
- Periodic UAR with documented challenge and remediation.
- Service-account owner, purpose, credential rotation, and monitoring.

## Sample test
For a selected sample of users, inspect request, approver authority, role mapping, provisioning timestamp, and evidence of business need. For leavers, compare HR termination date with disablement timestamp and policy SLA. For UAR, inspect reviewer, population, review date, challenge, and closure of removals.
