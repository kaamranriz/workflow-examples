# Workflow Template Examples

This folder contains test examples for the non-gaming workflow templates. Each subfolder contains files and documentation for testing a specific workflow.

## Template Overview

| Template | Folder | Description |
|----------|--------|-------------|
| **Test Generator** | `test-generator/` | Generate tests for any source file |
| **Run & Fix Single Test** | `single-test-fix/` | Run tests and auto-fix failures |
| **AI Code Review** | `code-review/` | Review code and propose improvements |
| **API Interface Sync** | `api-sync/` | Sync interface changes across codebase |
| **Alert Generator** | `alert-generator/` | Generate Prometheus alerts from descriptions |
| **Multi-Model IaC** | `multi-model-iac/` | Generate IaC with multiple AI models |
| **Alert PR Generator** | `alert-pr-generator/` | Generate alerts from incident reviews |

---

## Quick Start Examples

### 1. Test Generator
```
file_path: workflow-examples/test-generator/calculator.py
```
Generates unit tests for a calculator module with arithmetic operations.

### 2. Run & Fix Single Test
```
source_file: workflow-examples/single-test-fix/buggy_shopping_cart.py
test_file: workflow-examples/single-test-fix/test_shopping_cart.py
```
Finds and fixes 5 intentional bugs in a shopping cart implementation.

### 3. AI Code Review
```
file_path: workflow-examples/code-review/legacy_user_service.py
```
Reviews legacy code with security issues, poor naming, and missing docs.

### 4. API Interface Sync
```
base_branch: main
```
(Requires a feature branch with interface changes)

### 5. Alert Generator
```
alert_description: Create an alert for when CPU usage exceeds 90% for 5 minutes
alert_repo_path: workflow-examples/alert-generator/sample-alerts
```
Learns patterns from existing alerts and generates new ones.

### 6. Multi-Model IaC Generator
```
iac_request: Deploy a Redis cache with 1GB memory and persistent storage
iac_type: kubernetes
```
Generates manifests using GPT-4, GPT-4-Turbo, and GPT-4-Mini in parallel.

### 7. Alert PR Generator
```
incident_review_file: workflow-examples/alert-pr-generator/incident-review-2024-001.md
team_name: payments
```
Extracts alert action items from incident reviews and creates a PR.

---

## Folder Structure

```
workflow-examples/
├── README.md                          # This file
├── test-generator/
│   ├── calculator.py                  # Source file with math functions
│   ├── string_utils.py                # Source file with string utilities
│   └── README.md
├── single-test-fix/
│   ├── buggy_shopping_cart.py         # Source file with 5 bugs
│   ├── test_shopping_cart.py          # Test file (will fail initially)
│   └── README.md
├── code-review/
│   ├── legacy_user_service.py         # Code with quality issues
│   ├── api_client.py                  # Code with security issues
│   └── README.md
├── api-sync/
│   └── README.md                      # Instructions only (needs git branches)
├── alert-generator/
│   ├── sample-alerts/
│   │   ├── api-alerts.yaml            # Example Prometheus alerts
│   │   └── database-alerts.yaml       # More example alerts
│   └── README.md
├── multi-model-iac/
│   └── README.md                      # Example IaC requests
└── alert-pr-generator/
    ├── incident-review-2024-001.md    # Payment service outage
    ├── incident-review-2024-002.md    # Memory leak incident
    └── README.md
```

---

## Notes

- **Test Generator** and **Run & Fix Single Test** require Python with pytest installed
- **Alert Generator** and **Alert PR Generator** require the runner to have alert tools available
- **Multi-Model IaC** uses multiple AI models and may have higher API costs
- **API Interface Sync** requires an actual git repository with branches
- All file paths are relative to the repository root


