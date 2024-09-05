# 8. Write a program to compute the value of Euler’s number that is used as the base of natural logarithms. Use the following formula. e= 1+ 1/1! +1 /2! + 1/3+................ 1/n!

import math

def compute_euler_number(n):
    e = 1
    for i in range(1, n + 1):
        e += 1 / math.factorial(i)
    return e

# Example usage
n = int(input("Enter the value of n: "))
print(f"The value of Euler's number up to {n} terms is {compute_euler_number(n)}")
