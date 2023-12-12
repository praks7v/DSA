def insertion_sort(elements):
    # Traverse through 1 to len(elements)
    for i in range(1, len(elements)):
        # Select the element to be compared
        value_to_sort = elements[i]

        # Move elements to the right (one position ahead) in the range [0, i-1]
        # if they are greater than the current value being sorted (value_to_sort).
        while i > 0 and value_to_sort < elements[i - 1]:
            # Swap the elements
            elements[i], elements[i - 1] = elements[i - 1], elements[i]
            # Move to the next element on the left
            i = i - 1


if __name__ == "__main__":
    # Example usage:
    element_list = [12, 3, 4, 5, 2, 1, 7, 8, 10, 11]

    # Call the insertion_sort function to sort the list
    insertion_sort(element_list)

    # Print the sorted list
    print(element_list)
