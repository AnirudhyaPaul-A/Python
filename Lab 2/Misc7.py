# 7. Write a program to find median of a set of numbers.

def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

# Prompt user for input
input_string = input("Enter the numbers separated by spaces: ")

# Split the input string into a list of substrings
substrings = input_string.split()

# Convert each substring to an integer using a list comprehension
numbers = [int(substring) for substring in substrings]

# Calculate and print the median
print(f"The median is {find_median(numbers)}")

