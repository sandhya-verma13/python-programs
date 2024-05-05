# List of temperatures measured in Celsius
celsius= [0, 10, 20, 30, 40]

# Initialize an empty list to store Fahrenheit temperatures
fahr = []

# Iterate over each temperature in the list of Celsius temperatures
for celsius in celsius:
    # Convert Celsius to Fahrenheit using the conversion formula
    fahrenheit = (celsius * 9/5) + 32
    # Add the converted temperature to the list of Fahrenheit temperatures
    fahr.append(fahrenheit)

# Print the resulting list of Fahrenheit temperatures
print("Fahrenheit temperatures:", fahr)

