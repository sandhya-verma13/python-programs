# Dictionary representing student grades in various subjects
student_grades = {
    "Alice": {"Math": 90, "Physics": 85, "Chemistry": 88},
    "Bob": {"Math": 92, "Physics": 88, "Chemistry": 84},
    "Charlie": {"Math": 85, "Physics": 82, "Chemistry": 90}
}

# Calculate average grade for each student
average_grades = {}

for student, grades in student_grades.items():
    total_grades = sum(grades.values())
    num_subjects = len(grades)
    average_grade = total_grades / num_subjects
    average_grades[student] = average_grade

# Print average grades for each student
for student, avg_grade in average_grades.items():
    print(f"{student}: {avg_grade:.2f}")

