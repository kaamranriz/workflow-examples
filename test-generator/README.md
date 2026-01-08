# Test Generator Workflow Examples

This folder contains example source files for testing the **Test Generator** workflow template.

## What This Workflow Does
1. Takes a source file path as input
2. Uses AI to generate comprehensive test files
3. Runs the generated tests with auto-fix capability

## Example Files

### 1. `calculator.py`
A simple calculator module with:
- `Calculator` class with basic arithmetic operations (add, subtract, multiply, divide, power)
- History tracking functionality
- Standalone functions: `factorial`, `fibonacci`, `is_prime`

**To test this workflow:**
```
Input: workflow-examples/test-generator/calculator.py
```

### 2. `string_utils.py`
String manipulation utilities with:
- Functions: `reverse_string`, `is_palindrome`, `count_words`, `capitalize_words`, `truncate`, etc.
- `TextAnalyzer` class for text statistics

**To test this workflow:**
```
Input: workflow-examples/test-generator/string_utils.py
```

## Expected Behavior
The workflow should:
1. Read the source file
2. Generate a test file (e.g., `test_calculator.py`)
3. Run the tests using pytest
4. Auto-fix any failing tests (up to 2 iterations)
5. Return the test results


