# Sample program to display prime numbers between a given interval


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes
def main():
    start = int(input("Enter the starting number of the interval: "))
    end = int(input("Enter the ending number of the interval: "))
    if start > end:
        print("Invalid interval. The starting number must be less than or equal to the ending number.")
    else:
        primes = find_primes(start, end)
        print(f"Prime numbers between {start} and {end}: {primes}")
if __name__ == "__main__":
    main()