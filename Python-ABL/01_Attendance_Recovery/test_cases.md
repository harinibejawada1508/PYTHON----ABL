# Test Cases: Attendance Recovery Computation

These are manual test cases for `main.py`. Use the inputs in order when prompted. Expected output may include formatting and prompts that are not repeated here.

| Test ID | Input | Scenario | Expected result |
|---|---|---|---|
| TC01 | 60 | 100 | Valid, below 75% |
| TC02 | 75 | 100 | Exactly 75% |
| TC03 | 80 | 100 | Above 75% |
| TC04 | 10 | 0 | Zero classes conducted |
| TC05 | 101 | 100 | Attended exceeds conducted |
| TC06 | -1 | 100 | Negative attended classes |

## Test Notes
- Run each test in Python 3 using `python main.py`.
- Compare the actual output with the expected result.
- Some case studies are simplified learning examples; limitations are noted where relevant.
