# Sample program to implement stack using array


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to the stack.")

    def pop(self):
        if self.is_empty():
            return "Stack is empty."
        return f"Popped {self.stack.pop()} from the stack."

    def display(self):
        if self.is_empty():
            return "Stack is empty."
        return f"Current stack: {self.stack}"

def main():
    stack = Stack()

    while True:
        print("\nOptions:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = int(input("Enter the item to push: "))
            stack.push(item)
        elif choice == 2:
            print(stack.pop())
        elif choice == 3:
            print(stack.display())
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()