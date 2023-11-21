class Node:
    """
        Initialize a new node with the given data.

        Parameters:
        - data: The data to be stored in the node.
        """

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:

    def __init__(self):
        """
        Initialize an empty Circular Doubly Linked List.
        """
        self.start_node = None

    def append(self, data):
        """
        Append a new node with the given data at the end of the circular doubly linked list.

        Parameters:
        - data: The data to be appended.
        """
        new_node = Node(data)
        if not self.start_node:
            self.start_node = new_node
            self.start_node.next = new_node
            self.start_node.prev = new_node
            return
        current_node = self.start_node
        while current_node.next != self.start_node:
            current_node = current_node.next

        new_node.prev = current_node
        new_node.next = self.start_node
        self.start_node.prev = new_node
        current_node.next = new_node

    def append_by_value(self, after_x, data):
        """
        Append a new node with the given data after a specified value (after_x).

        Parameters:
        - after_x: The value after which the new node should be inserted.
        - data: The data to be appended.
        """
        new_node = Node(data)
        if not self.start_node:
            print("List is empty. Cannot append after value", after_x)
            return

        if self.start_node.data == after_x:
            new_node.prev = self.start_node
            new_node.next = self.start_node.next
            self.start_node.next.prev = new_node
            self.start_node.next = new_node
            return

        current_node = self.start_node
        while current_node.next != self.start_node:

            if current_node.data == after_x:
                break
            current_node = current_node.next

        if current_node.data != after_x:
            print("Value", after_x, "not found in the list. Cannot append.")
        else:
            new_node.prev = current_node
            new_node.next = current_node.next
            current_node.next.prev = new_node
            current_node.next = new_node

    def del_node(self):
        """
        Delete the last node in the circular doubly linked list.
        """
        if not self.start_node:
            return
        if self.start_node.next == self.start_node:
            self.start_node = None
            return
        current_node = self.start_node
        while current_node.next.next != self.start_node:
            current_node = current_node.next

        self.start_node.prev = current_node
        current_node.next = self.start_node

    def del_by_value(self, del_x):
        """
        Delete a node with a specific value (del_x) in the circular doubly linked list.

        Parameters:
        - del_x: The value to be deleted from the list.
        """
        if not self.start_node:
            return
        elif self.start_node == self.start_node.next and self.start_node.data == del_x:
            self.start_node = None
        else:

            current_node = self.start_node
            while current_node.next != self.start_node:

                if current_node.next.data == del_x:
                    break
                current_node = current_node.next

            if self.start_node.data == del_x:
                self.start_node = self.start_node.next
                self.start_node.prev = current_node
                current_node.next = self.start_node
                return
            elif current_node.next.data == del_x:
                current_node.next.next.prev = current_node
                current_node.next = current_node.next.next

            else:
                print("Value", del_x, "not found in the list. Cannot DELETE.")

    def display_forward(self):
        """
        Display the circular doubly linked list in forward traversal.
        """
        if self.start_node is None:
            print('Empty Linked List')
        else:
            current_node = self.start_node
            while True:
                print(current_node.data, end=' <-> ')
                current_node = current_node.next
                if current_node == self.start_node:
                    break

    def display_backward(self):
        """
        Display the circular doubly linked list in backward traversal.
        """
        if not self.start_node:
            print('Empty Linked List')
        else:
            current_node = self.start_node.prev
            while True:
                print(current_node.data, end=' <-> ')
                current_node = current_node.prev
                if current_node == self.start_node.prev:
                    break

    def display_forward_updated(self, start_point=None):
        """
        Display the circular doubly linked list in forward traversal with an updated starting point.

        Parameters:
        - start_point: The value to set as the new starting point. If None, the original starting point is used.
        """
        if not self.start_node:
            print('Empty Linked List')
        else:
            if start_point is not None:
                current_node = self.start_node
                while True:
                    if current_node.data == start_point:
                        self.start_node = current_node
                        break
                    current_node = current_node.next
                    if self.start_node == current_node:
                        break
                current_node = self.start_node
                while True:
                    print(current_node.data, end=' <-> ')
                    current_node = current_node.next
                    if current_node == self.start_node:
                        break

    def display_backward_updated(self, start_point=None):
        """
        Display the circular doubly linked list in backward traversal with an updated starting point.

        Parameters:
        - start_point: The value to set as the new starting point. If None, the original starting point is used.
        """
        if not self.start_node:
            print('Linked List is empty')

        else:
            if start_point is not None:
                current_node = self.start_node.prev
                while True:
                    if current_node.data == start_point:
                        self.start_node = current_node
                        break
                    current_node = current_node.prev
                    if current_node == self.start_node.prev:
                        break
                current_node = self.start_node
                while True:
                    print(current_node.data, end=' <-> ')
                    current_node = current_node.prev
                    if current_node == self.start_node:
                        break


if __name__ == "__main__":
    # Example usage of CircularDoublyLinkedList class
    circular_dll = CircularDoublyLinkedList()

    circular_dll.append(60)
    circular_dll.append(70)
    circular_dll.append(80)
    circular_dll.append(90)

    circular_dll.append_by_value(90, 100)

    circular_dll.del_node()
    circular_dll.del_by_value(60)
    circular_dll.append(100)
    circular_dll.append(101)

    print("\nForward traversal:")
    circular_dll.display_forward()

    print("\nBackward traversal:")
    circular_dll.display_backward()

    print("\nForward traversal from user input:")
    circular_dll.display_forward_updated(start_point=90)

    print("\nBackward traversal from user input:")
    circular_dll.display_backward_updated(start_point=90)
