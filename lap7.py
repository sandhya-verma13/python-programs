# Read the number from input
number = int(input("Enter a number: "))

# Initialize the factorial variable
factorial = 1

# Calculate the factorial using a loop
for i in range(1, number + 1):
    factorial *= i

# Print the factorial
print("The factorial of", number, "is:", factorial)






