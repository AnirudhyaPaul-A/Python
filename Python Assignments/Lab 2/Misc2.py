# 2. Write a program to calculate the sum of natural numbers up to a certain range.

def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

# Example usage
n = int(input("Enter the range: "))
print(f"The sum of natural numbers up to {n} is {sum_of_natural_numbers(n)}")
