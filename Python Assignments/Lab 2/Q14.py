# 14. Print the series upto N terms: 1,2,6,24,120,720 …

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def print_factorial_series(lim):
    for i in range(1, lim + 1):
        print(factorial(i), end=" ")

# Prompt user for input
lim = int(input("Enter the number of terms: "))
print(f"The series up to {lim} terms is:")
print_factorial_series(lim)
