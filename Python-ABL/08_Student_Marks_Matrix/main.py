students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

if students <= 0 or subjects <= 0:
    print("Enter positive counts")
else:
    marks = []
    for i in range(students):
        row = []
        for j in range(subjects):
            mark = float(input(f"Student {i + 1}, subject {j + 1} marks: "))
            row.append(mark)
        marks.append(row)

    for i, row in enumerate(marks, start=1):
        average = sum(row) / subjects
        print(f"Student {i}: marks={row}, average={average:.2f}")
    subject_totals = [0] * subjects
    for row in marks:
        for j in range(subjects):
            subject_totals[j] += row[j]
    for j, total in enumerate(subject_totals, start=1):
        print(f"Subject {j} average: {total / students:.2f}")
