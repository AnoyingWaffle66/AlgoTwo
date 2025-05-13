import unittest
from structures.lists.double_linked_list import DoubleLinkedList as dl
from structures.lists.linked_list import LinkedList as ll
from structures.lists.stack import Stack as s
from structures.lists.queue import Queue as q

class TestLinkedList(unittest.TestCase):
    def test_string_formats_correctly(self):
        expected = "[ This is a string, 2 ]"
        
        list = ll()
        list.add("This is a string")
        list.add(2)
        
        self.assertEqual(expected, list.__str__())

    def test_add_happy(self):
        expected = "[ 1, 2 ]"
        
        list = ll()
        list.add(1)
        list.add(2)
        
        self.assertEqual(expected, list.__str__())
    
    def test_insert_happy(self):
        expected = "[ 1, 2, 3 ]"
        
        list = ll()
        list.add(1)
        list.add(3)
        value = 2
        index = 1
        
        list.insert(value, index)
        
        self.assertEqual(expected, list.__str__())
    
    def test_insert_index_error(self):
        list = ll()
        with self.assertRaises(IndexError):
            list.insert(8274, 5)

        with self.assertRaises(IndexError):
            list.insert(83274, -12)
    
    def test_get_index_error(self):
        list = ll()
        with self.assertRaises(IndexError):
            list[12]
        
        with self.assertRaises(IndexError):
            list[-1]
    
    def test_get(self):
        list = ll()
        list.add(1)
        list.add(2)
        
        self.assertEqual(1, list[0])
        self.assertEqual(2, list[1])
    
    def test_remove_happy(self):
        expected = 0
        
        list = ll()
        list.add(0)
        list.add(1)
        
        actual = list.remove()
        
        self.assertEqual(expected, actual)
    
    def test_remove_index_error(self):
        list = ll()
        with self.assertRaises(IndexError):
            list.remove()
    
    def test_remove_at_happy(self):
        expected = 2
        
        list = ll()
        list.add(1)
        list.add(2)
        
        actual = list.removeAt(1)
        
        self.assertEqual(expected, actual)
    
    def test_remove_at_index_error(self):
        list = ll()
        with self.assertRaises(IndexError):
            list.removeAt(1)
            
        with self.assertRaises(IndexError):
            list.removeAt(-1)

    def test_remove_last_happy(self):
        expected = 3
        list = ll()
        
        list.add(1)
        list.add(2)
        list.add(3)
        
        actual = list.removeLast()
        
        self.assertEqual(expected, actual)
    
    def test_remove_last_index_error(self):
        list = ll()
        with self.assertRaises(IndexError):
            list.removeLast()
    
    def test_clear_happy(self):
        expected = "[ ]"
        list = ll()
        
        list.add(1)
        
        list.clear()
        
        self.assertEqual(expected, list.__str__())
    
    def test_search_found(self):
        expected = 1
        list = ll()
        
        list.add(2)
        list.add(3)
        
        actual = list.search(3)
        
        self.assertEqual(expected, actual)
    
    def test_search_not_found(self):
        expected = -1
        list = ll()
        
        list.add(2)
        list.add(3)
        
        actual = list.search(4)
        
        self.assertEqual(expected, actual)

class TestDoubleLinkedList(unittest.TestCase):
    def test_string_formats_correctly(self):
        expected = "[ This is a string, 2 ]"
        
        list = dl()
        list.add("This is a string")
        list.add(2)
        
        self.assertEqual(expected, list.__str__())

    def test_add_happy(self):
        expected = "[ 1, 2 ]"
        
        list = dl()
        list.add(1)
        list.add(2)
        
        self.assertEqual(expected, list.__str__())
    
    def test_insert_happy(self):
        expected = "[ 1, 2, 3 ]"
        
        list = dl()
        list.add(1)
        list.add(3)
        value = 2
        index = 1
        
        list.insert(value, index)
        
        self.assertEqual(expected, list.__str__())
    
    def test_insert_index_error(self):
        list = dl()
        with self.assertRaises(IndexError):
            list.insert(8274, 5)

        with self.assertRaises(IndexError):
            list.insert(83274, -12)
    
    def test_get_index_error(self):
        list = dl()
        with self.assertRaises(IndexError):
            list.get(12)
        
        with self.assertRaises(IndexError):
            list.get(-1)
    
    def test_remove_happy(self):
        expected = 0
        
        list = dl()
        list.add(0)
        list.add(1)
        
        actual = list.remove()
        
        self.assertEqual(expected, actual)
    
    def test_remove_index_error(self):
        list = dl()
        with self.assertRaises(IndexError):
            list.remove()
    
    def test_remove_at_happy(self):
        expected = 2
        
        list = dl()
        list.add(1)
        list.add(2)
        
        actual = list.removeAt(1)
        
        self.assertEqual(expected, actual)
    
    def test_remove_at_index_error(self):
        list = dl()
        list.add(1)
        with self.assertRaises(IndexError):
            list.removeAt(1)
            
        with self.assertRaises(IndexError):
            list.removeAt(-1)

    def test_remove_last_happy(self):
        expected = 3
        list = dl()
        
        list.add(1)
        list.add(2)
        list.add(3)
        
        actual = list.removeLast()
        
        self.assertEqual(expected, actual)
    
    def test_remove_last_index_error(self):
        list = dl()
        with self.assertRaises(IndexError):
            list.removeLast()
    
    def test_clear_happy(self):
        expected = "[ ]"
        list = dl()
        
        list.add(1)
        
        list.clear()
        
        self.assertEqual(expected, list.__str__())
    
    def test_search_found(self):
        expected = 1
        list = dl()
        
        list.add(2)
        list.add(3)
        
        actual = list.search(3)
        
        self.assertEqual(expected, actual)
    
    def test_search_not_found(self):
        expected = -1
        list = dl()
        
        list.add(2)
        list.add(3)
        
        actual = list.search(4)
        
        self.assertEqual(expected, actual)

class TestStack(unittest.TestCase):
    def test_stack_push(self):
        expected = "[ 14, 13, 12 ]" # [ third, second, first ]
        stack = s()
        
        stack.push(12)
        stack.push(13)
        stack.push(14)
        
        self.assertEqual(expected, str(stack))
    
    def test_stack_get(self):
        expected = 14
        stack = s()
        
        stack.push(12)
        stack.push(13)
        stack.push(14)
        
        actual = stack.get(0)
        
        self.assertEqual(expected, actual)
    
    def test_stack_get_raises_exception(self):
        stack = s()
        
        with self.assertRaises(IndexError):
            stack.get(1)
        
        with self.assertRaises(IndexError):
            stack.get(-1)
    
    def test_stack_contains_true(self):
        stack = s()
        
        stack.push(12)
        stack.push(13)
        stack.push(14)
        
        self.assertTrue(stack.contains(13))
    
    def test_stack_contains_not_true(self):
        stack = s()
        
        stack.push(12)
        stack.push(13)
        stack.push(14)
        
        self.assertTrue(not stack.contains(15))
    
    def test_stack_pop(self):
        expected = 14
        expected_str = "[ 13, 12 ]"
        stack = s()
        
        stack.push(12)
        stack.push(13)
        stack.push(14)
        
        actual = stack.pop()
        
        self.assertEqual(expected, actual)
        self.assertEqual(expected_str, str(stack))
    
    def test_stack_pop_empty_raises_exception(self):
        stack = s()
        with self.assertRaises(IndexError):
            stack.pop()

class TestQueue(unittest.TestCase):
    def test_queue_enqueue(self):
        expected = "[ 14, 13, 12 ]"
        queue = q()
        
        queue.enqueue(12)
        queue.enqueue(13)
        queue.enqueue(14)
        
        self.assertEqual(expected, str(queue))
    
    def test_queue_dequeue(self):
        expected_str = "[ 14, 13 ]"
        expected = 12
        queue = q()
        
        queue.enqueue(12)
        queue.enqueue(13)
        queue.enqueue(14)
        
        self.assertEqual(expected, queue.dequeue())
        self.assertEqual(expected_str, str(queue))
    
    def test_queue_dequeue_empty_raises_exception(self):
        queue = q()
        
        with self.assertRaises(IndexError):
            queue.dequeue()
    
    def test_queue_contains_true(self):
        queue = q()
        
        queue.enqueue(12)
        queue.enqueue(13)
        queue.enqueue(14)
        
        self.assertTrue(queue.countains(14))
    
    def test_queue_contains_not_true(self):
        queue = q()
        
        queue.enqueue(12)
        queue.enqueue(13)
        queue.enqueue(14)
        
        self.assertTrue(not queue.countains(15))
    
    def test_queue_peek(self):
        queue = q()
        expected = 12
        
        queue.enqueue(12)
        queue.enqueue(13)
        queue.enqueue(14)
        
        actual = queue.peek()
        
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()