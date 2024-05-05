# Input dictionary of lists
dict_of_lists = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'London', 'Paris']
}

# Convert dictionary of lists into a list of dictionaries
list_of_dicts = [dict(zip(dict_of_lists, t)) for t in zip(*dict_of_lists.values())]

# Print the list of dictionaries
for item in list_of_dicts:
    print(item)
