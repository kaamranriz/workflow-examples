# Alert PR Generator Workflow Examples

This folder contains example files for testing the **Alert PR Generator** workflow template.

## What This Workflow Does
1. Takes an incident review file and optional team name as inputs
2. Parses the incident review to extract alert action items
3. Generates Prometheus alert definitions for each action item
4. Writes alert files to the repository
5. Creates a PR summary
6. Creates a GitHub Pull Request with the new alerts

## Example Files

### Incident Review 1: `incident-review-2024-001.md`
**Incident:** API Outage - Payment service database connection pool exhaustion

**Alert Actions Extracted:**
1. Database connection pool utilization alert (warning)
2. High 503 error rate alert (critical)
3. Payment processing latency alert (warning)

**To test:**
```
incident_review_file: workflow-examples/alert-pr-generator/incident-review-2024-001.md
team_name: payments
```

### Incident Review 2: `incident-review-2024-002.md`
**Incident:** Memory Leak in User Service

**Alert Actions Extracted:**
1. Memory growth rate alert (warning)
2. Pod restart frequency alert (warning)
3. OOMKilled events alert (critical)
4. Authentication failure rate alert (critical)

**To test:**
```
incident_review_file: workflow-examples/alert-pr-generator/incident-review-2024-002.md
team_name: identity
```

## Expected Behavior
1. Parse the incident review markdown file
2. Extract all "Alert Improvements Needed" items
3. Generate Prometheus-compatible YAML alerts for each
4. Group alerts by service
5. Create alert files in `alerts/` directory
6. Generate PR title and description summarizing the changes
7. Create a GitHub PR (requires GitHub authentication)

## Output Files Created
```
alerts/
├── payment-service-alerts.yaml
├── checkout-api-alerts.yaml
├── user-service-alerts.yaml
└── platform-alerts.yaml
```

## PR Created
- Branch: `alerts/incident-review-updates`
- Base: `main`
- Title: "Add alerts from incident review 2024-001"
- Body: Summary of alerts added with links to incident review


