# Feedback Sentiment Scoring

## Problem statement
Score feedback by counting positive keyword occurrences and subtracting negative occurrences.

## Objectives
- Practise basic Python programming and problem solving.
- Accept input, process values, and display results.
- Use validation, conditions, loops, and calculations where appropriate.

## Assumptions
Simple substring matching; not a full natural-language sentiment model.

## Algorithm
Lowercase feedback, count positive and negative keywords, then classify score.

## Flowchart
See [flowchart.md](flowchart.md) for the flowchart.

## Pseudocode
```text
READ feedback; lowercase; score = 0
FOR positive word: add occurrences
FOR negative word: subtract occurrences
IF score > 0: positive; ELSE IF score < 0: negative; ELSE neutral
```

## Python source code
The runnable source is in [main.py](main.py).

## Test cases
See [test_cases.md](test_cases.md) for normal and boundary test cases.

## Output screenshots
See the [screenshots folder](screenshots/) for the sample-run image. These are illustrative sample console images, not photographs of an actual terminal session.

## Conclusion
This case study demonstrates how a real-world task can be represented as an algorithm and implemented in Python. Running the program with valid and invalid inputs helps practise logic, testing, and interpreting output.
