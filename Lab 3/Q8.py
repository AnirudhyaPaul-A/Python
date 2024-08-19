# Write a program to compute cosine of x. The user should supply x and a positive integer n. We compute the cosine of x using the series and the computation should use all terms in the series up through the term involving xn cos x = 1 - x2/2! + x4/4! - x6/6! ....


import math
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for i in range(2, num + 1):
            fact *= i
        return fact
def compute_cos(x, n):
    cos_x = 0
    for i in range(n + 1):
        term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        cos_x += term
    return cos_x
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter a positive integer n: "))
cos_x = compute_cos(x, n)
print(f"The computed value of cos({x}) using {n} terms is: {cos_x}")