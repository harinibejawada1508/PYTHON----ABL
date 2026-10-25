capacity = float(input("Enter tank capacity in litres: "))
water = float(input("Enter starting water in litres: "))
days = int(input("Enter number of days: "))

if capacity <= 0 or water < 0 or water > capacity or days < 0:
    print("Invalid details")
else:
    for day in range(1, days + 1):
        inflow = float(input(f"Day {day} - water added (litres): "))
        outflow = float(input(f"Day {day} - water used (litres): "))
        water = water + inflow - outflow
        if water < 0:
            water = 0
        if water > capacity:
            water = capacity
        print("Water remaining:", round(water, 2), "litres")
