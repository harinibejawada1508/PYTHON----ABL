# Test Cases: Food Waste Monitoring System

These are manual test cases for `main.py`. Use the inputs in order when prompted. Expected output may include formatting and prompts that are not repeated here.

| Test ID | Input | Scenario | Expected result |
|---|---|---|---|
| TC01 | 3 days; 1,2,3 kg | Average exactly 2 kg | Total 6.00 kg; average 2.00 kg; keep monitoring |
| TC02 | 2 days; 3,3 kg | Average above 2 kg | Total 6.00 kg; average 3.00 kg; suggestion to plan portions |
| TC03 | 1 day; 0 kg | No waste | Total 0.00 kg; average 0.00 kg; keep monitoring |
| TC04 | 1 day; -1 kg | Negative waste | Waste cannot be negative; no totals printed |
| TC05 | 0 days | Invalid day count | Enter a positive number of days |

## Test Notes
- Run each test in Python 3 using `python main.py`.
- Compare the actual output with the expected result.
- Some case studies are simplified learning examples; limitations are noted where relevant.
