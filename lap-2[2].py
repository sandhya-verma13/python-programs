# List of tuples representing people's names and ages
people = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

# Calculate the total age and count the number of people
age = sum(age for name, age in people)
total_people = len(people)

# Calculate the average age
average_age = age / total_people

# Print the average age
print("Average age of all the people:", average_age)
