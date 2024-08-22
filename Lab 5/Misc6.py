# Write a python program where elements of two integer arrays get added index wise and get stored into a third array.

def add_arrays(arr1, arr2):
    return [x + y for x, y in zip(arr1, arr2)]

a = [1, 2, 3]
b = [4, 5, 6]
print("Added array:", add_arrays(a, b))