# Attendance Recovery

## Problem statement
Validate attended and total classes; calculate percentage; if below 75%, count extra attended classes until threshold is reached.

## Objectives
- Practise basic Python programming and problem solving.
- Accept input, process values, and display results.
- Use validation, conditions, loops, and calculations where appropriate.

## Assumptions
Assume all future classes are attended.

## Algorithm
Read attended and conducted. If invalid, show error. Otherwise calculate percentage. If below 75%, loop until ratio reaches 0.75.

## Flowchart
See [flowchart.md](flowchart.md) for the flowchart.

## Pseudocode
```text
READ attended, conducted
IF conducted <= 0 OR attended < 0 OR attended > conducted: PRINT invalid
ELSE: percentage = attended / conducted * 100; PRINT percentage
IF percentage < 75: required = 0; WHILE (attended+required)/(conducted+required) < 0.75: required += 1; PRINT required
ELSE: PRINT requirement satisfied
```

## Python source code
The runnable source is in [main.py](main.py).

## Test cases
See [test_cases.md](test_cases.md) for normal and boundary test cases.

## Output screenshots
See the [screenshots folder](screenshots/) for the sample-run image. These are illustrative sample console images, not photographs of an actual terminal session.

## Conclusion
This case study demonstrates how a real-world task can be represented as an algorithm and implemented in Python. Running the program with valid and invalid inputs helps practise logic, testing, and interpreting output.
