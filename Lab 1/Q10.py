# 10. WAP to generate the Fibonacci series upto n.

def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    while a <= n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
n = int(input("Enter a number: "))
fib_series = fibonacci_series(n)
print(f"Fibonacci series up to {n}: {fib_series}")