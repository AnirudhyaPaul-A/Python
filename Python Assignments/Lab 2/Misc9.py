# 9. Write a program to generate all combination of 1, 2, or 3 using loop.

def generate_combinations():
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                print(f"{i}{j}{k}")

# Example usage
generate_combinations()
