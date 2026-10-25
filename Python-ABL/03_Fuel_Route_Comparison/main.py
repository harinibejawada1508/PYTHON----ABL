distance = float(input("Enter route distance in km: "))
fuel_efficiency = float(input("Enter vehicle mileage in km/litre: "))
fuel_price = float(input("Enter fuel price per litre: "))

if distance < 0 or fuel_efficiency <= 0 or fuel_price < 0:
    print("Invalid details")
else:
    fuel_needed = distance / fuel_efficiency
    cost = fuel_needed * fuel_price
    print("Fuel needed:", round(fuel_needed, 2), "litres")
    print("Estimated trip cost: Rs.", round(cost, 2))
