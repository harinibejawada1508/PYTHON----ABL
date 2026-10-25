# Documentation: Student Marks Matrix Analysis

## 1. Problem Statement
Store marks for multiple students and subjects in a nested list, then calculate each student's total/average and each subject's average.

## 2. Objectives
- Practise writing a small Python console program.
- Accept user input and validate it where implemented.
- Process the data and display understandable results.

## 3. Input
Positive student and subject counts, followed by each mark.

## 4. Output
Each student's marks, total and average, plus average marks for each subject.

## 5. Algorithm
1. Read the number of students and subjects.
2. Validate that both counts are positive.
3. Use nested loops to collect each student's marks into a row, then add each row to the matrix.
4. For each student, print marks, total, and average.
5. For each subject, sum marks across students and print the subject average.

## 6. Sample Execution / Example
```text
For marks [[80, 90], [70, 80]], student averages are 85 and 75; subject averages are 75 and 85.
```

## 7. Python Concepts Used
nested lists, nested loops, indexing, sum, enumerate, arithmetic.

## 8. How to Run
1. Install Python 3 if it is not already installed.
2. Open a terminal in this folder.
3. Run `python main.py` (on some systems use `python3 main.py`).
4. Enter the requested values when prompted.

## 9. Notes and Limitations
This is an educational example, not a production system. Results depend on the values entered. Follow the validation messages and use realistic input values.
