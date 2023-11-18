class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def print_forward(self):
        node = self
        while node is not None:
            print(node.data, end=' - ')
            node = node.next
        print('None')

    def print_backward(self):
        node = self.next
        while node.next is not None:
            node = node.next

        while node is not None:
            print(node.data, end=' - ')
            node = node.prev
        print('None')


node1 = Node(20)
node2 = Node(10)
node3 = Node(5)
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node1.print_forward()
node1.print_backward()
