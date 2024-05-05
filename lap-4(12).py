def check_username(username):
    # Check if username contains only alphanumeric characters
    if not username.isalnum():
        return False
    
    # Check if username starts with a letter
    if not username[0].isalpha():
        return False
    
    # Check if username length is between 6 and 12 characters
    if not 6 <= len(username) <= 12:
        return False
    
    return True

# Test the function
username = input("Enter a username: ")
if check_username(username):
    print("Username is valid.")
else:
    print("Username does not meet the criteria.")

