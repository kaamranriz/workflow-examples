# How to Test the Alert PR Generator Workflow

This project is designed to test the **Incident Review → Auto-Generated Alert PRs** workflow.

---

## The Use Case

> During your weekly incident reviews, you often identify missing or insufficient alerts, but the follow-up work typically lands in the backlog. This workflow automates the creation of alerts from those reviews.

---

## What This Workflow Does

1. **Reads** your incident review notes (Markdown file)
2. **Extracts** alert-related action items
3. **Learns** patterns from existing alerts in your repository
4. **Generates** valid YAML + PromQL alert definitions
5. **Validates** syntax and metadata fields
6. **Creates** a Pull Request for review

---

## Quick Start

### Test with Week 50 Incident Review

This incident review contains **9 alert action items** from 3 incidents:

```
incident_review_file: workflow-examples/alert-pr-project/incident-reviews/week-50-2024.md
team_name: platform
```

**Expected Alerts Generated:**
1. Payment-service database connection pool warning (> 70%)
2. Payment-service database connection pool critical (> 90%)
3. Payment-service 503 error spike
4. Order-service memory growth rate
5. Order-service high memory utilization
6. Order-service OOMKilled events
7. API Gateway sudden traffic increase
8. API Gateway request queue depth
9. API Gateway latency threshold update

---

### Test with Week 49 Incident Review

This incident review contains **7 alert action items**:

```
incident_review_file: workflow-examples/alert-pr-project/incident-reviews/week-49-2024.md
team_name: identity
```

**Expected Alerts Generated:**
1. Session Redis memory warning (> 75%)
2. Session Redis evictions rate
3. Redis Sentinel failover events
4. Abnormal login rate spike
5. Inventory-service query latency
6. Inventory-service connection wait time
7. Order→Inventory dependency latency

---

### Test with Week 48 Incident Review

This incident review contains **8 alert action items** (Black Friday week):

```
incident_review_file: workflow-examples/alert-pr-project/incident-reviews/week-48-2024.md
team_name: platform
```

**Expected Alerts Generated:**
1. TLS certificate expiring in 30 days
2. TLS certificate expiring in 7 days
3. TLS certificate expired
4. SSL handshake failures
5. Kafka consumer lag warning (> 10k)
6. Kafka consumer lag critical (> 100k)
7. Email delivery latency
8. Kafka consumer offline

---

## What the Workflow Should Learn

The existing alerts in `alerts/` demonstrate these patterns:

### Naming Convention
```
CamelCase with ServiceConditionSeverity pattern
Examples: APIGatewayHighLatencyP95, PaymentServiceDown
```

### Required Labels
```yaml
labels:
  severity: critical|warning
  team: platform|identity|payments|orders
  service: <service-name>
  tier: frontend|backend|database|infrastructure
```

### Required Annotations
```yaml
annotations:
  summary: "Brief description"
  description: "Detailed with {{ $value }} and {{ $labels }}"
  runbook_url: "https://runbooks.techcorp.io/..."
  dashboard_url: "https://grafana.techcorp.io/d/..."
  slack_channel: "#team-alerts"
```

### Time Windows
- Availability alerts: `for: 1m`
- Error rate alerts: `for: 2-5m`
- Resource alerts: `for: 5-10m`

---

## Project Structure

```
alert-pr-project/
├── README.md                      # Project context
├── HOW_TO_TEST.md                 # This file
│
├── alerts/                        # Existing alerts (patterns to learn)
│   ├── api/
│   │   ├── gateway-alerts.yaml    # 5 alerts
│   │   └── rate-limiting-alerts.yaml  # 3 alerts
│   ├── payments/
│   │   ├── payment-service-alerts.yaml  # 6 alerts
│   │   └── payment-gateway-alerts.yaml  # 3 alerts
│   ├── infrastructure/
│   │   ├── kubernetes-alerts.yaml  # 5 alerts
│   │   └── database-alerts.yaml    # 6 alerts
│   └── user/
│       └── user-service-alerts.yaml  # 6 alerts
│
├── incident-reviews/              # Input documents
│   ├── week-50-2024.md            # 9 alert action items
│   ├── week-49-2024.md            # 7 alert action items
│   └── week-48-2024.md            # 8 alert action items
│
├── runbooks/                      # Referenced runbooks
│   ├── template.md
│   └── payment-service-down.md
│
└── docs/                          # Standards documentation
    ├── alert-standards.md
    └── team-ownership.md
```

---

## Expected Workflow Output

### Generated Alert Example

Based on Week 50's incident, the workflow should generate something like:

```yaml
groups:
  - name: payment-service.database
    rules:
      - alert: PaymentDBConnectionPoolWarning
        expr: |
          sum(pg_stat_activity_count{job="payment-service-db"}) 
          / sum(pg_settings_max_connections{job="payment-service-db"}) > 0.70
        for: 2m
        labels:
          severity: warning
          team: payments
          service: payment-service
          tier: database
        annotations:
          summary: "Payment service database connection pool above 70%"
          description: "Connection pool utilization is {{ $value | humanizePercentage }}. Consider scaling or investigating query patterns."
          runbook_url: "https://runbooks.techcorp.io/payment-service/connection-pool"
          dashboard_url: "https://grafana.techcorp.io/d/payment-service-db"
          slack_channel: "#payments-alerts"
```

### PR Created
- **Branch:** `alerts/incident-review-week-50-2024`
- **Title:** `Add 9 alerts from Week 50 Incident Review`
- **Files Changed:**
  - `alerts/payments/payment-service-alerts.yaml` (3 new alerts)
  - `alerts/orders/order-service-alerts.yaml` (new file, 3 alerts)
  - `alerts/api/gateway-alerts.yaml` (3 new alerts)

---

## Validation Checks

The workflow should validate:

1. ✅ YAML syntax is valid
2. ✅ PromQL queries are syntactically correct
3. ✅ All required labels present
4. ✅ All required annotations present
5. ✅ Alert names follow naming convention
6. ✅ Severity matches the condition described
7. ✅ Time thresholds are reasonable

---

## Success Criteria

The workflow succeeds if it:

1. ✅ Parses all alert action items from the incident review
2. ✅ Generates alerts matching the existing patterns
3. ✅ Creates valid YAML files
4. ✅ Groups alerts by service appropriately
5. ✅ Produces a clear PR summary
6. ✅ No manual intervention required for basic alerts


