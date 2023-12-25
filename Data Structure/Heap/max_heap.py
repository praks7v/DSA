class MaxHeap:
    def __init__(self):
        """
        Initializes an empty MaxHeap.
        """
        self.heap = []

    def insert(self, data):
        """
        Inserts a new element into the MaxHeap and maintains the heap property by performing _heapify_up.

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
            if self.heap[index] > self.heap[parent_index]:
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
            highest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[highest]:
                highest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[highest]:
                highest = right_child_index

            if highest != index:
                self.heap[index], self.heap[highest] = self.heap[highest], self.heap[index]
                index = highest
            else:
                break

    def extract_max(self):
        """
        Extracts the maximum element from the MaxHeap and maintains the heap property by performing _heapify_down.
        Returns the extracted maximum element.
        """
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]

        # Swap root with the last element and then remove the last element
        last_index = len(self.heap) - 1
        self.heap[0], self.heap[last_index] = self.heap[last_index], self.heap[0]
        self.heap.pop()

        # Perform heapify-down to maintain the heap property
        self._heapify_down()

        return root


if __name__ == "__main__":
    max_heap = MaxHeap()
    max_heap.insert(4)
    max_heap.insert(5)
    max_heap.insert(2)
    max_heap.insert(7)
    max_heap.insert(1)
    max_heap.insert(9)
    max_heap.insert(8)
    max_heap.insert(3)

    print("Max Heap:", max_heap.heap)

    extracted_max = max_heap.extract_max()
    print("Extracted Max Element:", extracted_max)
    print("Updated Max Heap:", max_heap.heap)
