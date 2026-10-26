# Test Cases: Student Feedback Sentiment Scoring

These are manual test cases for `main.py`. Use the inputs in order when prompted. Expected output may include formatting and prompts that are not repeated here.

| Test ID | Input | Scenario | Expected result |
|---|---|---|---|
| TC01 | The class is good and helpful | Positive feedback | Positive 2; negative 0; score 2; Positive |
| TC02 | This is a bad and boring class | Negative feedback | Positive 0; negative 2; score -2; Negative |
| TC03 | The class starts today | No matching keywords | Score 0; Neutral |
| TC04 | GOOD! | Case and punctuation handling | Positive 1; score 1; Positive |
| TC05 | good, helpful. | Punctuation at word ends | Positive 2; score 2; Positive |

## Test Notes
- Run each test in Python 3 using `python main.py`.
- Compare the actual output with the expected result.
- Some case studies are simplified learning examples; limitations are noted where relevant.
