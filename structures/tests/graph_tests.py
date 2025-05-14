import unittest
from structures.graphs.tree import BinarySearchTree as t

class TreeTests(unittest.TestCase):
    def test_tree_string(self):
        tree = t()
        expected = "[ 1, 2, 3 ]"
        tree.add(2)
        tree.add(1)
        tree.add(3)
        
        self.assertEqual(expected, str(tree))
    
    def test_tree_string_empty(self):
        tree = t()
        expected = "[ ]"
        
        self.assertEqual(expected, str(tree))
    
    def test_tree_add(self):
        tree = t()
        expected = "[ 4, 5, 6 ]"
        
        tree.add(5)
        tree.add(6)
        tree.add(4)
        
        self.assertEqual(expected, str(tree))
    
    def test_tree_add_duplicate(self):
        tree = t()
        expected = "[ 1, 2, 2, 3 ]"
        
        tree.add(2)
        tree.add(2)
        tree.add(1)
        tree.add(3)
        
        self.assertEqual(expected, str(tree))
    
    def test_tree_clear(self):
        tree = t()
        expected = "[ ]"
        tree.add(1)
        tree.add(2)
        tree.add(3)
        tree.add(4)
        
        tree.clear()
        
        self.assertEqual(expected, str(tree))
    
    def test_tree_clear_empty(self):
        tree = t()
        expected = "[ ]"
        
        tree.clear()
        
        self.assertEqual(expected, str(tree))
    
    def test_tree_count(self):
        tree = t()
        expected = 3
        tree.add(1)
        tree.add(2)
        tree.add(3)
        
        self.assertEqual(expected, tree._count)
    
    def test_tree_grab_all_values(self):
        tree = t()
        expected = [1, 2, 3]
        tree.add(2)
        tree.add(3)
        tree.add(1)
        actual = list()
        
        tree._traverse_grab_all_values(tree._root, actual)
        
        self.assertEqual(expected, actual)
    
    def test_tree_grab_all_values_empty_raises_exception(self):
        tree = t()
        with self.assertRaises(AttributeError):
            tree_list = list()
            tree._traverse_grab_all_values(tree._root, tree_list)
    
    def test_tree_to_list(self): # uses _traverse_grab_all_values in to_list
        tree = t()
        expected = [1, 2, 3]
        tree.add(1)
        tree.add(3)
        tree.add(2)
        
        actual = tree.to_list()
        
        self.assertEqual(expected, actual)
    
    def test_tree_to_list_duplicates(self):
        tree = t()
        expected = [1, 2, 2, 3]
        tree.add(1)
        tree.add(3)
        tree.add(2)
        tree.add(2)
        
        actual = tree.to_list()
        
        self.assertEqual(expected, actual)
    
    def test_tree_to_list_empty(self):
        tree = t()
        expected = []
        
        actual = tree.to_list()
        
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()