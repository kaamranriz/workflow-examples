# Incident Review: Memory Leak in User Service - 2024-002

## Incident Summary
**Date:** December 20, 2024
**Duration:** 2 hours
**Severity:** P2
**Services Affected:** user-service

## Timeline
- 09:00 - Automated restart of user-service pods detected
- 09:30 - Engineering investigation started
- 10:00 - Memory leak identified in user session handling
- 10:45 - Hotfix deployed
- 11:00 - Service stable

## Root Cause
A memory leak in the user session handling code caused user-service pods to OOM (Out of Memory) after approximately 4 hours of runtime. The Kubernetes liveness probe correctly restarted the pods, but this caused brief service interruptions.

## Impact
- 15 pod restarts over 2 hours
- Brief authentication failures during restarts
- No data loss

## Action Items

### Alert Improvements Needed

1. **Add alert for memory growth rate**
   - Alert when memory usage grows more than 20% per hour
   - Service: user-service
   - Severity: warning
   - Team: identity

2. **Add alert for pod restart frequency**
   - Alert when more than 3 pod restarts occur in 30 minutes
   - Service: all
   - Severity: warning
   - Team: platform

3. **Add alert for OOMKilled events**
   - Alert immediately when any pod is OOMKilled
   - Service: all
   - Severity: critical
   - Team: platform

4. **Add alert for authentication failure rate**
   - Alert when auth failure rate exceeds 5% for 2 minutes
   - Service: user-service
   - Severity: critical
   - Team: identity

### Code Improvements
- Fix memory leak in session handling
- Add memory profiling to CI pipeline

### Infrastructure Improvements
- Increase memory limits for user-service from 512MB to 1GB
- Add memory usage to Grafana dashboard

## Attendees
- Mike Chen (Incident Commander)
- Sarah Lee (User Service Owner)
- Tom Brown (Platform Engineer)


