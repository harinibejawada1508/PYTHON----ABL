# Test Cases: Password Policy Validation

These are manual test cases for `main.py`. Use the inputs in order when prompted. Expected output may include formatting and prompts that are not repeated here.

| Test ID | Input | Scenario | Expected result |
|---|---|---|---|
| TC01 | Hello123! | All requirements satisfied | All five checks pass; password meets sample policy |
| TC02 | hello123! | No uppercase letter | Uppercase check fails; overall policy not met |
| TC03 | HELLO123! | No lowercase letter | Lowercase check fails; overall policy not met |
| TC04 | HelloWorld! | No digit | Digit check fails; overall policy not met |
| TC05 | Hello123 | No special character | Special-character check fails; overall policy not met |
| TC06 | Ab1! | Too short | Length check fails; overall policy not met |

## Test Notes
- Run each test in Python 3 using `python main.py`.
- Compare the actual output with the expected result.
- Some case studies are simplified learning examples; limitations are noted where relevant.
