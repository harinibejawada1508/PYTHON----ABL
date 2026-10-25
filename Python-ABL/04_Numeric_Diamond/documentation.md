# Documentation: Numeric Diamond Pattern Generator

## 1. Problem Statement
Print a numeric diamond pattern using nested loops, increasing the number of values per row and then decreasing it.

## 2. Objectives
- Practise writing a small Python console program.
- Accept user input and validate it where implemented.
- Process the data and display understandable results.

## 3. Input
Positive integer height.

## 4. Output
A centred numeric pattern with rows from 1 up to the height and back down.

## 5. Algorithm
1. Read the diamond height.
2. If height is not positive, display an error.
3. Loop from row 1 to height, printing leading spaces and numbers 1 through the row number.
4. Loop backwards from height - 1 to 1 and print the lower half.

## 6. Sample Execution / Example
```text
For height 3:
  1
 1 2
1 2 3
 1 2
  1
```

## 7. Python Concepts Used
input/output, validation, for loops, nested iteration, range, strings.

## 8. How to Run
1. Install Python 3 if it is not already installed.
2. Open a terminal in this folder.
3. Run `python main.py` (on some systems use `python3 main.py`).
4. Enter the requested values when prompted.

## 9. Notes and Limitations
This is an educational example, not a production system. Results depend on the values entered. Follow the validation messages and use realistic input values.
