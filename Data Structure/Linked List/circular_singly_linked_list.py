class Node:
    def __init__(self, data):
        """
        Initialize a new node with the given data.

        Parameters:
        - data: The data to be stored in the node.
        """
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        """
        Initialize an empty Circular Singly Linked List.
        """
        self.start_node = None

    def is_empty(self):
        """
        Check if the circular linked list is empty.

        Returns:
        - True if the list is empty, False otherwise.
        """
        return self.start_node is None

    def append(self, data):
        """
        Append a new node with the given data at the end of the circular linked list.

        Parameters:
        - data: The data to be appended.
        """
        new_node = Node(data)
        if self.is_empty():
            self.start_node = new_node
        else:
            current_node = self.start_node
            while current_node.next != self.start_node:
                current_node = current_node.next
            current_node.next = new_node
        new_node.next = self.start_node

    def append_after(self, data, after_x):
        """
        Append a new node with the given data after a specified value (after_x).

        Parameters:
        - data: The data to be appended.
        - after_x: The value after which the new node should be inserted.
        """
        new_node = Node(data)
        if self.is_empty():
            self.start_node = new_node
        else:
            if self.start_node.data == after_x:
                new_node.next = self.start_node.next
                self.start_node.next = new_node
                return

            current_node = self.start_node
            while current_node.next != self.start_node:
                current_node = current_node.next
                if after_x == current_node.data:
                    break
            if after_x != current_node.data:
                print("Value", after_x, "not found in the list. Cannot append.")
            else:
                new_node.next = current_node.next
                current_node.next = new_node

    def delete(self):
        """
        Delete the last node in the circular linked list.
        """
        if self.is_empty():
            print('Linked List is empty')

        elif self.start_node.next == self.start_node:
            # If there is only one node, set start_node to None
            self.start_node = None

        else:
            current_node = self.start_node
            while current_node.next.next != self.start_node:
                current_node = current_node.next

            current_node.next = self.start_node

    def delete_by_value(self, del_x):
        """
        Delete a node with a specific value (del_x) in the circular linked list.

        Parameters:
        - del_x: The value to be deleted from the list.
        """
        if self.is_empty():
            print('Empty linked list')

        elif self.start_node.next == self.start_node:
            # If there is only one node, set start_node to None
            self.start_node = None
        else:
            if self.start_node.data == del_x:
                self.start_node = self.start_node.next

            current_node = self.start_node
            while current_node.next != self.start_node:
                if current_node.next.data == del_x:
                    break

                current_node = current_node.next

            if current_node.next.data == del_x:
                current_node.next = current_node.next.next
            else:
                print("Value", del_x, "not found in the list. Cannot DELETE.")

    def display(self):
        """
        Display the circular linked list.
        """
        if self.is_empty():
            print("Circular Singly Linked List is Empty!")
        else:
            current_node = self.start_node
            while True:
                print(current_node.data, end=" -> ")
                current_node = current_node.next
                if current_node == self.start_node:
                    break

    def display_updated(self, start_point=None):
        """
        Display the circular linked list with an updated starting point.

        Parameters:
        - start_point: The value to set as the new starting point. If None, the original starting point is used.
        """
        if self.is_empty():
            print("Circular Linked List is Empty!")
        else:

            if start_point is not None:
                current_node = self.start_node
                while True:
                    if current_node.data == start_point:
                        self.start_node = current_node
                        break
                    current_node = current_node.next
                    if current_node == self.start_node:
                        break

            current_node = self.start_node
            while True:
                print(current_node.data, end=' -> ')
                current_node = current_node.next
                if current_node == self.start_node:
                    break


# Example usage
if __name__ == "__main__":
    csll = CircularSinglyLinkedList()
    csll.append(10)
    csll.append(30)
    csll.append(50)
    csll.append_after(40, 30)
    csll.append_after(20, 10)
    csll.delete()
    csll.delete_by_value(30)
    csll.append_after(30, 20)
    csll.display()
    print()
    csll.display_updated(start_point=20)
    print()
    csll.append(130)
    csll.append(230)
    csll.display_updated(start_point=20)
