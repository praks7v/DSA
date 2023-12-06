class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.rear = -1
        self.front = 0
        self.size = 0

    def enqueue(self, item):
        if self.size < self.capacity:
            self.rear = (self.rear + 1) % self.capacity
            self.items[self.rear] = item
            self.size += 1
            self._heapify_up(self.rear)
        else:
            return None

    def _heapify_up(self, index):
        # index = len(self.items) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.items[index] < self.items[parent_index]:
                self.items[index], self.items[parent_index] = self.items[parent_index], self.items[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index=0):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index
            if left_child_index < self.size and self.items[left_child_index] < self.items[smallest]:
                smallest = left_child_index
            if right_child_index < self.size and self.items[right_child_index] < self.items[smallest]:
                smallest = right_child_index

            if smallest != index:
                self.items[index], self.items[smallest] = self.items[smallest], self.items[index]
                index = smallest
            else:
                break

    def extract_min(self):
        if self.size == 0:
            return None

        root = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.items[self.size - 1] = None
        self.size -= 1
        self._heapify_down()
        return root


if __name__ == "__main__":
    pq = PriorityQueue(7)
    pq.enqueue(2)
    pq.enqueue(3)
    pq.enqueue(5)
    pq.enqueue(6)
    pq.enqueue(8)
    pq.enqueue(1)
    pq.enqueue(9)
    pq.extract_min()
    while pq.size > 0:
        print(pq.extract_min(), end=' ')
    print()
