# Student Marks Matrix Analysis

## Problem statement
Store student marks in a nested list and calculate each student's and each subject's average.

## Objectives
- Practise basic Python programming and problem solving.
- Accept input, process values, and display results.
- Use validation, conditions, loops, and calculations where appropriate.

## Assumptions
Numeric marks are entered; score ranges are not validated.

## Algorithm
Read counts, validate positive counts, collect matrix with nested loops, print row averages and subject averages.

## Flowchart
See [flowchart.md](flowchart.md) for the flowchart.

## Pseudocode
```text
READ students, subjects
IF counts invalid: PRINT error
ELSE collect marks matrix
FOR each student row: PRINT row and average
FOR each subject column: calculate and PRINT average
```

## Python source code
The runnable source is in [main.py](main.py).

## Test cases
See [test_cases.md](test_cases.md) for normal and boundary test cases.

## Output screenshots
See the [screenshots folder](screenshots/) for the sample-run image. These are illustrative sample console images, not photographs of an actual terminal session.

## Conclusion
This case study demonstrates how a real-world task can be represented as an algorithm and implemented in Python. Running the program with valid and invalid inputs helps practise logic, testing, and interpreting output.
