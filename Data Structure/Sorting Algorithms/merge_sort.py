def merge_sort(elements):
    """
    Sorts a list in ascending order using the Merge Sort algorithm.

    Parameters:
    - elements (list): The list to be sorted.

    Returns:
    - list: The sorted list.
    """
    # Base case: if the length of the list is 1 or less, it is already sorted
    if len(elements) <= 1:
        return elements

    # Find the middle index of the list
    mid = len(elements) // 2

    # Divide the list into two halves
    left_half = elements[:mid]
    right_half = elements[mid:]

    # Recursively apply merge_sort to both halves
    merge_sort(left_half)
    merge_sort(right_half)

    # Merge the sorted halves
    merge(elements, left_half, right_half)


def merge(elements, left, right):
    """
    Merges two sorted lists into a single sorted list.

    Parameters:
    - elements (list): The main list to be modified and merged.
    - left (list): The left half of the elements.
    - right (list): The right half of the elements.

    Returns:
    - None: The merged result is directly modified in the 'elements' list.
    """
    i = j = k = 0

    # Compare elements from left and right halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            elements[k] = left[i]
            i += 1
        else:
            elements[k] = right[j]
            j += 1
        k += 1

    # Check for any remaining elements in both left and right halves
    while i < len(left):
        elements[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        elements[k] = right[j]
        j += 1
        k += 1


if __name__ == "__main__":
    # Example usage
    element_list = [4, 2, 5, 7, 9, 8, 1, 3, 6]
    merge_sort(element_list)
    print("Sorted List:", element_list)
