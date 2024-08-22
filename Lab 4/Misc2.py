# Write a program to find the sum of even numbers in an integer array

def sum_of_even_numbers(array):
    # Initialize the sum to 0
    even_sum = 0

    # Iterate through the array
    for num in array:
        # Check if the number is even
        if num % 2 == 0:
            even_sum += num

    return even_sum

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

    # Calculate the sum of even numbers
    even_sum = sum_of_even_numbers(array)

    # Output the result
    print("The sum of even numbers in the array is:", even_sum)

if __name__ == "__main__":
    main()