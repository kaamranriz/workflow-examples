# Alert Generator Workflow Examples

This folder contains example files for testing the **Alert Generator** workflow template.

## What This Workflow Does
1. Takes a natural language alert description and alert repo path as inputs
2. Finds existing alert files in the repo
3. Analyzes patterns and conventions from existing alerts
4. Generates a new alert YAML following the same patterns
5. Validates the YAML and PromQL syntax
6. Saves the alert file and creates a review summary

## Example Files

### Sample Alert Repository: `sample-alerts/`
Contains example Prometheus alert files that demonstrate the patterns:

- `api-alerts.yaml` - API service alerts with latency, error rate, and availability checks
- `database-alerts.yaml` - Database alerts with connection count, replication lag, and disk space checks

### Conventions Demonstrated
- **Naming**: CamelCase alert names (e.g., `HighAPILatency`)
- **Severity Levels**: `warning`, `critical`
- **Labels**: `team`, `service`, `severity`, `pagerduty`
- **Annotations**: `summary`, `description`, `runbook_url`, `dashboard_url`
- **Time Thresholds**: `for: 1m`, `for: 5m`, `for: 10m`

## How to Test This Workflow

**Inputs:**
```
alert_description: Create an alert that fires when memory usage on Kubernetes pods exceeds 90% for more than 5 minutes
alert_repo_path: workflow-examples/alert-generator/sample-alerts
```

### More Example Alert Descriptions

1. **CPU Alert:**
```
Create a critical alert for when CPU usage on any production server exceeds 95% for 3 minutes
```

2. **Queue Alert:**
```
Alert when the message queue depth exceeds 10000 messages for more than 2 minutes
```

3. **Certificate Alert:**
```
Warning alert when SSL certificates are expiring within 30 days
```

4. **Redis Alert:**
```
Alert when Redis memory usage is above 80% or when evictions are happening
```

## Expected Behavior
1. Workflow reads existing alerts
2. Extracts naming conventions, labels, annotations
3. Generates new alert following the same patterns
4. Validates YAML syntax and PromQL
5. Saves to `generated-alerts/alert-{run_id}.yaml`
6. Creates a review summary for approval


