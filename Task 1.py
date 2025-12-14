students_marks = {
    "Avirup": 85,
    "Rahul": 78,
    "Sneha": 92,
    "Anjali": 88
}

name = input("Enter the student's name: ")

if name in students_marks:
    print(f"Marks obtained by {name}: {students_marks[name]}")
else:
    print("Student not found in the record.")
