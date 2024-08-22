# Write a program that accepts a string I. 1.reverses it. II. 2.checks whether it is a palindrome. III. 3.checks whether it ends with a specific substring. IV. 4.capitalize the first letter of each word in a string V. 5.check if a string is anagram of another string VI. 6.remove vowels from string VII. 7.find length of the longest word in a sentence

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def ends_with_substring(s, substring):
    return s.endswith(substring)

def capitalize_words(s):
    return s.title()

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char not in vowels])

def length_of_longest_word(sentence):
    words = sentence.split()
    return len(max(words, key=len))

# Example usage
input_string = "Able was I saw Elba"
substring = "Elba"
another_string = "Elba was I saw Able"

print("Original string:", input_string)

# 1. Reverse the string
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)

# 2. Check if it is a palindrome
print("Is palindrome?", is_palindrome(input_string))

# 3. Check if it ends with a specific substring
print(f"Does it end with '{substring}'?", ends_with_substring(input_string, substring))

# 4. Capitalize the first letter of each word
print("Capitalized:", capitalize_words(input_string))

# 5. Check if a string is an anagram of another string
print(f"Is '{input_string}' an anagram of '{another_string}'?", is_anagram(input_string.replace(" ", "").lower(), another_string.replace(" ", "").lower()))

# 6. Remove vowels from the string
print("String without vowels:", remove_vowels(input_string))

# 7. Find the length of the longest word in a sentence
sentence = "This is an example sentence"
print("Length of the longest word:", length_of_longest_word(sentence))