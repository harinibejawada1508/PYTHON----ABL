attended = int(input("Enter classes attended: "))
conducted = int(input("Enter total classes conducted: "))

if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid attendance details")
else:
    percentage = attended / conducted * 100
    print("Attendance percentage:", round(percentage, 2), "%")
    if percentage >= 75:
        print("Attendance requirement satisfied")
    else:
        required = 0
        while (attended + required) / (conducted + required) < 0.75:
            required += 1
        print("Additional classes to attend:", required)
