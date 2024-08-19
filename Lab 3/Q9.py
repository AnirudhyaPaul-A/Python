# 9. Print the pattern upto N Lines:

#  .
# /_\
# N=2
#   .
#  / \
# /___\
#  N=3

#   .
#  / \
#  / \
# /_____\
#  N=4

def print_pattern(N):
    # Loop through each level
    for i in range(1, N+1):
        # Calculate the width of the base of the triangle for the current level
        base_width = 2 * i - 1

        # Calculate the leading spaces for centering the triangle
        leading_spaces = N - i

        # Print the top of the triangle (a dot)
        print(" " * leading_spaces + ".")

        # Print the sides of the triangle (if i > 1)
        for j in range(1, i):
            print(" " * (leading_spaces - j) + "/" + " " * (2 * j - 1) + "\\")

        # Print the base of the triangle
        print(" " * (leading_spaces - i) + "/" + "_" * base_width + "\\")

N = 4  # Number of lines
print_pattern(N)
