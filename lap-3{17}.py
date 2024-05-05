# Dictionary representing expenses for each category
expenses = {
    'food': 250,
    'utilities': 120,
    'transportation': 80,
    'entertainment': 150,
    'clothing': 100
}

# Calculate total expenses for each category
total_expenses = {}
for category, expense in expenses.items():
    total_expenses[category] = expense

# Print total expenses for each category
for category, total in total_expenses.items():
    print(f"Total expenses for {category}: {total}")

