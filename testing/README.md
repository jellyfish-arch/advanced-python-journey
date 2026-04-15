# 🧪 Testing in Python

Testing is the backbone of reliable software development. This module covers essential techniques for verifying code correctness using both the standard library (`unittest`) and the industry-standard `pytest` framework.

## 📁 Testing Programs

| #  | File | Topic | Key Concepts |
|----|------|-------|--------------|
| 01 | `01_unittest_basics.py` | Unittest Basics | `TestCase` classes, standard assertions, test runners |
| 02 | `02_pytest_intro.py` | Pytest Introduction | Minimalist syntax, plain `assert` statements, functional tests |
| 03 | `03_pytest_parametrize.py` | Pytest Parametrization | Data-driven testing, reducing boilerplate with `@pytest.mark` |
| 04 | `04_pytest_fixtures.py` | Pytest Fixtures | Setup/Teardown logic, reusable state, temporary resources |
| 05 | `05_mocking_api.py` | Mocking External APIs | `unittest.mock`, side effects, return values, patch decorators |
| 06 | `06_testing_exceptions.py` | Testing Exceptions | Asserting failures, `assertRaises`, `pytest.raises` |
| 07 | `07_class_based_tests.py` | Class-Based Testing | Organizing complex test suites, setup/teardown methods |
| 08 | `08_edge_cases_validation.py` | Edge Cases & Validation | Boundary testing, complex logic verification, error messages |

## 🚀 How to Run

### Using Standard Python
Most scripts can be run directly:
```bash
python testing/01_unittest_basics.py
```

### Using Pytest (Recommended)
For the best experience, run all tests in the folder using `pytest`:
```bash
pytest testing/
```

> [!TIP]
> Use `pytest -v` for verbose output or `pytest -s` to see `print()` statements during test execution.

## 📌 Why Testing Matters
1. **Prevents Regressions:** Ensures new changes don't break existing functionality.
2. **Improves Design:** Testable code is naturally more modular and clean.
3. **Documentation:** Tests serve as an executable specification of how code should behave.
4. **Confidence:** Deploy with the certainty that your logic is sound.