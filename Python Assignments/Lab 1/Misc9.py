# 9. Program to convert miles to kilometers

def miles_to_kilometers(miles):
    return miles * 1.60934
miles = float(input("Enter distance in miles: "))
kilometers = miles_to_kilometers(miles)
print(f"{miles} miles is equal to {kilometers:.2f} kilometers.")