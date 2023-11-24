class BinarySearch:
    def __init__(self):
        """
        Initialize the BinarySearch object.

        Parameters:
        - None

        Attributes:
        - items (list): The list of items to perform binary search on.
        - search_val (int): The value to search for in the list.
        """
        self.items = items  # You might want to initialize these to meaningful values
        self.search_val = search_val

    def search(self):
        """
        Perform binary search on the list of items.

        Returns:
        - None

        Prints the result of the search.
        """
        low = 0
        high = len(self.items) - 1
        while low <= high:
            mid = (low + high) // 2

            # Check if the middle element is the target
            if self.items[mid] == self.search_val:
                print(f"Element {self.search_val} found at index {mid}")
                return  # Target found, exit the loop or return the index

            # If the middle element is less than the target, adjust the search range to the right half
            elif self.items[mid] < self.search_val:
                low = mid + 1

            # If the middle element is greater than the target, adjust the search range to the left half
            else:
                high = mid - 1

        print(f"Element {self.search_val} not found in the array")


if __name__ == "__main__":
    """
    Example usage of the BinarySearch class.
    """
    items = [10, 20, 30, 40, 50, 60, 70, 80]
    search_val = 80
    binary_search = BinarySearch()
    binary_search.items = items
    binary_search.search()
