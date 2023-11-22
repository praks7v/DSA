class Deque:
    """
    Implementation of a double-ended queue (deque) using a Python list.
    """

    def __init__(self):
        """
        Initializes an empty deque.
        """
        self.items = []

    def enqueue_front(self, item):
        """
        Adds an item to the front of the deque.

        Parameters:
        - item: The item to be added to the deque.
        """
        self.items.insert(0, item)
        print(f"Enqueue Front {item}. Deque {self.items}")

    def enqueue_rear(self, item):
        """
        Adds an item to the rear of the deque.

        Parameters:
        - item: The item to be added to the deque.
        """
        self.items.append(item)
        print(f"Enqueue rear {item}. Deque {self.items}")

    def dequeue_front(self):
        """
        Removes and returns the item from the front of the deque.
        """
        if not len(self.items) == 0:
            remove_front = self.items.pop(0)
            print(f"Dequeue Front {remove_front}. Deque {self.items}")
        else:
            print("Deque is empty. Cannot remove item.")

    def dequeue_rear(self):
        """
        Removes and returns the item from the rear of the deque.
        """
        if not len(self.items) == 0:
            remove_rear = self.items.pop()
            print(f"Dequeue rear {remove_rear}. Deque {self.items}")
        else:
            print("Deque is empty. Cannot remove item.")

    def size(self):
        """
        Returns the current size of the deque.
        """
        return len(self.items)


if __name__ == "__main__":
    # example usage
    deque = Deque()
    deque.enqueue_front(10)
    deque.enqueue_rear(20)
    deque.enqueue_rear(30)
    deque.enqueue_front(40)
    deque.enqueue_front(50)
    print()
    deque.dequeue_front()
    deque.dequeue_front()
    deque.dequeue_rear()
    print()
    print(f'Deque size is {deque.size()}')
