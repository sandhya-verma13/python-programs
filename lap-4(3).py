def are_rotations(str1, str2):
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False
    
    # Concatenate str1 with itself
    concatenated_str = str1 + str1
    
    # Check if str2 is a substring of the concatenated string
    if str2 in concatenated_str:
        return True
    else:
        return False

# Test the function
string1 = "abcd"
string2 = "cdab"
print(are_rotations(string1, string2))  # Output: True

