# Two lists of integers
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Initialize an empty list to store common elements
common_elements = []

# Iterate over each element in the first list
for num in list1:
    # Check if the element is also present in the second list
    if num in list2:
        # Add the common element to the list of common elements
        common_elements.append(num)

# Print the list of common elements
print("Common elements:", common_elements)

