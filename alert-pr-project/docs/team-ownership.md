# Team Ownership & Alert Responsibilities

## Team Structure

### Platform Team
**Slack:** #platform-team
**On-Call Rotation:** @platform-oncall
**Manager:** Sarah Chen

**Services Owned:**
- api-gateway
- kubernetes infrastructure
- databases (PostgreSQL, Redis)
- networking/load balancers
- CI/CD pipelines

**Alert Directories:**
- `alerts/api/`
- `alerts/infrastructure/`

---

### Identity Team
**Slack:** #identity-team
**On-Call Rotation:** @identity-oncall
**Manager:** Mike Johnson

**Services Owned:**
- user-service
- authentication/OAuth
- session management
- SSO integrations

**Alert Directories:**
- `alerts/user/`

---

### Payments Team
**Slack:** #payments-team
**On-Call Rotation:** @payments-oncall
**Manager:** Lisa Wang

**Services Owned:**
- payment-service
- payment gateway integrations (Stripe, PayPal)
- transaction processing
- fraud detection

**Alert Directories:**
- `alerts/payments/`

---

### Orders Team
**Slack:** #orders-team
**On-Call Rotation:** @orders-oncall
**Manager:** Tom Brown

**Services Owned:**
- order-service
- inventory-service
- notification-service
- fulfillment integrations

**Alert Directories:**
- `alerts/orders/` (to be created)

---

## On-Call Responsibilities

### During On-Call Shift
1. Respond to PagerDuty alerts within 5 minutes
2. Acknowledge and triage incoming alerts
3. Escalate if unable to resolve within 30 minutes
4. Document incidents in #incidents channel
5. Hand off to next on-call with context

### After Incident
1. Create JIRA ticket for follow-up
2. Update runbooks if procedures changed
3. Propose new alerts if gaps identified
4. Attend weekly incident review

---

## Escalation Matrix

| Severity | Initial Response | Escalation After | Escalate To |
|----------|------------------|------------------|-------------|
| Critical | On-call engineer | 15 minutes | Team lead + manager |
| Warning | On-call engineer | 1 hour | Team lead |
| Info | Next business day | N/A | N/A |

### Executive Escalation
For outages > 30 minutes affecting revenue:
- VP Engineering: @vp-engineering
- CTO: @cto (for P1 > 1 hour)


