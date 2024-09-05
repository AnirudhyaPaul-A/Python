# Write a python program which counts the non-zero elements in an integer array.

def count_non_zero(arr):
    return sum(1 for x in arr if x != 0)

array = [0, 1, 2, 0, 3, 4, 0]
print("Number of non-zero elements:", count_non_zero(array))