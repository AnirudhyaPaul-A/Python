# Sample program to print 1 2 3 4 5 6 7 8 9

def print_pattern(rows):
    current_num = 1
    for i in range(1, rows + 1):
        for j in range(1, 2*i):
            print(current_num, end=' ')
            current_num += 1
        print()
def main():
    rows = 3
    print_pattern(rows)
if __name__ == "__main__":
    main()