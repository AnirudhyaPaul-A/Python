# Write a program to print transpose of matrix.

def transpose_matrix(matrix):
    return list(zip(*matrix))

def main():
    n = int(input("Enter the number of rows for the matrix: "))
    m = int(input("Enter the number of columns for the matrix: "))
    matrix = []
    print("Enter the matrix row by row:")
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    transposed = transpose_matrix(matrix)
    print("Transpose of the matrix:")
    for row in transposed:
        print('\t'.join(map(str, row)))

if __name__ == "__main__":
    main()