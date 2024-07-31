# 6. Write a program to count the number of digits of an integer.

def count_digits(number):
    return len(str(abs(number)))

# Example usage
number = int(input("Enter an integer: "))
print(f"The number of digits in {number} is {count_digits(number)}")
