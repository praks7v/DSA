def quick_sort(elements):
    # Base case: If the length of the list is 1 or less, it is already sorted
    if len(elements) <= 1:
        return elements

    # Choose the pivot (in this case, the last element)
    pivot = elements[-1]

    # Alternative way to initialize items_lower and items_greater using list comprehensions
    # This is commented out as it's an alternative to the explicit for loop below
    # items_lower = [x for x in elements[:-1] if x <= pivot]
    # items_greater = [x for x in elements[:-1] if x > pivot]

    # Initialize lists to store elements less than or equal to the pivot, and greater than the pivot
    items_lower = []
    items_greater = []

    # Partition the list into items_lower and items_greater
    for item in elements[:-1]:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    # Recursively sort the sublists and concatenate them with the pivot in between
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


if __name__ == "__main__":
    # Example usage
    element_list = [4, 2, 5, 7, 9, 8, 1, 3, 6]
    sorted_list = quick_sort(element_list)
    print("Original List:", element_list)
    print("Sorted List  :", sorted_list)
