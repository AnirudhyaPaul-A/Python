# Write a program to find the sum of diagonal elements in a 2D array

def sum_of_diagonals(matrix, n):
    # Initialize the sum to 0
    diagonal_sum = 0

    # Sum the primary diagonal elements
    for i in range(n):
        diagonal_sum += matrix[i][i]

    return diagonal_sum

def main():
    # Take input for the size of the matrix (assuming it's a square matrix)
    n = int(input("Enter the size of the square matrix (n x n): "))

    # Create an empty 2D list to hold the matrix elements
    matrix = []

    # Take input for each row of the matrix
    print("Enter the elements of the matrix row by row:")
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    # Calculate the sum of diagonal elements
    diagonal_sum = sum_of_diagonals(matrix, n)

    # Output the result
    print("The sum of diagonal elements in the matrix is:", diagonal_sum)

if __name__ == "__main__":
    main()