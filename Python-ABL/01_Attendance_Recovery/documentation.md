# Documentation: Attendance Recovery Computation

## 1. Problem Statement
Calculate a student's current attendance percentage and determine the number of additional consecutive classes they must attend to reach 75%, assuming no further absences.

## 2. Objectives
- Practise writing a small Python console program.
- Accept user input and validate it where implemented.
- Process the data and display understandable results.

## 3. Input
Classes attended and total classes conducted (integers).

## 4. Output
Attendance percentage, eligibility message, or number of additional classes needed.

## 5. Algorithm
1. Read attended and conducted class counts.
2. Reject totals that are not positive or attended counts outside 0..conducted.
3. Calculate percentage = attended / conducted × 100.
4. If percentage is at least 75%, report that the requirement is met.
5. Otherwise, increase a counter until (attended + counter) / (conducted + counter) is at least 0.75, then display it.

## 6. Sample Execution / Example
```text
Input: attended = 60, conducted = 100
Output: Attendance percentage: 60.00%
Additional consecutive classes needed: 60
```

## 7. Python Concepts Used
input/output, type conversion, validation, arithmetic, if/else, while loop.

## 8. How to Run
1. Install Python 3 if it is not already installed.
2. Open a terminal in this folder.
3. Run `python main.py` (on some systems use `python3 main.py`).
4. Enter the requested values when prompted.

## 9. Notes and Limitations
This is an educational example, not a production system. Results depend on the values entered. Follow the validation messages and use realistic input values.
