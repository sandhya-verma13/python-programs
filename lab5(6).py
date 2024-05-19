meal_cost = float(input("Enter the cost of the meal: $"))
tax_percent = float(input("Enter the tax percentage: "))
tip_percent = float(input("Enter the tip percentage: "))
tax_amount = meal_cost * (tax_percent / 100)
tip_amount = meal_cost * (tip_percent / 100)
total_cost = meal_cost + tax_amount + tip_amount
print("Total cost of the meal: ${:.2f}".format(total_cost))
