# Test Cases: Student Marks Matrix Analysis

These are manual test cases for `main.py`. Use the inputs in order when prompted. Expected output may include formatting and prompts that are not repeated here.

| Test ID | Input | Scenario | Expected result |
|---|---|---|---|
| TC01 | 2 students; 2 subjects; marks 80,90,70,80 | Normal matrix | Student averages 85 and 75; subject averages 75 and 85 |
| TC02 | 1 student; 1 subject; mark 100 | Single value | Total 100; average 100; subject average 100 |
| TC03 | 0 students | Invalid student count | Enter positive counts |
| TC04 | 2 students; 0 subjects | Invalid subject count | Enter positive counts |

## Test Notes
- Run each test in Python 3 using `python main.py`.
- Compare the actual output with the expected result.
- Some case studies are simplified learning examples; limitations are noted where relevant.
