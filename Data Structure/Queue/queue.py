class Queue:
    def __init__(self, capacity):
        """
        Initialize a Queue with a specified capacity.

        Parameters:
            capacity (int): The maximum number of elements the queue can hold.
        """
        self.capacity = capacity
        self.items = [None] * capacity
        self.rear = -1
        self.front = 0
        self.size = 0

    def enqueue(self, item):
        """
        Enqueue (add) an element to the rear of the queue.

        Parameters:
            item: The element to be enqueued.

        Prints:
            A message indicating the enqueued element and the current state of the queue.
            If the queue is full, it prints a message indicating that the element cannot be enqueued.
        """
        if self.size < self.capacity:
            self.rear = (self.rear + 1) % self.capacity
            self.items[self.rear] = item
            self.size += 1
            print(f'Enqueue {item}. Queue {self.items}')
        else:
            print(f'Queue is full! Capacity: {self.size} Cannot enqueue.')
            return None

    def dequeue(self):
        """
        Dequeue (remove) an element from the front of the queue.

        Returns:
            The dequeued element.

        Prints:
            A message indicating the dequeued element and the current state of the queue.
            If the queue is empty, it prints a message indicating that the queue is empty and cannot be dequeued.
        """
        if self.size > 0:
            front_element = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            print(f"Dequeue {front_element}. Queue {self.items}")
            return front_element
        else:
            print(f'Queue is empty! Cannot dequeue.')
            return None


if __name__ == "__main__":
    # Example usage
    queue = Queue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print()
    queue.dequeue()
    queue.dequeue()
