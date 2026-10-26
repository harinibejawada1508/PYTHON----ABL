# Password Policy Validation

## Problem statement
Check length, uppercase, lowercase, digit, and supported special character rules.

## Objectives
- Practise basic Python programming and problem solving.
- Accept input, process values, and display results.
- Use validation, conditions, loops, and calculations where appropriate.

## Assumptions
Educational policy only; supported specials are !@#$%^&*()-_+=?.

## Algorithm
Scan password characters, set category flags, then check all flags and minimum length.

## Flowchart
See [flowchart.md](flowchart.md) for the flowchart.

## Pseudocode
```text
READ password; set all flags FALSE
FOR each character: update matching flag
IF length >= 8 AND all flags: PRINT meets policy
ELSE PRINT does not meet policy and guidance
```

## Python source code
The runnable source is in [main.py](main.py).

## Test cases
See [test_cases.md](test_cases.md) for normal and boundary test cases.

## Output screenshots
See the [screenshots folder](screenshots/) for the sample-run image. These are illustrative sample console images, not photographs of an actual terminal session.

## Conclusion
This case study demonstrates how a real-world task can be represented as an algorithm and implemented in Python. Running the program with valid and invalid inputs helps practise logic, testing, and interpreting output.
