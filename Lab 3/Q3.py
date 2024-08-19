# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

import math
def _solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        return ()
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
solutions = _solve_quadratic_eqn(a, b, c)
if solutions:
    if len(solutions) == 1:
        print(f"The solution is: {solutions[0]}")
    else:
        print(f"The solutions are: {solutions[0]} and {solutions[1]}")
else:
    print("There are no real solutions.")