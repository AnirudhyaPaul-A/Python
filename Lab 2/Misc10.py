# 10. Write a program to read two integer values m and n and to decide and print whether m is multiple of n.

def is_multiple(m, n):
    return m % n == 0

# Example usage
m = int(input("Enter the first number (m): "))
n = int(input("Enter the second number (n): "))
if is_multiple(m, n):
    print(f"{m} is a multiple of {n}")
else:
    print(f"{m} is not a multiple of {n}")
