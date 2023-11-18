class Node:
    """
    Node class represents a node in a linked list.

    Attributes:
        data: The data stored in the node.
        next: Reference to the next node in the linked list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    LinkedList class represents a singly linked list.

    Attributes:
        head: Reference to the first node in the linked list.
    """

    def __init__(self):
        self.head = None

    def append_end(self, data):
        """
        Appends a new node with the given data to the end of the linked list.

        Parameters:
            data: The data to be added to the new node.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def append_begin(self, data):
        """
        Adds a new node with the given data to the beginning of the linked list.

        Parameters:
            data: The data to be added to the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append_after(self, data, x):
        """
        Adds a new node with the given data after a node with the specified value 'x'.

        Parameters:
            data: The data to be added to the new node.
            x: The value of the node after which the new node should be added.
        """
        node = self.head
        while node is not None:
            if x == node.data:
                break
            node = node.next
        if node is None:
            print('Node is not present. Enter the correct node')
        else:
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node

    def append_before(self, data, x):
        """
        Adds a new node with the given data before a node with the specified value 'x'.

        Parameters:
            data: The data to be added to the new node.
            x: The value of the node before which the new node should be added.
        """
        if self.head is None:
            return

        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        node = self.head
        while node.next is not None:
            if x == node.next.data:
                break
            node = node.next

        if node.next is None:
            print('Node is not present. Enter the correct node')

        else:
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node

    def del_begin_node(self):
        """Deletes the first node in the linked list."""
        if self.head is not None:
            self.head = self.head.next

    def del_end_node(self):
        """Deletes the last node in the linked list."""
        if self.head is None:
            return
        node = self.head
        while node.next.next is not None:
            node = node.next
        node.next = None

    def del_node(self, x):
        """
        Deletes the node with the specified value 'x' from the linked list.

        Parameters:
            x: The value of the node to be deleted.
        """
        if self.head is None:
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        node = self.head
        while node is not None:
            if node.next.data == x:
                break
            node = node.next
        node.next = node.next.next

    def print_list(self):
        """Prints the elements of the linked list."""
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print('None')


# Example Usage:
if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.append_end(1)
    linkedlist.append_end(2)
    linkedlist.append_end(3)
    linkedlist.del_begin_node()
    linkedlist.append_end(6)
    linkedlist.append_begin(1)
    linkedlist.append_begin(8)
    linkedlist.append_after(4, 3)
    linkedlist.append_before(5, 6)
    linkedlist.del_end_node()
    linkedlist.del_node(8)
    linkedlist.print_list()
