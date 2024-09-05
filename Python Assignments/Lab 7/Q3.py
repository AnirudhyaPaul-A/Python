#3. Write a python program to implement gradient descent.

def gradient_descent(learning_rate, num_iterations):
    x = float(input("Enter the initial value of x: "))
    for i in range(num_iterations):
        grad = 2 * x # Gradient of f(x) = x^2 is f'(x) = 2x
        x = x - learning_rate * grad
        print(f"Iteration {i+1}: x = {x}, f(x) = {x**2}")
    return x
learning_rate = float(input("Enter the learning rate: "))
num_iterations = int(input("Enter the number of iterations: "))
final_x = gradient_descent(learning_rate, num_iterations)
print(f"Final value of x after {num_iterations} iterations is {final_x}")
