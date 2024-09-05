# 9. Convert Decimal number to Binary

def decimal_to_binary(n):
    # Base case for recursion
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        # Recursive step: floor division by 2 and get remainder
        return decimal_to_binary(n // 2) + str(n % 2)

# Example usage
decimal_number = 23
binary_number = decimal_to_binary(decimal_number)
print(f"Decimal {decimal_number} in binary is {binary_number}")
