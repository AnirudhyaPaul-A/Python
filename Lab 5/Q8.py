# Print the season name of the year based on the month number using a dictionary.

month_to_season = {
    1: 'Winter', 2: 'Winter', 3: 'Spring',
    4: 'Spring', 5: 'Spring', 6: 'Summer',
    7: 'Summer', 8: 'Summer', 9: 'Autumn',
    10: 'Autumn', 11: 'Autumn', 12: 'Winter'
}

def get_season(month):
    return month_to_season.get(month, 'Invalid month')

month_number = int(input("Enter the month number: "))
season = get_season(month_number)
print(f"The season for month {month_number} is {season}.")