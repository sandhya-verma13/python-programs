age = int(input("Enter your age: "))
gender = input("Enter your gender (Male/Female): ")

# Define the heart rate range based on age and gender
if gender.lower() == 'male':
    lower_limit = 0.5 * (220 - age)
    upper_limit = 0.85 * (220 - age)
elif gender.lower() == 'female':
    lower_limit = 0.5 * (226 - age)
    upper_limit = 0.85 * (226 - age)
else:
    print("Invalid gender. Please enter Male or Female.")
    exit()
print("Recommended heart rate range during exercise:", int(lower_limit), "-", int(upper_limit), "bpm.")

