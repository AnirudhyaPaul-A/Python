# Write a program to search an element in an array.


# Python program to search an element in an array
def main():
    # Take input for the number of elements in the array
    n = int(input("Enter the number of elements in the array: "))

    # Create an empty list to hold the array elements
    array = []

    # Take input for each element of the array
    print("Enter the elements of the array:")
    for i in range(n):
        element = int(input())
        array.append(element)

    # Take input for the element to search for
    search_element = int(input("Enter the element to search for: "))

    # Search for the element in the array
    if search_element in array:
        index = array.index(search_element)
        print(f"Element {search_element} found at index {index}")
    else:
        print(f"Element {search_element} not found in the array.")

if __name__ == "__main__":
    main()