# 2. To solve the quadratic equation.

import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return ("Two distinct real roots", root1, root2)
    elif discriminant == 0:
        # One real root (double root)
        root = -b / (2*a)
        return ("One real root", root)
    else:
        # Two complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return ("Two complex roots", root1, root2)

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

solution = solve_quadratic(a, b, c)

if len(solution) == 3:
    print(f"The quadratic equation {a}x^2 + {b}x + {c} = 0 has {solution[0]}: {solution[1]}, {solution[2]}")
else:
    print(f"The quadratic equation {a}x^2 + {b}x + {c} = 0 has {solution[0]}: {solution[1]}")