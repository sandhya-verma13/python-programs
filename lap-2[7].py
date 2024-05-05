# List of tuples containing (name, scores) pairs
students = [("Alice", (85, 90, 88)),("Bob", (75, 82, 79)),("Charlie", (90, 85, 92))]

# Sort the list of tuples based on the total score (sum of scores in all subjects) in descending order
sorted_students = sorted(students, key=lambda x: sum(x[1]), reverse=True)

# Print the sorted list of tuples
for student in sorted_students:
    print(student)
