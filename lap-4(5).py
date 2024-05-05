def is_valid_palindrome(sentence):
    # Remove non-alphanumeric characters and convert to lowercase
    clean_sentence = ''.join(char.lower() for char in sentence if char.isalnum())
    # Check if the clean sentence is equal to its reverse
    return clean_sentence == clean_sentence[::-1]

# Test the function
sentence = "A man, a plan, a canal, Panama!"
print(is_valid_palindrome(sentence))  # Output: True

