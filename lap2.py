# Read three numbers from input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Check if any two or more numbers are equal
if a == b == c:
    print("Numbers are not distinct.")
# Sort the numbers in ascending order and print them
else:
    numbers = [a, b, c]
    numbers.sort()
    print("Numbers in ascending order:", numbers)


