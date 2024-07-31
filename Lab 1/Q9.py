# 9. WAP to check whether a)is a perfect number b)is an Armstrong number

def is_perfect(number):
    if number < 1:
        return False
    divisors_sum = sum([i for i in range(1, number) if number % i == 0])
    return divisors_sum == number
def is_armstrong(number):
    num_str = str(number)
    num_length = len(num_str)
    armstrong_sum = sum([int(digit) ** num_length for digit in num_str])
    return armstrong_sum == number
number = int(input("Enter a number: "))
if is_perfect(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")