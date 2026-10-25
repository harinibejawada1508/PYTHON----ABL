days = int(input("Enter number of days to record: "))

if days <= 0:
    print("Enter a positive number of days")
else:
    usage = []
    for day in range(1, days + 1):
        row = []
        for slot in range(1, 4):
            units = float(input(f"Day {day}, reading {slot} (units): "))
            row.append(units)
        usage.append(row)

    total = 0
    for day, row in enumerate(usage, start=1):
        daily_total = sum(row)
        total += daily_total
        print(f"Day {day} total: {daily_total:.2f} units")
    print("Total consumption:", round(total, 2), "units")
    print("Average per day:", round(total / days, 2), "units")
