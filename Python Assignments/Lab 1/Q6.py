# 6. WAP to generate prime number series up to n

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime_series(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes
n = 50
print(f"Prime numbers up to {n}: {prime_series(n)}")