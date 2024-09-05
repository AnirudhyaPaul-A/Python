# Write a python program to count the prime numbers in an array.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(arr):
    return sum(1 for x in arr if is_prime(x))

array = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Number of prime numbers:", count_primes(array))