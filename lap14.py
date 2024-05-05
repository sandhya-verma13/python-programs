def reverse_string(string):
    # Using slicing to reverse the string
    reversed_string = string[::-1]
    return reversed_string

# Example usage
string = input("Enter a string: ")
reversed_string = reverse_string(string)
print("Reversed string:", reversed_string)

