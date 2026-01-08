# TechCorp Alert Standards

## Purpose
This document defines the standards for creating and maintaining Prometheus alerts at TechCorp.

---

## Alert Naming Convention

### Format
```
<Service><Condition><Severity>
```

### Examples
- `PaymentServiceDown` - Critical availability alert
- `PaymentProcessingSlowP95` - Warning performance alert
- `APIGatewayHighErrorRate` - Error rate alert
- `PostgreSQLDiskSpaceLow` - Resource alert

### Rules
1. Use CamelCase
2. Start with service/component name
3. Describe the condition clearly
4. Optionally include severity in name for quick identification

---

## Severity Levels

### Critical
- **Response Time:** Immediate (< 5 minutes)
- **PagerDuty:** Yes
- **Examples:**
  - Service is down
  - Data loss risk
  - Revenue impact
  - Customer-facing outage

### Warning
- **Response Time:** < 15 minutes during business hours
- **PagerDuty:** No (Slack notification only)
- **Examples:**
  - Approaching resource limits
  - Elevated error rates (below critical)
  - Performance degradation

### Info
- **Response Time:** Next business day
- **PagerDuty:** No
- **Examples:**
  - Informational metrics
  - Non-urgent anomalies
  - Batch job completions

---

## Required Labels

Every alert MUST have these labels:

```yaml
labels:
  severity: critical|warning|info
  team: platform|identity|payments|orders
  service: <service-name>
  tier: frontend|backend|database|infrastructure
```

### Optional Labels
```yaml
labels:
  pagerduty: enabled     # For critical alerts requiring page
  environment: production|staging
```

---

## Required Annotations

Every alert MUST have these annotations:

```yaml
annotations:
  summary: "Short one-line description"
  description: "Detailed description with context"
  runbook_url: "https://runbooks.techcorp.io/<alert-id>"
  dashboard_url: "https://grafana.techcorp.io/d/<dashboard-id>"
  slack_channel: "#<team>-alerts"
```

### Description Best Practices
- Include current value using `{{ $value }}`
- Include relevant labels using `{{ $labels.label_name }}`
- Use Prometheus template functions: `humanize`, `humanizePercentage`, `humanizeDuration`

---

## Time Thresholds (`for` clause)

### Guidelines
| Alert Type | Typical `for` Value |
|------------|---------------------|
| Service down | 1m |
| High error rate | 2-5m |
| Latency issues | 5m |
| Resource warnings | 5-10m |
| Capacity alerts | 10-30m |

### Anti-Patterns
- `for: 0s` or no `for` clause - causes flapping
- `for: 1h` for critical alerts - too slow
- Different thresholds for similar alerts - inconsistent

---

## PromQL Best Practices

### Rate vs Increase
- Use `rate()` for gauges that reset (counters)
- Use `increase()` when you need absolute counts
- Always specify a time window: `rate(metric[5m])`

### Percentiles
```yaml
histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))
```

### Error Rates
```yaml
sum(rate(http_requests_total{status=~"5.."}[5m])) 
/ sum(rate(http_requests_total[5m]))
```

### Avoiding Gaps
- Use `or vector(0)` for optional metrics
- Consider `absent()` for expected metrics that might disappear

---

## Alert File Organization

```
alerts/
├── api/
│   ├── gateway-alerts.yaml
│   └── rate-limiting-alerts.yaml
├── payments/
│   ├── payment-service-alerts.yaml
│   └── payment-gateway-alerts.yaml
├── infrastructure/
│   ├── kubernetes-alerts.yaml
│   └── database-alerts.yaml
└── user/
    └── user-service-alerts.yaml
```

### Rules
1. One file per service or component
2. Group related alerts in the same file
3. Use descriptive filenames
4. Keep files under 200 lines

---

## Review Checklist

Before merging new alerts:

- [ ] Alert name follows naming convention
- [ ] Severity is appropriate for the condition
- [ ] All required labels are present
- [ ] All required annotations are present
- [ ] Runbook exists at the specified URL
- [ ] Dashboard exists and is linked
- [ ] `for` clause is appropriate
- [ ] PromQL is tested and validated
- [ ] No duplicate alerts
- [ ] Added to appropriate team's alert file


