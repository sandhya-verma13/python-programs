# Read a string from input
input_string = input("Enter a string: ")

# Read start and end indices from input
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))

# Extract the substring based on the start and end indices
substring = input_string[start_index:end_index]

# Display the extracted substring
print("Extracted substring:", substring)


