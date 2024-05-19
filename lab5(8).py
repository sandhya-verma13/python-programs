year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year with 366 days.")
else:
    print(year, "is a common year with 365 days.")

