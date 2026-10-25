# Documentation: Multi-Day Water Tank Simulation

## 1. Problem Statement
Simulate the amount of water in a tank over several days as water is added and used, without allowing the stored amount to exceed tank capacity or fall below zero.

## 2. Objectives
- Practise writing a small Python console program.
- Accept user input and validate it where implemented.
- Process the data and display understandable results.

## 3. Input
Number of days, tank capacity, starting water level, and daily added/used litres.

## 4. Output
End-of-day water level for each day.

## 5. Algorithm
1. Read days, capacity, and starting water.
2. Validate positive days/capacity and starting water between zero and capacity.
3. For each day, read added and used litres.
4. If either amount is negative, show an error and stop.
5. Add water but cap it at tank capacity; subtract usage but floor the level at zero.
6. Display the end-of-day level.

## 6. Sample Execution / Example
```text
Example: capacity 100 L, starting level 50 L, add 20 L, use 15 L → end level 55.00 L.
```

## 7. Python Concepts Used
input/output, validation, for loop, arithmetic, min/max.

## 8. How to Run
1. Install Python 3 if it is not already installed.
2. Open a terminal in this folder.
3. Run `python main.py` (on some systems use `python3 main.py`).
4. Enter the requested values when prompted.

## 9. Notes and Limitations
This is an educational example, not a production system. Results depend on the values entered. Follow the validation messages and use realistic input values.
