# Sample program to calculate Sum of two 2-dimensional arrays

def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements for a {rows}x{cols} matrix:")
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        if len(row) != cols:
            raise ValueError("The number of columns entered does not match the specified number of columns.")
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    print("Matrix 1:")
    matrix1 = input_matrix(rows, cols)

    print("Matrix 2:")
    matrix2 = input_matrix(rows, cols)

    sum_matrix = add_matrices(matrix1, matrix2)

    print("Sum of the two matrices:")
    for row in sum_matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
