import unittest
from algorithms import Algorithm as algo

class BinarySearch(unittest.TestCase):
    def test_find_index(self):
        sorted_array = [0,1,2,3,4,5,6]
        expected_idx = 3
        
        self.assertEqual(sorted_array[expected_idx], sorted_array[algo.binary_search(expected_idx, sorted_array)])

    def test_element_not_in_array_raises_RecursionError(self):
        sorted_array = [0,1,2,4,5,6]
        element_to_find = 3
        with self.assertRaises(RecursionError):
            algo.binary_search(element_to_find, sorted_array)

    def test_single_element_array_index_found(self):
        sorted_array = [1]
        element_to_find = 1
        expected = 0
        
        self.assertEqual(expected, algo.binary_search(element_to_find, sorted_array))

    def test_sorted_array_is_null_raises_TypeError(self):
        with self.assertRaises(TypeError):
            algo.binary_search(0, None)

    def test_sorted_array_has_null_elements_raises_TypeError(self):
        with self.assertRaises(TypeError):
            algo.binary_search(0, [None, 1, None, 2, None, 3])

    def test_sorted_array_has_mixed_types_raises_TypeError(self):
        with self.assertRaises(TypeError):
            algo.binary_search(0, [0, "1", 2, "3", 4, "5"])

    def test_guess_all_returns(self):
        expected = 0
        correct = 2
        guess = 2
        self.assertEqual(expected, algo.guess(correct, guess))
        
        expected = 1
        correct = 2
        guess = 3
        self.assertEqual(expected, algo.guess(correct, guess))
        
        expected = -1
        correct = 2
        guess = 1
        self.assertEqual(expected, algo.guess(correct, guess))

if __name__ == "__main__":
    unittest.main()