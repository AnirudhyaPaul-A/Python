# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

if __name__ == "__main__":
    input_string = input("Enter a string:")
    if input_string.lower() in ["yes", "yes", "Yes"]:
        print("Yes")
    else:
          print("No")