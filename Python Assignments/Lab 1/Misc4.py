# 4. Program to find area & perimeter of a circle

import math
def calculate_area(radius):
    return math.pi * radius ** 2
def calculate_perimeter(radius):
    return 2 * math.pi * radius
radius = float(input("Enter the radius of the circle: "))
area = calculate_area(radius)
perimeter = calculate_perimeter(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}.")
print(f"The perimeter (circumference) of the circle with radius {radius} is {perimeter:.2f}.")