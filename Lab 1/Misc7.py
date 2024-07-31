# 7. Program to check if a number is Positive or Negative

number = float(input("Enter a number: "))
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print(f"{number} is zero.")