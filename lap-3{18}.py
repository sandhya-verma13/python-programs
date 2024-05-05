# Dictionary representing room availability for each date
room_availability = {
    '2024-04-20': {'single': 5, 'double': 10, 'suite': 3},
    '2024-04-21': {'single': 3, 'double': 8, 'suite': 1},
    '2024-04-22': {'single': 8, 'double': 12, 'suite': 5}
}

# Input date to check availability
date_to_check = input("Enter the date (YYYY-MM-DD): ")

# Check availability for the input date
if date_to_check in room_availability:
    print(f"Room availability for {date_to_check}:")
    for room_type, availability in room_availability[date_to_check].items():
        print(f"{room_type.capitalize()} rooms: {availability}")
else:
    print(f"No information available for {date_to_check}.")

