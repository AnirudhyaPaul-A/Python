# Write a python script that displays the following table 1 1 1 1 1 2 1 2 4 8 3 1 3 9 27 4 1 4 16 64 5 1 5 25 125

def generate_table():
    print("Number 1 Number Number^2 Number^3")
    for i in range(1, 6):
        number = i
        print(f"{number} 1 {number} {number ** 2} {number ** 3}")
generate_table()