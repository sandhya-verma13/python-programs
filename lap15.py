def count_vowels(input_string):
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Initialize a counter for vowels
    vowel_count = 0
    
    # Iterate through each character in the string
    for char in input_string:
        # Check if the character is a vowel (case-insensitive)
        if char.lower() in vowels:
            vowel_count += 1
    
    return vowel_count

# Example usage
input_string = input("Enter a string: ")
num_vowels = count_vowels(input_string)
print("Number of vowels in the string:", num_vowels)

