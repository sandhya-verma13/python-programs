def generate_email(first_name, last_name):
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    return email

# Test the function
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email_address = generate_email(first_name, last_name)
print("Generated email address:", email_address)

