# Test Cases: Fuel Consumption and Route Cost

These are manual test cases for `main.py`. Use the inputs in order when prompted. Expected output may include formatting and prompts that are not repeated here.

| Test ID | Input | Scenario | Expected result |
|---|---|---|---|
| TC01 | 150 km; 15 km/L; ₹100/L | Normal calculation | Fuel required 10.00 litres; cost ₹1000.00 |
| TC02 | 100 km; 20 km/L; ₹0/L | Zero fuel price | Fuel required 5.00 litres; cost ₹0.00 |
| TC03 | 0 km; 10 km/L; ₹100/L | Zero distance | Validation message |
| TC04 | 100 km; 0 km/L; ₹100/L | Zero mileage | Validation message |
| TC05 | 100 km; 10 km/L; ₹-1/L | Negative price | Validation message |

## Test Notes
- Run each test in Python 3 using `python main.py`.
- Compare the actual output with the expected result.
- Some case studies are simplified learning examples; limitations are noted where relevant.
