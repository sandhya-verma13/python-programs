# Define two dictionaries
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 30, 'c': 40, 'd': 50}

# Combine dictionaries by adding values for common keys
combined_dict = {}
for key in dict1:
    if key in dict2:
        combined_dict[key] = dict1[key] + dict2[key]
    else:
        combined_dict[key] = dict1[key]

# Add keys from dict2 not present in dict1
for key in dict2:
    if key not in dict1:
        combined_dict[key] = dict2[key]

print("Combined Dictionary:", combined_dict)

