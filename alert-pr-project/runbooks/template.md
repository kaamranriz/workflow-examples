# Runbook Template

## Alert Name
**Alert:** `AlertName`
**Severity:** critical | warning | info
**Team:** @team-oncall

---

## Overview
Brief description of what this alert means and why it fires.

---

## Impact
What is the customer or business impact when this alert fires?

---

## Investigation Steps

### 1. Verify the alert
```bash
# Example: check current metric value
curl -s 'http://prometheus:9090/api/v1/query?query=your_metric_here'
```

### 2. Check service health
```bash
kubectl get pods -n production -l app=service-name
kubectl logs -n production -l app=service-name --tail=100
```

### 3. Check dependencies
List downstream services and how to verify their health.

### 4. Check recent changes
```bash
kubectl rollout history deployment/service-name -n production
git log --oneline -10 -- path/to/service
```

---

## Mitigation Steps

### Immediate Mitigation
1. Step 1
2. Step 2
3. Step 3

### Rollback (if needed)
```bash
kubectl rollout undo deployment/service-name -n production
```

---

## Escalation

### When to escalate
- Condition 1
- Condition 2

### Escalation contacts
- **Primary:** @primary-contact
- **Secondary:** @secondary-contact
- **Manager:** @manager-contact

---

## Related Resources
- Dashboard: [Grafana Dashboard](https://grafana.techcorp.io/d/dashboard-id)
- Logs: [Kibana Query](https://kibana.techcorp.io/...)
- Architecture Doc: [Confluence Link](https://confluence.techcorp.io/...)

---

## Post-Incident
After resolving:
1. Document what happened in #incidents channel
2. Create follow-up tickets for root cause fix
3. Update this runbook if needed


