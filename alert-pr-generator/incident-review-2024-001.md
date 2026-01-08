# Incident Review: API Outage - 2024-001

## Incident Summary
**Date:** December 15, 2024
**Duration:** 45 minutes
**Severity:** P1
**Services Affected:** payment-service, checkout-api

## Timeline
- 14:00 - First customer reports of failed payments
- 14:05 - Engineering notified via customer support
- 14:15 - Root cause identified: payment-service database connection pool exhausted
- 14:30 - Mitigation applied: increased connection pool size
- 14:45 - Service fully restored

## Root Cause
The payment-service database connection pool was set to 10 connections, which was insufficient during a traffic spike. The connection pool exhaustion caused the service to return 503 errors for all payment requests.

## Impact
- ~2,500 failed payment attempts
- Estimated revenue impact: $125,000
- Customer trust impact: High

## Action Items

### Alert Improvements Needed

1. **Add alert for database connection pool utilization**
   - Alert when connection pool usage exceeds 80% for more than 2 minutes
   - Service: payment-service
   - Severity: warning
   - Team: payments

2. **Add alert for high 503 error rate**
   - Alert when 503 error rate exceeds 1% for more than 1 minute
   - Service: payment-service, checkout-api
   - Severity: critical
   - Team: payments

3. **Add alert for payment processing latency**
   - Alert when p95 latency exceeds 2 seconds for more than 3 minutes
   - Service: payment-service
   - Severity: warning
   - Team: payments

### Infrastructure Improvements
- Increase default connection pool size to 50
- Add auto-scaling for payment-service based on connection pool metrics

### Process Improvements
- Add connection pool utilization to daily metrics review
- Create runbook for connection pool exhaustion scenarios

## Attendees
- Jane Smith (Incident Commander)
- Bob Johnson (Payment Service Owner)
- Alice Williams (SRE)


