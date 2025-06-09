import unittest
from basic_functions import BasicFunctions as bf


class BasicFunctionsTests(unittest.TestCase):
    def test_compare_two_nums_true(self):
        funcs = bf()
        
        self.assertTrue(funcs.compare_two(3, 3))

    def test_compare_two_strings_true(self):
        funcs = bf()
        
        self.assertTrue(funcs.compare_two("hello there", "hello there"))

    def test_max_different_nums(self):
        funcs = bf()
        maximum = 10
        not_maximum = 3
        
        self.assertEqual(maximum, funcs.max(maximum, not_maximum))

if __name__ == "__main__":
    unittest.main()