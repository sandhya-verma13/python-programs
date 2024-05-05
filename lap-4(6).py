# Input string
input_string = "Hello World"

# Convert input string to lowercase
input_string = input_string.lower()

# Initialize an empty dictionary to store character counts
char_counts = {}

# Iterate over each character in the input string
for char in input_string:
    # Check if the character is alphanumeric
    if char.isalnum():
        # If the character is already in the dictionary, increment its count
        if char in char_counts:
            char_counts[char] += 1
        # If the character is not in the dictionary, add it with count 1
        else:
            char_counts[char] = 1

# Print the character counts
for char, count in char_counts.items():
    print(f"'{char}': {count}")

