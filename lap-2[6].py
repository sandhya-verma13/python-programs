# List of tuples representing (name, age) pairs
people = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

# Initialize an empty dictionary to store the converted data
people_dict = {}

# Iterate through the list of tuples and add each pair to the dictionary
for name, age in people:
    people_dict[name] = age

# Print the resulting dictionary
print("Dictionary:", people_dict)

