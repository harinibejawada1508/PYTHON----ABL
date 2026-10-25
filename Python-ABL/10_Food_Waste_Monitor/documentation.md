# Documentation: Food Waste Monitoring System

## 1. Problem Statement
Record daily food waste over a selected period and report total and average waste, with a simple suggestion based on the average.

## 2. Objectives
- Practise writing a small Python console program.
- Accept user input and validate it where implemented.
- Process the data and display understandable results.

## 3. Input
Positive number of days and food waste in kilograms for each day.

## 4. Output
Total waste, average daily waste, and a suggestion; negative waste triggers an error.

## 5. Algorithm
1. Read the number of days and validate it is positive.
2. Collect each day's waste amount.
3. If a negative amount is entered, show an error and stop collection.
4. If all days were recorded, calculate total and average waste.
5. If average is above 2 kg, suggest planning portions and storing leftovers safely; otherwise encourage continued monitoring.

## 6. Sample Execution / Example
```text
Three days: 1, 2, 3 kg → total 6.00 kg, average 2.00 kg; keep monitoring food waste.
```

## 7. Python Concepts Used
lists, loops, validation, sum, averages, conditionals.

## 8. How to Run
1. Install Python 3 if it is not already installed.
2. Open a terminal in this folder.
3. Run `python main.py` (on some systems use `python3 main.py`).
4. Enter the requested values when prompted.

## 9. Notes and Limitations
This is an educational example, not a production system. Results depend on the values entered. Follow the validation messages and use realistic input values.
