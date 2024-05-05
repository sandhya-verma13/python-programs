def check_password_strength(password):
    if len(password) < 6:
        print("Weak: Password is less than 6 characters long")
    elif 6 <= len(password) <= 10:
        print("Medium: Password is between 6 and 10 characters long")
    else:
        print("Strong: Password is more than 10 characters long")

# Test the function
password = input("Enter your password: ")
check_password_strength(password)

