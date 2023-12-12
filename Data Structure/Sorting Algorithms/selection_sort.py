def selection_sort(elements):
    """
    Sorts a list of elements using the Selection Sort algorithm.

    Parameters:
    - elements (list): The list of elements to be sorted.

    Returns:
    - None: The list is sorted in-place, and there is no need to return a new list.
    """
    # Traverse through the entire list
    for i in range(len(elements)):
        # Assume the current position is the minimum
        min_pos = i

        # Find the minimum element in the unsorted part of the list
        for j in range(i, len(elements)):
            if elements[j] < elements[min_pos]:
                min_pos = j

        # Swap the found minimum element with the first element in the unsorted part
        elements[i], elements[min_pos] = elements[min_pos], elements[i]


if __name__ == "__main__":
    # Example usage:
    element_list = [4, 2, 5, 6, 8, 7, 9, 1, 3]

    # Call the selection_sort function to sort the list
    selection_sort(element_list)

    # Print the sorted list
    print(element_list)
