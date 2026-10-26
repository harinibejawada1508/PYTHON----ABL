# Calendar Generator

## Problem statement
Display the calendar for a selected month and year.

## Objectives
- Practise basic Python programming and problem solving.
- Accept input, process values, and display results.
- Use validation, conditions, loops, and calculations where appropriate.

## Assumptions
Year and month are integers; Python calendar module is available.

## Algorithm
Read year and month, validate ranges, and print the month calendar.

## Flowchart
See [flowchart.md](flowchart.md) for the flowchart.

## Pseudocode
```text
IMPORT calendar; READ year, month
IF year < 1 OR month not in 1..12: PRINT invalid
ELSE PRINT calendar.month(year, month)
```

## Python source code
The runnable source is in [main.py](main.py).

## Test cases
See [test_cases.md](test_cases.md) for normal and boundary test cases.

## Output screenshots
See the [screenshots folder](screenshots/) for the sample-run image. These are illustrative sample console images, not photographs of an actual terminal session.

## Conclusion
This case study demonstrates how a real-world task can be represented as an algorithm and implemented in Python. Running the program with valid and invalid inputs helps practise logic, testing, and interpreting output.
