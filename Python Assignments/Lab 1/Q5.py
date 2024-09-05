# 5. WAP to find factors of a given number

number = int(input("Enter a number to find its factors: "))
factors = [i for i in range(1, number + 1) if number % i == 0]
print(f"The factors of {number} are: {factors}")