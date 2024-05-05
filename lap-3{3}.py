# Define a dictionary
data = {'a': 10, 'b': 20, 'c': 30, 'd': 15, 'e': 25}

# Get the values and sort them in descending order
sorted_values = sorted(data.values(), reverse=True)

# Find the second largest value
second_largest = sorted_values[1]

print("Second largest value:", second_largest)
