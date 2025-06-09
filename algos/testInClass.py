import unittest
from demo import bubble_sort

class TestBubbleSort(unittest.TestCase):

    def test_bubblesort_unsortedarray(self):
        expected_numbers = [1, 2, 3, 4, 5]
        unsorted = [4, 2, 3, 1, 5]
        self.assertEqual(bubble_sort(unsorted), expected_numbers)
    
    def test_sort_nullarray(self):
        with self.assertRaises(TypeError):
            bubble_sort(None)

if __name__ == "__main__":
    unittest.main()