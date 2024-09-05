# 1. Write a program to check whether a number is Buzz or not.

def is_buzz_number(number):
    return number % 7 == 0 or number % 10 == 7

# Example usage
number = int(input("Enter a number: "))
if is_buzz_number(number):
    print(f"{number} is a Buzz number.")
else:
    print(f"{number} is not a Buzz number.")
