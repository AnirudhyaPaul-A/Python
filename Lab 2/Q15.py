# 15. Write a Python program that prompts the user to enter a base number and an exponent, and then calculates the power of the base to the exponent. The program should not use the exponentiation operator (**) or the math.pow() function.

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Prompt user for input
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Calculate the power
result = power(base, exponent)

# Print the result
print(f"{base} raised to the power of {exponent} is {result}")
