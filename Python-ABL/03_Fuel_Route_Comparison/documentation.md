# Documentation: Fuel Consumption and Route Cost

## 1. Problem Statement
Estimate the fuel required and fuel cost for a journey from its distance, vehicle mileage, and fuel price.

## 2. Objectives
- Practise writing a small Python console program.
- Accept user input and validate it where implemented.
- Process the data and display understandable results.

## 3. Input
Distance in kilometres, mileage in km per litre, and price per litre.

## 4. Output
Estimated litres required and cost in rupees.

## 5. Algorithm
1. Read distance, mileage, and fuel price.
2. Check that distance and mileage are positive and price is non-negative.
3. Calculate fuel = distance / mileage.
4. Calculate cost = fuel × price.
5. Display fuel and cost rounded to two decimal places.

## 6. Sample Execution / Example
```text
Input: distance 150 km, mileage 15 km/L, price ₹100/L → fuel 10.00 L; cost ₹1000.00.
```

## 7. Python Concepts Used
input/output, type conversion, validation, arithmetic, formatted output.

## 8. How to Run
1. Install Python 3 if it is not already installed.
2. Open a terminal in this folder.
3. Run `python main.py` (on some systems use `python3 main.py`).
4. Enter the requested values when prompted.

## 9. Notes and Limitations
This is an educational example, not a production system. Results depend on the values entered. Follow the validation messages and use realistic input values.
