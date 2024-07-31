# 11. Write a program in Python to find the sum of digits of a number.

def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        digit = number % 10
        sum_digits += digit
        number //= 10
    return sum_digits

# Example usage
number = 1234
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is {result}")
