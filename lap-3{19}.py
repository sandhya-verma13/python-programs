# Sample data
data = [
    {"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
    {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}
]

# Extracting values from the dictionaries and storing them in a set to get distinct values
distinct_values = set(value for d in data for value in d.values())

# Printing the unique values
print("Unique Values:", distinct_values)

