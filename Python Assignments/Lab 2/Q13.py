# 13. Write a Python program to print the first 6 terms of a geometric sequence starting with 2 and having a common ratio of 3.

def geometric_sequence(start, ratio, terms):
    sequence = []
    current_term = start
    for _ in range(terms):
        sequence.append(current_term)
        current_term *= ratio
    return sequence

# Define the starting term, common ratio, and number of terms
start_term = 2
common_ratio = 3
number_of_terms = 6

# Generate the sequence
sequence = geometric_sequence(start_term, common_ratio, number_of_terms)

# Print the sequence
print("The first 6 terms of the geometric sequence are:", sequence)
