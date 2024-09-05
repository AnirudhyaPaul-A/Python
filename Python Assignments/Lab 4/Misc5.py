# Write a program to enter n elements in an array and find smallest number among them.

def find_smallest_number(arr):
    if not arr:
        return None
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

arr = list(map(int, input("Enter integers for the array separated by spaces: ").split()))
smallest_number = find_smallest_number(arr)
if smallest_number is not None:
    print(f"Smallest number in the array: {smallest_number}")