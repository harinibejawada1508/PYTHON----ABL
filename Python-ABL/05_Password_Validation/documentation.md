# Documentation: Password Policy Validation

## 1. Problem Statement
Check a password against a simple sample policy and report which requirements pass or fail.

## 2. Objectives
- Practise writing a small Python console program.
- Accept user input and validate it where implemented.
- Process the data and display understandable results.

## 3. Input
A password string.

## 4. Output
Pass/fail result for length, uppercase, lowercase, digit, and special-character rules, plus an overall result.

## 5. Algorithm
1. Read the password.
2. Check whether it has at least 8 characters.
3. Check for uppercase and lowercase letters, a digit, and a non-alphanumeric character.
4. Display the result of each rule.
5. If all rules pass, report that the sample policy is satisfied; otherwise ask the user to improve it.

## 6. Sample Execution / Example
```text
Input: Hello123!
Output: all five checks pass; Password meets the sample policy.
```

## 7. Python Concepts Used
strings, len, dictionaries, any, isupper/islower/isdigit, loops, all.

## 8. How to Run
1. Install Python 3 if it is not already installed.
2. Open a terminal in this folder.
3. Run `python main.py` (on some systems use `python3 main.py`).
4. Enter the requested values when prompted.

## 9. Notes and Limitations
This is an educational example, not a production system. Results depend on the values entered. Follow the validation messages and use realistic input values.
