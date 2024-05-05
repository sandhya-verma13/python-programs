# Input string
input_string = "Hello, World! How are you today?"

# Convert the input string to lowercase
input_string = input_string.lower()

# Initialize a variable to count vowels
vowel_count = 0

# Iterate through each character in the input string
for char in input_string:
    # Check if the character is a vowel
    if char in 'aeiou':
        # Increment the vowel count
        vowel_count += 1

# Print the total number of vowels
print("Number of vowels:", vowel_count)

