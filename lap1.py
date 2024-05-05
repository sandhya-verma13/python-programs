# Read three integers from input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Check if all three integers are equal
if a == b == c:
    print("All numbers are equal")
# Check if two or more integers are equal and larger than the third integer
elif (a == b and a > c) or (a == c and a > b) or (b == c and b > a):
    print("Equal numbers are larger")
# Check the largest among the three integers
else:
    maximum = max(a, b, c)
    print("The largest number is:", maximum)

