# Test Cases: Weekly Electricity Consumption Matrix

These are manual test cases for `main.py`. Use the inputs in order when prompted. Expected output may include formatting and prompts that are not repeated here.

| Test ID | Input | Scenario | Expected result |
|---|---|---|---|
| TC01 | 1 day; readings 1.2, 0.8, 1.0 | One-day total | Daily total 3.00 kWh; total 3.00; average 3.00 |
| TC02 | 2 days; readings 1,1,1 and 2,2,2 | Multiple days | Daily totals 3.00 and 6.00; overall 9.00; average 4.50 |
| TC03 | 0 days | Invalid day count | Enter a positive number of days |
| TC04 | 1 day; readings -1, 2, 3 | Negative reading (current program does not validate this) | Calculates with negative value; consider adding validation |

## Test Notes
- Run each test in Python 3 using `python main.py`.
- Compare the actual output with the expected result.
- Some case studies are simplified learning examples; limitations are noted where relevant.
