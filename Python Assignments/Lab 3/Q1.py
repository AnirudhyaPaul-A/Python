# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    seasons = {
        'January': 'Winter', 'February': 'Winter', 'March': 'Spring',
        'April': 'Spring', 'May': 'Spring', 'June': 'Summer',
        'July': 'Summer', 'August': 'Summer', 'September': 'Autumn',
        'October': 'Autumn', 'November': 'Autumn', 'December': 'Winter'
    }
    return seasons.get(month.capitalize(), "Invalid month")
month = input("Enter a month: ")
season = check_season(month)
print(f"The season for {month} is {season}.")
