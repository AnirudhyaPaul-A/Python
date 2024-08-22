# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again Then, the output should be: again and hello makes perfect practice world

if __name__ == "__main__":
    input_string = input("Enter a sequence of whitespace-separated words: ")
    words = input_string.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    sorted_string = ' '.join(sorted_words)
    print(sorted_string)