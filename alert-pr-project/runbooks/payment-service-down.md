# Runbook: PaymentServiceDown

## Alert Name
**Alert:** `PaymentServiceDown`
**Severity:** critical
**Team:** @payments-oncall
**PagerDuty:** Yes

---

## Overview
This alert fires when the payment-service is unreachable by Prometheus. This indicates a complete outage of payment processing capability.

---

## Impact
**Customer Impact:** CRITICAL
- All payment attempts will fail
- Checkout is completely blocked
- Revenue loss is immediate and ongoing

**Typical Duration:** Usually resolved within 5-15 minutes if pods are simply crashing.

---

## Investigation Steps

### 1. Check pod status
```bash
kubectl get pods -n production -l app=payment-service
kubectl describe pod -n production -l app=payment-service
```

Look for:
- CrashLoopBackOff
- OOMKilled
- ImagePullBackOff
- Pending state

### 2. Check recent events
```bash
kubectl get events -n production --sort-by='.lastTimestamp' | grep payment
```

### 3. Check logs
```bash
kubectl logs -n production -l app=payment-service --tail=200 --previous
kubectl logs -n production -l app=payment-service --tail=200
```

### 4. Check node health
```bash
kubectl get nodes
kubectl describe node <node-name-where-pods-run>
```

### 5. Check database connectivity
```bash
kubectl exec -n production deployment/payment-service -- nc -zv payment-db.techcorp.io 5432
```

---

## Mitigation Steps

### Restart pods (if not auto-recovering)
```bash
kubectl rollout restart deployment/payment-service -n production
```

### Scale up (if capacity issue)
```bash
kubectl scale deployment/payment-service -n production --replicas=5
```

### Rollback recent deployment
```bash
kubectl rollout history deployment/payment-service -n production
kubectl rollout undo deployment/payment-service -n production
```

### Database failover (if DB issue)
See: [PostgreSQL Failover Runbook](./postgresql-failover.md)

---

## Escalation

### Escalate immediately if:
- Service doesn't recover after rollback
- Database appears to be the issue
- More than 10 minutes of outage

### Escalation contacts
- **Primary:** @payments-oncall (PagerDuty)
- **Secondary:** @payments-lead
- **Database:** @platform-oncall
- **VP Eng:** @vp-engineering (after 15 min outage)

---

## Related Resources
- Dashboard: [Payment Service Overview](https://grafana.techcorp.io/d/payment-service-overview)
- Logs: [Payment Service Logs](https://kibana.techcorp.io/app/discover#/?_g=()&_a=(query:(match:(kubernetes.labels.app:'payment-service'))))
- Architecture: [Payment Service Architecture](https://confluence.techcorp.io/display/ENG/Payment+Service)

---

## Post-Incident
1. Post update in #incident-payment channel
2. Create JIRA ticket for root cause analysis
3. Schedule post-mortem if outage > 5 minutes


