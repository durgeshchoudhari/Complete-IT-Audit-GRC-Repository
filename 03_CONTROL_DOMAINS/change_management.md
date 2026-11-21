# Change Management Audit Program

## Control objective
Only authorized, tested, and appropriately segregated changes are migrated to production, with emergency changes governed by an approved expedited process.

## Test attributes
- Request has unique ticket and business justification.
- Risk/impact assessment is documented.
- Required approval occurred at the stage required by policy.
- Testing/UAT evidence exists and failures are resolved.
- Developer/deployer segregation or approved compensating control exists.
- Production deployment matches approved version and window.
- Emergency classification is justified; retrospective review occurs within policy timeline.
- Failed/rolled-back changes are tracked.

## Red flags
Repeated emergency changes, approvals after the fact without permitted process, same person developing and deploying, no test evidence, direct production access, and incomplete change population.
