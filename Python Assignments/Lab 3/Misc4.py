# Sample program to calculate Sum & Average of an integer array

def calculate_sum_and_average(arr):
    total_sum = sum(arr)
    average = total_sum / len(arr) if len(arr) > 0 else 0
    return total_sum, average
def main():
    array = list(map(int, input("Enter the integers separated by spaces: ").split()))
    total_sum, average = calculate_sum_and_average(array)
    # Displaying the results
    print(f"Sum of the array: {total_sum}")
    print(f"Average of the array: {average}")
if __name__ == "__main__":
    main()