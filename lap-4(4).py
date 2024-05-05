# Define the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Input string
input_string = input("Enter a string: ")

# Convert input string to lowercase
input_string = input_string.lower()

# Initialize a set to store unique characters in the input string
unique_chars = set()

# Iterate through the characters in the input string
for char in input_string:
    # Add alphabetic characters to the set
    if char.isalpha():
        unique_chars.add(char)

# Check if the set of unique characters contains all the letters of the alphabet
if len(unique_chars) == len(alphabet):
    print("True")
else:
    print("False")

