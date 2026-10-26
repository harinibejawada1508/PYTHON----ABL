# Numeric Diamond Pattern

## Problem statement
Print an increasing numeric triangle followed by a decreasing triangle.

## Objectives
- Practise basic Python programming and problem solving.
- Accept input, process values, and display results.
- Use validation, conditions, loops, and calculations where appropriate.

## Assumptions
Input is an integer row count.

## Algorithm
Reject non-positive rows. Print rows 1..n and then n-1..1 with leading spaces.

## Flowchart
See [flowchart.md](flowchart.md) for the flowchart.

## Pseudocode
```text
READ n
IF n <= 0: PRINT error
ELSE FOR i = 1 TO n: PRINT spaces and numbers 1..i
FOR i = n-1 DOWNTO 1: PRINT spaces and numbers 1..i
```

## Python source code
The runnable source is in [main.py](main.py).

## Test cases
See [test_cases.md](test_cases.md) for normal and boundary test cases.

## Output screenshots
See the [screenshots folder](screenshots/) for the sample-run image. These are illustrative sample console images, not photographs of an actual terminal session.

## Conclusion
This case study demonstrates how a real-world task can be represented as an algorithm and implemented in Python. Running the program with valid and invalid inputs helps practise logic, testing, and interpreting output.
