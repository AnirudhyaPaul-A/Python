# Sample program to find the range of a 1D array

def find_range(arr):
    if len(arr) == 0:
        return 0
    return max(arr) - min(arr)
def main():
    array = list(map(int, input("Enter the integers separated by spaces: ").split()))
    range_value = find_range(array)
    print(f"The range of the array is: {range_value}")
if __name__ == "__main__":
    main()