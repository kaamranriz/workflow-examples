# TechCorp Alert Repository

This is a simulated production alerts repository for **TechCorp**, an e-commerce platform. It demonstrates a realistic SRE team environment for testing the **Incident Review → Auto-Generated Alert PRs** workflow.

## Company Context

**TechCorp** runs a microservices-based e-commerce platform with:
- **API Gateway** - Routes all external traffic
- **User Service** - Authentication, profiles, sessions
- **Payment Service** - Payment processing, transactions
- **Order Service** - Order management, fulfillment
- **Inventory Service** - Stock management
- **Notification Service** - Email, SMS, push notifications

## Team Structure

| Team | Services Owned | On-Call Rotation |
|------|----------------|------------------|
| Platform | api-gateway, infrastructure | @platform-oncall |
| Identity | user-service, auth | @identity-oncall |
| Payments | payment-service, transactions | @payments-oncall |
| Orders | order-service, inventory-service | @orders-oncall |

## Repository Structure

```
alert-pr-project/
├── alerts/                    # Prometheus alert definitions
│   ├── api/                   # API Gateway alerts
│   ├── payments/              # Payment service alerts  
│   ├── infrastructure/        # Infrastructure alerts
│   └── user/                  # User service alerts
├── incident-reviews/          # Weekly incident review documents
├── runbooks/                  # Runbook templates
├── docs/                      # Documentation
└── README.md
```

## Alert Conventions

All alerts in this repository follow these standards:

### Naming
- CamelCase alert names
- Prefix with service name for service-specific alerts
- Suffix with severity for quick identification (e.g., `PaymentLatencyWarning`)

### Labels (Required)
```yaml
labels:
  severity: critical|warning|info
  team: platform|identity|payments|orders
  service: <service-name>
  tier: frontend|backend|database|infrastructure
```

### Annotations (Required)
```yaml
annotations:
  summary: "Brief one-line description"
  description: "Detailed description with {{ $value }} and {{ $labels }}"
  runbook_url: "https://runbooks.techcorp.io/<runbook-id>"
  dashboard_url: "https://grafana.techcorp.io/d/<dashboard-id>"
  slack_channel: "#<team>-alerts"
```

### Severity Guidelines
- **critical**: Customer-facing impact, immediate response required, pages on-call
- **warning**: Degraded performance or approaching limits, respond within 15 minutes
- **info**: Informational, no immediate action needed, review during business hours

## How to Test the Workflow

### Step 1: Use an Incident Review
The `incident-reviews/` folder contains realistic incident review documents with alert gaps identified.

### Step 2: Run the Alert PR Generator Workflow
```
incident_review_file: workflow-examples/alert-pr-project/incident-reviews/week-50-2024.md
team_name: platform
```

### Step 3: Review Generated Alerts
The workflow will:
1. Parse the incident review
2. Extract alert action items
3. Learn patterns from existing alerts in `alerts/`
4. Generate new alert YAML files
5. Create a Pull Request for review

## Metrics Reference

Common metrics used in this repository:
- `http_request_duration_seconds` - Request latency histogram
- `http_requests_total` - Request counter with status labels
- `up` - Target availability
- `container_memory_usage_bytes` - Container memory
- `kube_pod_container_status_restarts_total` - Pod restarts
- `pg_*` - PostgreSQL metrics
- `redis_*` - Redis metrics


