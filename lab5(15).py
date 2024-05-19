
month = input("Enter the month: ")
year = int(input("Enter the year: "))

# Define a dictionary mapping months to their corresponding number of days
days_in_month = {
    "January": 31,
    "February": 28 if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0) else 29,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}
print("Number of days in {} {}: {} days.".format(month, year, days_in_month[month]))

