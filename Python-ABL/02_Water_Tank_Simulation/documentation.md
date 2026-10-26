# Water Tank Simulation

## Problem statement
Simulate tank level over multiple days, keeping it between zero and tank capacity.

## Objectives
- Practise basic Python programming and problem solving.
- Accept input, process values, and display results.
- Use validation, conditions, loops, and calculations where appropriate.

## Assumptions
All water values are in litres; inflow and outflow are numeric.

## Algorithm
Read capacity, starting water, days. Validate. For each day read inflow/outflow, update level, clamp to range, print.

## Flowchart
See [flowchart.md](flowchart.md) for the flowchart.

## Pseudocode
```text
READ capacity, water, days
IF invalid: PRINT error
ELSE FOR each day: READ inflow, outflow; water = water + inflow - outflow; clamp water to [0, capacity]; PRINT water
```

## Python source code
The runnable source is in [main.py](main.py).

## Test cases
See [test_cases.md](test_cases.md) for normal and boundary test cases.

## Output screenshots
See the [screenshots folder](screenshots/) for the sample-run image. These are illustrative sample console images, not photographs of an actual terminal session.

## Conclusion
This case study demonstrates how a real-world task can be represented as an algorithm and implemented in Python. Running the program with valid and invalid inputs helps practise logic, testing, and interpreting output.
