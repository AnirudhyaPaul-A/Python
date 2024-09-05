# 10. Write a program in Python to check if a number is Krishnamurthy number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_krishnamurthy_number(number):
    sum_of_factorials = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum_of_factorials += factorial(digit)
        temp //= 10
    
    return sum_of_factorials == number

# Example usage
number = 145
if is_krishnamurthy_number(number):
    print(f"{number} is a Krishnamurthy number.")
else:
    print(f"{number} is not a Krishnamurthy number.")
