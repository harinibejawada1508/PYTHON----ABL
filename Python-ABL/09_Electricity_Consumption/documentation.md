# Documentation: Weekly Electricity Consumption Matrix

## 1. Problem Statement
Record electricity usage for three time slots per day and calculate daily totals, overall usage, and average daily consumption.

## 2. Objectives
- Practise writing a small Python console program.
- Accept user input and validate it where implemented.
- Process the data and display understandable results.

## 3. Input
Positive number of days and three non-negative kWh readings per day (the current code does not reject negative readings).

## 4. Output
Daily consumption, total consumption, and average daily consumption in kWh.

## 5. Algorithm
1. Read the number of days and validate that it is positive.
2. For each day, collect three time-slot readings in a list.
3. Store each daily row in a matrix.
4. Calculate and display the sum for each day.
5. Add daily totals and display overall and average consumption.

## 6. Sample Execution / Example
```text
One day with readings 1.2, 0.8, 1.0 kWh → daily and total 3.00 kWh; average 3.00 kWh.
```

## 7. Python Concepts Used
nested lists, loops, input conversion, sum, enumerate, averages.

## 8. How to Run
1. Install Python 3 if it is not already installed.
2. Open a terminal in this folder.
3. Run `python main.py` (on some systems use `python3 main.py`).
4. Enter the requested values when prompted.

## 9. Notes and Limitations
This is an educational example, not a production system. Results depend on the values entered. Follow the validation messages and use realistic input values.
