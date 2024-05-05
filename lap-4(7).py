def reverse_string(input_string):
    # Initialize an empty string to store the reversed string
    reversed_string = ""
    
    # Iterate over the characters in the input string in reverse order
    for i in range(len(input_string) - 1, -1, -1):
        # Append each character to the reversed string
        reversed_string += input_string[i]
    
    # Return the reversed string
    return reversed_string

# Test the function
input_string = "Hello World"
reversed_str = reverse_string(input_string)
print("Reversed string:", reversed_str)

