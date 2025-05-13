def insertion_sort_desc(arr):
    """
    Sorts an array in-place in monotonically decreasing order using the Insertion Sort algorithm.

    Insertion Sort operates incrementally by growing a sorted subsection of the array,
    placing each new element in its correct position relative to the previously sorted elements.

    Time Complexity: O(n^2) in the worst and average cases due to nested iterations.
    Space Complexity: O(1) since sorting is done in-place without extra memory usage.
    
    Parameters:
        arr (list): A list of comparable elements to be sorted.

    Returns:
        list: The sorted list in decreasing order.
    """
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be positioned into the sorted portion
        j = i - 1

        # Shift elements of the sorted section that are smaller than 'key' to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]  # Move smaller elements one position to the right
            j -= 1

        # Place 'key' in its correct location
        arr[j + 1] = key

    return arr
