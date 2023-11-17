class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def add_begin_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_after_node(self, data, x):
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

    def add_before_node(self, data, x):
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
        if self.head is not None:
            self.head = self.head.next

    def del_end_node(self):
        if self.head is None:
            return
        node = self.head
        while node.next.next is not None:
            node = node.next
        node.next = None

    def del_node(self, x):
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
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' -> ')
            current_node = current_node.next


linkedlist = LinkedList()
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.del_begin_node()
linkedlist.append(6)
linkedlist.add_begin_node(1)
linkedlist.add_begin_node(8)
linkedlist.add_after_node(4, 3)
linkedlist.add_before_node(5, 6)
linkedlist.del_end_node()
linkedlist.del_node(8)
print(linkedlist.print_list())
