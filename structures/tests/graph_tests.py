import pdb
import unittest
from structures.graphs.tree import BinarySearchTree as t
from structures.graphs.avl_tree import AVLTree as atree

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
        
        tree._traverse_in_order(tree._root.left, actual)
        
        self.assertEqual(expected, actual)
    
    def test_tree_grab_all_values_empty_raises_exception(self):
        tree = t()
        with self.assertRaises(AttributeError):
            tree_list = list()
            tree._traverse_in_order(tree._root.left, tree_list)
    
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
    
    def test_tree_remove_on_right_side(self):
        tree = t()
        expected = "[ 1, 2, 3 ]"
        
        tree.add(1)
        tree.add(3)
        tree.add(2)
        tree.add(2)
        
        tree.remove(2)
        
        self.assertEqual(expected, str(tree))
    
    def test_tree_remove_on_left_side(self):
        tree = t()
        expected = "[ 2, 2, 3 ]"
        
        tree.add(2)
        tree.add(1)
        tree.add(3)
        tree.add(2)
        
        tree.remove(1)
        
        self.assertEqual(expected, str(tree))
    
    def test_tree_remove_root(self):
        tree = t()
        expected = "[ 2, 2, 3 ]"
        
        tree.add(1)
        tree.add(3)
        tree.add(2)
        tree.add(2)
        
        tree.remove(1)
        
        self.assertEqual(expected, str(tree))
    
    def test_remove_on_complex_tree(self):
        tree = t()
        expected = "[ 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ]"
        
        tree.add(8)
        tree.add(4)
        tree.add(2)
        tree.add(1)
        tree.add(3)
        tree.add(6)
        tree.add(5)
        tree.add(7)
        tree.add(12)
        tree.add(10)
        tree.add(9)
        tree.add(11)
        tree.add(14)
        tree.add(13)
        tree.add(15)
        
        tree.remove(4)
        
        self.assertEqual(expected, str(tree))
    
    def test_tree_count_after_remove(self):
        tree = t()
        expected = 4
        
        tree.add(1)
        tree.add(1)
        tree.add(1)
        tree.add(1)
        tree.add(1)
        
        tree.remove(1)
        
        self.assertEqual(expected, tree._count)
    
    def test_farthest_left(self):
        tree = t()
        expected = 1
        
        tree.add(4)
        tree.add(5)
        tree.add(3)
        tree.add(2)
        tree.add(1)
        
        actual = tree._farthest_left(tree._root.left).value
        
        self.assertEqual(expected, actual)
    
    def test_pre_order(self):
        tree = t()
        expected = "[5, 3, 1, 4, 6]"
        
        tree.add(5)
        tree.add(3)
        tree.add(1)
        tree.add(4)
        tree.add(6)
        
        self.assertEqual(expected, tree.pre_order_str())
    
    def test_post_order(self):
        tree = t()
        expected = "[1, 4, 3, 6, 5]"
        
        tree.add(5)
        tree.add(3)
        tree.add(1)
        tree.add(4)
        tree.add(6)
        
        self.assertEqual(expected, tree.post_order_str())
    
    def test_tree_contains_true(self):
        tree = t()
        
        tree.add(1)
        tree.add(2)
        tree.add(3)
        tree.add(4)
        tree.add(5)
        
        self.assertTrue(tree.contains(3))
    
    def test_tree_contains_false(self):
        tree = t()
        
        tree.add(1)
        tree.add(2)
        tree.add(3)
        tree.add(4)
        tree.add(5)
        
        self.assertTrue(not tree.contains(6))
    
    def test_is_empty_true(self):
        tree = t()
        
        self.assertTrue(tree._is_empty())
    
    def test_is_empty_false(self):
        tree = t()
        tree.add(1)
        
        self.assertTrue(not tree._is_empty())
    
    def test_tree_height(self):
        tree = t()
        tree.add(4)
        tree.add(3)
        tree.add(2)
        tree.add(1)
        tree.add(6)
        tree.add(7)
        tree.add(8)
        expected = 4
        
        actual = tree.height()
        
        self.assertEqual(expected, actual)
    
class AVLTreeTests(unittest.TestCase):
    def test_add(self):
        print("hello")
        tree = atree()
        expected = [1,2,3]
        
        tree.add(2)
        tree.add(1)
        tree.add(3)
        
        actual = tree.to_list("in") # "in" forces the tree to be made into an in-order array
        
        self.assertEqual(expected, actual)
    
    def test_in_order_list(self):
        tree = atree()
        expected = [1,2,3]
        
        tree.add(1)
        tree.add(2)
        tree.add(3)
        
        actual = tree.to_list("in")
        
        self.assertEqual(expected, actual)
    
    def test_breadth_first_list(self):
        tree = atree()
        expected = [2,1,3]
        
        tree.add(2)
        tree.add(1)
        tree.add(3)
        
        actual = tree.to_list() # breadth by default
        
        self.assertEqual(expected, actual)
    
    def test_rotation_left_works_add(self):
        tree = atree()
        expected = [2,1,3]
        
        tree.add(1)
        tree.add(2)
        tree.add(3)
        
        actual = tree.to_list()
        
        self.assertEqual(expected, actual)
    
    def test_rotation_right_works_add(self):
        tree = atree()
        expected = [2,1,3]
        
        tree.add(3)
        tree.add(2)
        tree.add(1)
        
        actual = tree.to_list()
        
        self.assertEqual(expected, actual)
    
    def test_rotation_left_right_works_add(self):
        tree = atree()
        expected = [2,1,3]
        
        tree.add(3)
        tree.add(1)
        tree.add(2)
        
        actual = tree.to_list()
        
        self.assertEqual(expected, actual)
    
    def test_rotation_right_left_works_add(self):
        tree = atree()
        expected = [2,1,3]
        
        tree.add(1)
        tree.add(3)
        tree.add(2)
        
        actual = tree.to_list()
        
        self.assertEqual(expected, actual)
    
    def test_rotation_left_works_remove(self):
        tree = atree()
        expected = [3,2,4]
        
        tree.add(2)
        tree.add(1)
        tree.add(3)
        tree.add(4)
        tree.remove(1)
        
        actual = tree.to_list()
        
        self.assertEqual(expected, actual)
    
    def test_rotation_right_works_remove(self):
        tree = atree()
        expected = [2,1,3]
        
        tree.add(3)
        tree.add(2)
        tree.add(4)
        tree.add(1)
        tree.remove(4)
        
        actual = tree.to_list()
        
        self.assertEqual(expected, actual)
    
    def test_rotation_left_right_works_remove(self):
        tree = atree()
        expected = [2,1,3]
        
        tree.add(3)
        tree.add(1)
        tree.add(4)
        tree.add(2)
        tree.remove(4)
        
        actual = tree.to_list()
        
        self.assertEqual(expected, actual)
    
    def test_rotation_right_left_works_remove(self):
        tree = atree()
        expected = [3,2,4]
        
        tree.add(2)
        tree.add(1)
        tree.add(4)
        tree.add(3)
        tree.remove(1)
        
        actual = tree.to_list()
        
        self.assertEqual(expected, actual)
    
    def test_add_duplicates_raises_error(self):
        tree = atree()
        with self.assertRaises(ValueError):
            tree.add(1)
            tree.add(1)

if __name__ == "__main__":
    unittest.main()