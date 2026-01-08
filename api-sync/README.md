# Automated Interface & API Sync Workflow Examples

This folder contains instructions for testing the **Automated Interface & API Sync** workflow template.

## What This Workflow Does
1. Takes a base branch as input (e.g., `main`)
2. Compares current branch with base branch to find changes
3. Detects interface/API changes in TypeScript/JavaScript/Python files
4. Uses Cursor to automatically sync dependent code
5. Runs type checking to verify changes
6. Reviews and commits if approved

## How to Test This Workflow

### Prerequisites
1. Make sure you're on a feature branch with some interface changes
2. The base branch should exist (e.g., `main`, `develop`)

### Example Scenario 1: TypeScript Interface Change
Create a branch and modify an interface:

```bash
# Create a test branch
git checkout -b test/interface-change

# Modify an interface (example in this repo)
# In src/types/graphSpec.ts, add a new field to an interface
```

Then run the workflow with:
```
Input: main
```

### Example Scenario 2: Python API Change
```bash
# Create a branch with Python API changes
git checkout -b test/api-change

# Modify a function signature in runner/api/
```

Then run the workflow with:
```
Input: main
```

## Expected Behavior
1. Detect changed files between branches
2. Identify interface/API signature changes
3. Find all files that import/use the changed interfaces
4. Update dependent code automatically
5. Run `npm run check-types` to verify
6. Create a commit with changes if approved

## Notes
- This workflow requires an actual git repository with branches
- The base branch must exist and have commits
- Works best with TypeScript/JavaScript interface changes
- Can also detect Python function signature changes


