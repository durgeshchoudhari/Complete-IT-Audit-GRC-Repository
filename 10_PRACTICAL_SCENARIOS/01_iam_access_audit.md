# Scenario 1 — IAM / User Access Review

**Business context:** A fictional finance application contains payroll and accounts-payable data.

**Risk:** Unauthorized or excessive access may result in inappropriate viewing, modification, or approval of financial data.

**Control objective:** Access is approved, appropriate to job responsibilities, reviewed periodically, and removed within defined SLA after termination.

**Evidence:** HR population, IAM account export, access requests, role matrix, approval trail, UAR certification, removal logs, privileged account list.

**Test approach:** Validate the population; compare terminated employees to enabled accounts; sample provisioning and role changes; inspect reviewer challenge and closure; examine privileged access.

**Scenario questions**
1. What would you request first and why?
2. How would you prove the HR and IAM populations are complete?
3. What if the manager approved access after provisioning?
4. How do you test least privilege?
5. What if the reviewer certified all access without challenge?
6. How would you assess a terminated user who still has access?
7. What compensating controls might reduce risk, and what evidence would prove they operate?

**Expected answer structure:** risk → control → population → sample → evidence → exception → validation → conclusion.
