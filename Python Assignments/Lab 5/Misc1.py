# Write a python program to check whether a given matrix is sparse or not.

def is_sparse(matrix):
    total_elements = len(matrix) * len(matrix[0])
    zero_count = sum(row.count(0) for row in matrix)
    return zero_count > total_elements / 2

matrix = [
    [5, 8, 0],
    [0, 4, 0],
    [2, 0, 8]
]

print("The matrix is sparse:", is_sparse(matrix))
