import unittest
from insertion_sort.sorter import insertion_sort_desc

class TestInsertionSort(unittest.TestCase):
    def test_ascending_sorted_array(self):
        self.assertEqual(insertion_sort_desc([1, 2, 3]), [3, 2, 1])

    def test_descending_sorted_array(self):
        self.assertEqual(insertion_sort_desc([5, 4, 3, 2]), [5, 4, 3, 2])

    def test_duplicates(self):
        self.assertEqual(insertion_sort_desc([4, 2, 4, 2]), [4, 4, 2, 2])

    def test_negative_numbers(self):
        self.assertEqual(insertion_sort_desc([-1, -3, -2]), [-1, -2, -3])

    def test_empty(self):
        self.assertEqual(insertion_sort_desc([]), [])

    def test_single_element(self):
        self.assertEqual(insertion_sort_desc([10]), [10])

if __name__ == '__main__':
    unittest.main()
