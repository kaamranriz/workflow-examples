# Run & Fix Single Test Workflow Examples

This folder contains example files for testing the **Run & Fix Single Test** workflow template.

## What This Workflow Does
1. Takes a source file and test file as inputs
2. Runs the tests to identify failures
3. Uses AI to analyze and fix the failing code
4. Re-runs tests to verify the fix

## Example Files

### Source File: `buggy_shopping_cart.py`
A shopping cart implementation with **5 intentional bugs**:

1. **Bug 1**: `add_to_cart()` doesn't check stock availability
2. **Bug 2**: `remove_from_cart()` has an off-by-one error
3. **Bug 3**: `get_cart_total()` doesn't multiply by quantity
4. **Bug 4**: `get_item_count()` returns unique products instead of total items
5. **Bug 5**: `apply_discount()` adds discount instead of subtracting

### Test File: `test_shopping_cart.py`
Comprehensive test suite with 14 test cases that will expose the bugs.

## How to Test This Workflow

**Inputs:**
```
source_file: workflow-examples/single-test-fix/buggy_shopping_cart.py
test_file: workflow-examples/single-test-fix/test_shopping_cart.py
```

## Expected Behavior
1. Run the tests (expect ~6 failures)
2. AI analyzes the failures and source code
3. AI generates fixes for all 5 bugs
4. Re-run tests (should all pass)
5. Return success with fixed code

## To Run Tests Manually
```bash
cd workflow-examples/single-test-fix
pytest test_shopping_cart.py -v
```


