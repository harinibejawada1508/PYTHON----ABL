# Test Cases: Multi-Day Water Tank Simulation

These are manual test cases for `main.py`. Use the inputs in order when prompted. Expected output may include formatting and prompts that are not repeated here.

| Test ID | Input | Scenario | Expected result |
|---|---|---|---|
| TC01 | 1 day; capacity 100; start 50; add 20; use 15 | Valid normal operation | End of day 1: 55.00 litres |
| TC02 | 1 day; capacity 100; start 90; add 30; use 10 | Added amount exceeds capacity | Water capped at 100 then usage gives 90.00 litres |
| TC03 | 1 day; capacity 100; start 10; add 0; use 20 | Usage exceeds available water | End of day 1: 0.00 litres |
| TC04 | 1 day; capacity 100; start 50; add -1; use 2 | Negative added amount | Negative amounts are not allowed; simulation stops |
| TC05 | 0 days | Invalid day count | Invalid tank details |

## Test Notes
- Run each test in Python 3 using `python main.py`.
- Compare the actual output with the expected result.
- Some case studies are simplified learning examples; limitations are noted where relevant.
