class Stack:
    def __init__(self):
        """
        Initialize an empty stack.

        Attributes:
            items (list): List to hold stack elements.
            top (int): Index representing the top of the stack. Initialized to -1 to indicate an empty stack.
        """
        self.items = []
        self.top = -1

    def push(self, item):
        """
        Push an element onto the stack.

        Args:
            item: The element to be pushed onto the stack.

        Prints:
            A message indicating the pushed element and the current state of the stack.
        """
        self.items.append(item)
        self.top += 1
        print(f"Pushed {item}. Stack: {self.items}")

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.top == -1

    def pop(self):
        """
        Pop an element from the stack.

        Returns:
            The popped element.

        Prints:
            A message indicating the popped element and the current state of the stack.
            If the stack is empty, a message indicating that the stack is empty and cannot be popped.
        """
        if not self.is_empty():
            top_element = self.items.pop()
            self.top -= 1
            print(f"Popped {top_element}. Stack: {self.items}")
            return top_element
        else:
            print("Stack is empty. Cannot pop.")


if __name__ == "__main__":
    # Example usage:
    my_stack = Stack()

    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)

    print()

    my_stack.pop()
    my_stack.pop()
