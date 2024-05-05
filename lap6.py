# Read the number from input
num = int(input("Enter a number: "))

# Initialize the sum variable
digit_sum = 0

# Convert the number to a string to iterate over its digits
num_str = str(num)

# Iterate over each digit and add it to the sum
for digit in num_str:
    digit_sum += int(digit)

# Print the result
print("The sum of digits of", num, "is:", digit_sum)






