# Test Cases: Calendar Generator

These are manual test cases for `main.py`. Use the inputs in order when prompted. Expected output may include formatting and prompts that are not repeated here.

| Test ID | Input | Scenario | Expected result |
|---|---|---|---|
| TC01 | 2026; 10 | Valid month/year | Prints October 2026 calendar |
| TC02 | 2024; 2 | Leap year February | Prints February 2024 with 29 days |
| TC03 | 2026; 13 | Invalid month | Please enter a valid year and month |
| TC04 | 0; 1 | Invalid year | Please enter a valid year and month |
| TC05 | 2026; 1 | January | Prints January 2026 calendar |

## Test Notes
- Run each test in Python 3 using `python main.py`.
- Compare the actual output with the expected result.
- Some case studies are simplified learning examples; limitations are noted where relevant.
