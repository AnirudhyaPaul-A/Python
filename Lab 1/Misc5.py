# 5. Program to find area & perimeter of a rectangle

def calculate_area(length, width):
    return length * width
def calculate_perimeter(length, width):
    return 2 * (length + width)
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)
print(f"The area of the rectangle with length {length} and width {width} is {area:.2f}.")
print(f"The perimeter of the rectangle with length {length} and width {width} is {perimeter:.2f}.")