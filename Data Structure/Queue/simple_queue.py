class SimpleQueue:
    def __init__(self):
        """
        Initialize an empty SimpleQueue.

        Attributes:
            items (list): List to hold queue elements.
        """
        self.items = []

    def enqueue(self, item):
        """
        Enqueue (add) an element to the rear of the queue.

        Args:
            item: The element to be enqueued.

        Prints:
            A message indicating the enqueued element and the current state of the queue.
        """
        self.items.append(item)
        print(f"Enqueue {item}. Queue {self.items}")

    def dequeue(self):
        """
        Dequeue (remove) an element from the front of the queue.

        Returns:
            The dequeued element.

        Prints:
            A message indicating the dequeued element and the current state of the queue.
            If the queue is empty, a message indicating that the queue is empty and cannot be dequeued.
        """
        if not self.is_empty():
            front_element = self.items.pop(0)
            print(f"Dequeue {front_element}. Queue {self.items}")
            return front_element
        else:
            print("Queue is empty. Cannot Dequeue.")
            return None

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return not self.items


if __name__ == "__main__":
    simple_queue = SimpleQueue()
    print("Enqueue Operation:")
    simple_queue.enqueue(10)
    simple_queue.enqueue(20)
    simple_queue.enqueue(30)
    simple_queue.enqueue(40)
    print("\nDequeue Operation:")
    simple_queue.dequeue()
    simple_queue.dequeue()
