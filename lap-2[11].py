# Define the performance data for investment instruments
instrument1 = [("2023-01-01", 1000), ("2023-03-01", 1200), ("2023-06-01", 1400)]
instrument2 = [("2023-01-01", 2000), ("2023-03-01", 1800), ("2023-06-01", 2500)]
instrument3 = [("2023-01-01", 1500), ("2023-03-01", 1700), ("2023-06-01", 1800)]

# Prompt the user to enter start and end dates for the analysis period
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

# Calculate growth rate for each instrument over the specified period
max_growth_rate = -1
best_instrument = None

# Function to convert date strings to integers for comparison
def date_to_int(date):
    year, month, day = map(int, date.split('-'))
    return year * 10000 + month * 100 + day

# Iterate over each instrument's performance data
for instrument, data in [("Instrument 1", instrument1), ("Instrument 2", instrument2), ("Instrument 3", instrument3)]:
    start_value = None
    end_value = None

    # Find start and end values for the specified period
    for date, value in data:
        if date_to_int(date) == date_to_int(start_date):
            start_value = value
        elif date_to_int(date) == date_to_int(end_date):
            end_value = value

    # If both start and end values are found, calculate growth rate
    if start_value is not None and end_value is not None:
        growth_rate = ((end_value - start_value) / start_value) * 100
        print(f"{instrument}: Growth rate = {growth_rate:.2f}%")

        # Update the instrument with the highest growth rate
        if growth_rate > max_growth_rate:
            max_growth_rate = growth_rate
            best_instrument = instrument

# Print the instrument with the highest growth rate
print(f"The instrument with the highest growth rate is {best_instrument} with a growth rate of {max_growth_rate:.2f}%.")


