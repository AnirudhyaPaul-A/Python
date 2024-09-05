# Write a program to compute sin x for given x. The user should supply x and a positive integer n. We compute the sine of x using the series and the computation should use all terms in the series up through the term involving xn sin x = x - x3/3! + x5/5! - x7/7! + x9/9! ........


import math
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for i in range(2, num + 1):
            fact *= i
        return fact
def compute_sin(x, n):
    sin_x = 0
    for i in range(n + 1):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        sin_x += term
    return sin_x
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter a positive integer n: "))
sin_x = compute_sin(x, n)
print(f"The computed value of sin({x}) using {n} terms is: {sin_x}")