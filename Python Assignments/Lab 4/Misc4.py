# Reverse the elements in an array of integers without using a second array

def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def main():
    arr = list(map(int, input("Enter integers for the array separated by spaces: ").split()))
    reverse_array(arr)
    print(f"Reversed array: {' '.join(map(str, arr))}")

if __name__ == "__main__":
    main()