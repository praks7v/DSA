class PriorityQueue:
    def __init__(self, capacity):
        """
        Initializes a Priority Queue with the given capacity.

        Parameters:
        - capacity: The maximum number of elements the queue can hold.
        """
        self.capacity = capacity
        self.items = [None] * capacity
        self.rear = -1
        self.front = 0
        self.size = 0

    def enqueue(self, item):
        """
        Adds an item to the Priority Queue.

        Parameters:
        - item: The item to be added to the queue.

        Returns:
        - None if the queue is full; otherwise, adds the item to the queue.
        """
        if self.size < self.capacity:
            self.rear = (self.rear + 1) % self.capacity
            self.items[self.rear] = item
            self.size += 1
            self._heapify_up(self.rear)
        else:
            return None

    def _heapify_up(self, index):
        """
        Restores the heap property by moving the recently added element (at the end of the heap)
        upwards to its correct position.

        Parameters:
        - index: The index of the recently added element.
        """
        while index > 0:
            parent_index = (index - 1) // 2
            if self.items[index] < self.items[parent_index]:
                self.items[index], self.items[parent_index] = self.items[parent_index], self.items[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index=0):
        """
        Restores the heap property by moving the element at the given index downwards to its correct position.

        Parameters:
        - index: The index from which to start the heapify-down process.
        """
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
        """
        Removes and returns the minimum element from the Priority Queue.

        Returns:
        - None if the queue is empty; otherwise, returns the extracted minimum element.
        """
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
        print("Priority from lowest to highest value: ", pq.extract_min())
