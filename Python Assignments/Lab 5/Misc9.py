# Write a python program to print every alternate number of a given array.

def print_alternate(arr):
    return arr[::2]

array = [1, 2, 3, 4, 5, 6]
print("Every alternate number:", print_alternate(array))