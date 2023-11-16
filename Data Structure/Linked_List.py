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

    def del_begin_node(self):
        if self.head is not None:
            self.head = self.head.next

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
linkedlist.append(4)
print(linkedlist.print_list())
