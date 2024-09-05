# 8. Write a function to calculate the power of a number using recursion

def power(base, exponent):
    # Base case: any number raised to the power of 0 is 1
    if exponent == 0:
        return 1
    # Recursive case: multiply the base by the result of base raised to (exponent - 1)
    else:
        return base * power(base, exponent - 1)

# Example usage
base = 2
exponent = 3
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")
