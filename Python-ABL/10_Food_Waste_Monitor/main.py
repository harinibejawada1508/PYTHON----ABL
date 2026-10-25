days = int(input("Enter number of days: "))

if days <= 0:
    print("Enter a positive number of days")
else:
    total_waste = 0.0
    for day in range(1, days + 1):
        waste = float(input(f"Day {day} food waste in kg: "))
        if waste < 0:
            print("Negative amount ignored")
            waste = 0
        total_waste += waste
    average = total_waste / days
    print("Total food waste:", round(total_waste, 2), "kg")
    print("Average daily waste:", round(average, 2), "kg")
    if average > 2:
        print("Suggestion: review food preparation and portion sizes.")
    else:
        print("Good job keeping average waste at or below 2 kg.")
