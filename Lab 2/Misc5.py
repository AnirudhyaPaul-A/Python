# 5. Write a program to find HCF of two Numbers.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The HCF of {num1} and {num2} is {gcd(num1, num2)}")
