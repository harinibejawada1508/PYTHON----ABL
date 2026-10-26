# Food Waste Monitoring

## Problem statement
Calculate total and average daily food waste and show a suggestion based on average.

## Objectives
- Practise basic Python programming and problem solving.
- Accept input, process values, and display results.
- Use validation, conditions, loops, and calculations where appropriate.

## Assumptions
Values are kilograms; negative entries are treated as zero.

## Algorithm
Read positive days, collect daily waste, replace negative values with zero, calculate total and average, then show advice.

## Flowchart
See [flowchart.md](flowchart.md) for the flowchart.

## Pseudocode
```text
READ days
IF days <= 0: PRINT error
ELSE FOR each day: READ waste; IF negative set zero; add to total
average = total/days; PRINT total and average
IF average > 2: suggest review portions; ELSE encourage monitoring
```

## Python source code
The runnable source is in [main.py](main.py).

## Test cases
See [test_cases.md](test_cases.md) for normal and boundary test cases.

## Output screenshots
See the [screenshots folder](screenshots/) for the sample-run image. These are illustrative sample console images, not photographs of an actual terminal session.

## Conclusion
This case study demonstrates how a real-world task can be represented as an algorithm and implemented in Python. Running the program with valid and invalid inputs helps practise logic, testing, and interpreting output.
