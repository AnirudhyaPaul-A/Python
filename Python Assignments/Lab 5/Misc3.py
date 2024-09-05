# Write a python program to find second highest element of an array.

def second_highest(arr):
    unique_arr = list(set(arr))
    unique_arr.sort()
    return unique_arr[-2] if len(unique_arr) > 1 else None

array = [10, 20, 4, 45, 99, 99]
print("Second highest element:", second_highest(array))
