# AI Code Review with Approval Workflow Examples

This folder contains example files for testing the **AI Code Review with Approval** workflow template.

## What This Workflow Does
1. Takes a file path as input
2. Reads the file content
3. Uses AI to analyze code quality, readability, performance, and best practices
4. Generates an improved version of the code
5. Proposes changes for human approval

## Example Files

### 1. `legacy_user_service.py`
A legacy user service with multiple code quality issues:

**Issues to find:**
- ❌ Global mutable state (`users` dictionary)
- ❌ Insecure password hashing (MD5)
- ❌ Missing docstrings and type hints
- ❌ Poor variable names (`h`, `e`, `q`, `s`)
- ❌ No input validation
- ❌ Security issues (returning passwords in `getAllUsers`)
- ❌ Inconsistent naming conventions (camelCase vs snake_case)
- ❌ Missing error handling

**To test:**
```
Input: workflow-examples/code-review/legacy_user_service.py
```

### 2. `api_client.py`
An API client with security and performance issues:

**Issues to find:**
- ❌ Hardcoded API key
- ❌ Bare `except` clause (catches all exceptions)
- ❌ No rate limiting on bulk operations
- ❌ Fixed retry delay (no exponential backoff)
- ❌ Cache with no expiration
- ❌ Missing type hints and docstrings
- ❌ Synchronous bulk fetching (slow)

**To test:**
```
Input: workflow-examples/code-review/api_client.py
```

## Expected Behavior
1. AI reads the file
2. Analyzes for code quality issues
3. Generates improved code with:
   - Better naming conventions
   - Type hints
   - Docstrings
   - Proper error handling
   - Security improvements
   - Performance optimizations
4. Proposes changes for approval


