class MinHeap:
    def __init__(self):
        """
        Initializes an empty MinHeap.
        """
        self.heap = []

    def insert(self, data):
        """
        Inserts a new element into the MinHeap and maintains the heap property by performing _heapify_up.

        Parameters:
        - data: The element to be inserted.
        """
        self.heap.append(data)
        self._heapify_up()

    def _heapify_up(self):
        """
        Restores the heap property by moving the recently added element (at the end of the heap)
        upwards to its correct position.
        """
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
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

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def extract_min(self):
        """
        Extracts the minimum element from the MinHeap and maintains the heap property by performing _heapify_down.
        Returns the extracted minimum element.
        """
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]

        # Swap root with the last element and then remove the last element
        self.heap[0] = self.heap.pop()

        # Alternatively, you can use the commented-out code below to first swap, then remove
        # last_element = len(self.heap) - 1
        # self.heap[0], self.heap[last_element] = self.heap[last_element], self.heap[0]
        # extracted_element = self.heap.pop()

        # Perform heapify-down to maintain the heap property
        self._heapify_down()

        return root


if __name__ == "__main__":
    min_heap = MinHeap()
    list1 = [3, 5, 6, 7, 9, 8, 2]
    for i in list1:
        min_heap.insert(i)

    print("Min Heap: ", min_heap.heap)

    extracted_min = min_heap.extract_min()
    print("Extracted Minimum Element: ", extracted_min)
    print("Updated Min Heap: ", min_heap.heap)
