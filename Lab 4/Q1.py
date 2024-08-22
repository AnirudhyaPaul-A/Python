# Write a program to enter a string. Calculate the length of the string. Find the substring country. Count the occurences of each word in the given sentence. If the String as input is India is my motherland. I love my country. Capital of India is New Delhi.

def count_word_occurrences(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word = word.lower().strip('.')
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
def find_substring(sentence, substring):
    if substring in sentence:
        return True
    else:
        return False
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    string_length = len(input_string)
    print(f"Length of the string: {string_length}")
    substring = "country"
    is_substring_present = find_substring(input_string, substring)
    print(f"Is the substring '{substring}' present in the string? {'Yes' if is_substring_present else 'No'}")
    word_count = count_word_occurrences(input_string)
    print("Occurrences of each word in the given sentence:")
    for word, count in word_count.items():
        print(f"{word}: {count}")