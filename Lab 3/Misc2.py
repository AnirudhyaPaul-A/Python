# Sample program to check whether a given number is Armstrong Number or not


def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == number
def main():
    number = int(input("Enter a number to check if it is an Armstrong number: "))
    if is_armstrong(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
if __name__ == "__main__":
    main()