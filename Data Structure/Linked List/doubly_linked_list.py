class Node:
    def __init__(self, data):
        """
        Class representing a doubly linked list node.

        Parameters:
        - data: The data stored in the node.
        """
        self.data = data
        self.prev = None  # Reference to the previous node
        self.next = None  # Reference to the next node


class DoublyLinkedList:
    def __init__(self):
        """
        Class representing a doubly linked list.

        Attributes:
        - head: The head (first node) of the doubly linked list.
        """
        self.head = None

    def append_end(self, data):
        """
        Appends a new node with the given data at the end of the doubly linked list.

        Parameters:
        - data: The data to be stored in the new node.
        """
        new_node = Node(data)
        if not self.head:
            # If the list is empty, the new node becomes the head
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node

    def append_begin(self, data):
        """
        Appends a new node with the given data at the beginning of the doubly linked list.

        Parameters:
        - data: The data to be stored in the new node.
        """
        new_node = Node(data)
        if not self.head:
            # If the list is empty, the new node becomes the head
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def append_between(self, data, after_x):
        """
        Inserts a new node with the given data after the node with data equal to after_x.

        Parameters:
        - data: The data to be stored in the new node.
        - after_x: The data value after which the new node should be inserted.
        """
        new_node = Node(data)

        current_node = self.head
        while current_node is not None:
            if after_x == current_node.data:
                break
            current_node = current_node.next

        if current_node is None:
            print('Node not found')
        else:
            new_node.next = current_node.next
            new_node.prev = current_node
            current_node.next.prev = new_node
            current_node.next = new_node

    def del_begin(self):
        """Deletes the first node in the doubly linked list."""
        if not self.head:
            return

        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None

    def del_end(self):
        """Deletes the last node in the doubly linked list."""
        if not self.head:
            return

        if not self.head.next:
            # If there is only one node in the list
            self.head = None
            return

        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    def del_by_value(self, del_node):
        """
        Deletes the node with the given data value from the doubly linked list.

        Parameters:
        - del_node: The data value of the node to be deleted.
        """
        if not self.head:
            return
        if self.head.next is None:
            if self.head.data == del_node:
                self.head = None
            else:
                print('Given node is not present in Linked List')
            return

        if self.head.data == del_node:
            self.head = self.head.next
            self.head.prev = None

        current_node = self.head
        while current_node.next is not None:
            if del_node == current_node.data:
                break
            current_node = current_node.next

        if current_node.next:
            current_node.next.prev = current_node.prev
            current_node.prev.next = current_node.next
        else:
            if current_node.data == del_node:
                current_node.prev.next = None
            else:
                print("Given node is not present in Linked List")

    def print_forward(self):
        """Prints the doubly linked list in forward direction."""
        if not self.head:
            return print("Empty Linked List")

        node = self.head
        while node is not None:
            print(node.data, end=' <-> ')
            node = node.next
        print('None')

    def print_backward(self):
        """Prints the doubly linked list in backward direction."""
        if not self.head:
            return print("Empty Linked List")

        node = self.head
        while node.next is not None:
            node = node.next

        while node is not None:
            print(node.data, end=' <-> ')
            node = node.prev
        print('None')


# Example Usage:
if __name__ == '__main__':
    doubly_list = DoublyLinkedList()
    doubly_list.append_end(1)
    doubly_list.append_end(2)
    doubly_list.append_end(4)
    doubly_list.append_begin(0)
    doubly_list.append_between(3, 2)
    doubly_list.del_begin()
    doubly_list.del_end()
    doubly_list.del_by_value(3)

    print("\nForward traversal:")
    doubly_list.print_forward()

    print("\nBackward traversal:")
    doubly_list.print_backward()
