# Write a python program to find duplicate elements in a 1D array and find their frequency of occurrence.

from collections import Counter

def find_duplicates(arr):
    count = Counter(arr)
    return {k: v for k, v in count.items() if v > 1}

array = [1, 2, 3, 2, 3, 4, 5]
print("Duplicates and their frequencies:", find_duplicates(array))