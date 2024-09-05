# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
example_array = [1, 2, 3, 4, 5]
reversed_array = reverse_list(example_array)
print("Original array:", example_array)
print("Reversed array:", reversed_array)
