# Multi-Model IaC Generator Workflow Examples

This folder contains example requests for testing the **Multi-Model IaC Generator** workflow template.

## What This Workflow Does
1. Takes an IaC request description and type (kubernetes/nomad) as inputs
2. Generates manifests using 3 different AI models in parallel:
   - GPT-4
   - GPT-4-Turbo
   - GPT-4-Mini
3. Validates each generated manifest
4. Saves all candidates to separate files
5. Creates a side-by-side comparison report
6. Recommends the best option

## Example Requests

### Kubernetes Examples

**1. Simple Web Application:**
```
iac_request: Deploy a Node.js web application with 3 replicas, 512MB memory limit, health checks, and a LoadBalancer service on port 80
iac_type: kubernetes
```

**2. Redis Cache:**
```
iac_request: Deploy a Redis cache with persistent volume, memory limit of 1GB, and a ClusterIP service
iac_type: kubernetes
```

**3. Full-Stack Application:**
```
iac_request: Deploy a full-stack app with a React frontend (2 replicas), Node.js API (3 replicas), and PostgreSQL database with persistent storage
iac_type: kubernetes
```

**4. Microservices with Ingress:**
```
iac_request: Create an Ingress resource that routes /api/* to an API service and /* to a frontend service, with TLS termination using cert-manager
iac_type: kubernetes
```

### Nomad Examples

**1. Simple Batch Job:**
```
iac_request: Create a Nomad job that runs a Python data processing script once a day with 2GB memory
iac_type: nomad
```

**2. Web Service:**
```
iac_request: Deploy a Go web service with 5 instances, Consul service discovery, and health checks
iac_type: nomad
```

**3. Database Service:**
```
iac_request: Deploy PostgreSQL 15 as a Nomad service with persistent host volumes and environment variables for configuration
iac_type: nomad
```

## Expected Behavior
1. Three AI models generate manifests in parallel
2. Each manifest is validated for syntax and best practices
3. Candidates are saved to:
   - `generated-iac/candidate-1-gpt4-{run_id}.{type}`
   - `generated-iac/candidate-2-gpt4turbo-{run_id}.{type}`
   - `generated-iac/candidate-3-gpt4mini-{run_id}.{type}`
4. Comparison report saved to:
   - `generated-iac/comparison-report-{run_id}.md`
5. Final output includes recommendation and analysis

## Sample Output Structure

The comparison report will include:
- Executive summary with recommendation
- Side-by-side comparison table
- Validation scores for each candidate
- Pros and cons analysis
- Specific differences highlighted
- File locations for all generated files


