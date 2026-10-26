# Fuel Cost Estimation

## Problem statement
Calculate fuel needed and estimated trip cost from distance, mileage, and price per litre.

## Objectives
- Practise basic Python programming and problem solving.
- Accept input, process values, and display results.
- Use validation, conditions, loops, and calculations where appropriate.

## Assumptions
Mileage and price are constant throughout the trip.

## Algorithm
Read distance, mileage, price. Validate. Compute distance/mileage and multiply by price.

## Flowchart
See [flowchart.md](flowchart.md) for the flowchart.

## Pseudocode
```text
READ distance, mileage, price
IF distance < 0 OR mileage <= 0 OR price < 0: PRINT invalid
ELSE fuel = distance / mileage; cost = fuel * price; PRINT fuel and cost
```

## Python source code
The runnable source is in [main.py](main.py).

## Test cases
See [test_cases.md](test_cases.md) for normal and boundary test cases.

## Output screenshots
See the [screenshots folder](screenshots/) for the sample-run image. These are illustrative sample console images, not photographs of an actual terminal session.

## Conclusion
This case study demonstrates how a real-world task can be represented as an algorithm and implemented in Python. Running the program with valid and invalid inputs helps practise logic, testing, and interpreting output.
