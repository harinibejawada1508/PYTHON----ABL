# Electricity Consumption

## Problem statement
Record three electricity readings per day and calculate daily and overall totals and daily average.

## Objectives
- Practise basic Python programming and problem solving.
- Accept input, process values, and display results.
- Use validation, conditions, loops, and calculations where appropriate.

## Assumptions
Exactly three readings per day; negative readings are not rejected by current code.

## Algorithm
Read positive day count, collect three readings per day, total each row, then calculate overall average.

## Flowchart
See [flowchart.md](flowchart.md) for the flowchart.

## Pseudocode
```text
READ days
IF days <= 0: PRINT error
ELSE collect 3 readings per day
FOR each row: calculate daily total
PRINT overall total and total/days average
```

## Python source code
The runnable source is in [main.py](main.py).

## Test cases
See [test_cases.md](test_cases.md) for normal and boundary test cases.

## Output screenshots
See the [screenshots folder](screenshots/) for the sample-run image. These are illustrative sample console images, not photographs of an actual terminal session.

## Conclusion
This case study demonstrates how a real-world task can be represented as an algorithm and implemented in Python. Running the program with valid and invalid inputs helps practise logic, testing, and interpreting output.
