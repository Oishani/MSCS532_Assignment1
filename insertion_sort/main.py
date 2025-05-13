from sorter import insertion_sort_desc

def main():
    unsorted_array = [5, 2, 9, 1, 5, 6]
    print("Original array:", unsorted_array)
    sorted_array = insertion_sort_desc(unsorted_array)
    print("Sorted in decreasing order:", sorted_array)

if __name__ == "__main__":
    main()
