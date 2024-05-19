temperature = float(input("Enter your temperature: "))
scale = input("Enter the scale (F for Fahrenheit, C for Celsius): ")

if scale.lower() == 'f':
    if temperature >= 100.4:
        print("You have a fever.")
    else:
        print("You do not have a fever.")
elif scale.lower() == 'c':
    if temperature >= 38:
        print("You have a fever.")
    else:
        print("You do not have a fever.")
else:
    print("Invalid scale. Please enter 'F' for Fahrenheit or 'C' for Celsius.")
