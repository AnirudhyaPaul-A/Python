# 3. Write a program to print all multiple of 10 between a given interval.

def multiples_of_10(start, end):
    for i in range(start, end + 1):
        if i % 10 == 0:
            print(i, end=" ")

# Example usage
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))
print(f"Multiples of 10 between {start} and {end}:")
multiples_of_10(start, end)
