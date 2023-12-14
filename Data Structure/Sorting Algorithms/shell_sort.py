def shell_sort(elements):
    """
    Perform Shell Sort on a list of elements.

    Parameters:
    - elements (list): The list of elements to be sorted.

    Returns:
    - None: The function modifies the input list in-place.

    Shell Sort works by dividing the input list into sublists and sorting them independently.
    It starts with a large gap and reduces it in each iteration until the entire list is sorted.
    """
    gap = len(elements) // 2
    while gap > 0:
        for i in range(gap, len(elements)):
            val_to_sort = elements[i]
            j = i
            while val_to_sort < elements[j - gap] and j >= gap:
                elements[j] = elements[j - gap]
                j -= gap
            elements[j] = val_to_sort
        gap //= 2


if __name__ == "__main__":
    element_list = [3, 6, 2, 7, 8, 4, 9, 5, 1]
    print(f"Original list: {element_list}")
    shell_sort(element_list)
    print(f"Sorted list  : {element_list}")
