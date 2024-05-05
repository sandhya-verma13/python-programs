# Read the list of numbers from input
numbers = list(map(int, input("Enter the list of numbers separated by space: ").split()))

# Initialize the maximum variable with the first element of the list
maximum = numbers[0]

# Iterate through the list to find the maximum element
for number in numbers:
    if number > maximum:
        maximum = number

# Print the maximum element
print("The maximum element in the list is:", maximum)

