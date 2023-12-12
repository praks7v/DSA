def bubble_sort(elements):
    """
    Sorts a list of elements using the Bubble Sort algorithm.

    Parameters:
    - elements (list): The list of elements to be sorted.

    Returns:
    - None: The list is sorted in-place, and there is no need to return a new list.
    """
    # Traverse through the entire list in reverse order
    for i in range(len(elements) - 1, 0, -1):
        # Iterate through the unsorted part of the list
        # j is started from 1st and j+1 is 2nd element till last
        # range i decrement the last sorted element
        for j in range(i):
            # Compare adjacent elements and swap them if they are in the wrong order
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]


if __name__ == "__main__":
    # Example usage:
    element_list = [4, 3, 7, 1, 6, 9, 8, 5, 2]

    # Call the bubble_sort function to sort the list
    bubble_sort(element_list)

    # Print the sorted list
    print(element_list)
