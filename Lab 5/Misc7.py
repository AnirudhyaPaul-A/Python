# Write a python program to multiply two matrices.

def get_matrix_input(rows, cols):
    matrix = []
    print(f"Enter the elements of the matrix ({rows}x{cols}):")
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix

def multiply_matrices(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

rows_A = int(input("Enter the number of rows for matrix A: "))
cols_A = int(input("Enter the number of columns for matrix A : "))
rows_B = int(input("Enter the number of rows for matrix B: "))
cols_B = int(input("Enter the number of columns for matrix B: "))

print("Matrix A:")
A = get_matrix_input(rows_A, cols_A)
print("Matrix B:")
B = get_matrix_input(rows_B, cols_B)

if cols_A != rows_B:
    print("Matrices cannot be multiplied.")
else:
  result = multiply_matrices(A, B)


print("Product of matrices:")
for row in result:
    print(row)