from structures.graphs.tree_node import TreeNode
from structures.graphs.tree import BinarySearchTree
from structures.lists.queue import Queue as q

class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()
        self._traversals = {
            "in"      : super()._traverse_in_order,
            "pre"     : super()._traverse_pre_order,
            "post"    : super()._traverse_post_order,
            "breadth" : self._breadth_first
        }
        self._directions = [(2,1),(-2,-1),(-2,1),(2,-1)]
        self._rotations = {
            (2, 1)    : self.left,
            (-2, -1)  : self.right,
            (-2, 1)   : self.left_right,
            (2, -1)   : self.right_left
        }
    
    def _breadth_first(self, node: TreeNode = None, full_list: list = None):
        # Pseudo Code
        # Create a queue and a list/array
        # Start at the root, throw it into a queue
        # While the queue has nodes in it, dequeue the bottom node, enqueue its left and right nodes if they exist
        # append to the list the value from the dequeued node
        # Once the queue is empty the breadth first traversal will be finished
        # This algorithm is O(n) every node in the tree is processed exactly once
        queue = q()
        queue.enqueue(self._root.left)
        while not queue.is_empty():
            current_item: TreeNode = queue.dequeue()
            if current_item.left:
                queue.enqueue(current_item.left)
            if current_item.right:
                queue.enqueue(current_item.right)
            full_list.append(current_item.value)
    
    def _detect_rotation(self, node: TreeNode):
        # detect rotation has a O(n) complexity, this is because in the worst case 
        # it always traverses the whole left and the whole right to find 
        # the balance factor of the root.
        left = self._height(node.left) if node.left else 0
        right = self._height(node.right) if node.right else 0
        height_factor = right - left
        lower_factor = 0
        if height_factor == 1 or height_factor == -1:
            return False, height_factor, None
        if height_factor > 1 or height_factor < -1:
            useless, lower_factor, useless2 = self._detect_rotation(node.right if height_factor > 1 else node.left)
            if lower_factor in self._directions:
                return useless, lower_factor, useless2
        direction = (height_factor, lower_factor)
        return direction in self._directions, direction, node
    
    def add(self, value):
        if self.contains(value):
            raise ValueError("AVLTree cannot hold duplicate values")
        super().add(value)
        rotate, direction, node_to_rotate = self._detect_rotation(self._root.left)
        if rotate:
            self._rotations[direction](node_to_rotate)
    
    def remove(self, value):
        super().remove(value)
        rotate, direction, node_to_rotate = self._detect_rotation(self._root.left)
        if rotate:
            self._rotations[direction](node_to_rotate)
    
    # To simplify the amount of comments I have to make, 
    # I will group left, right, left_right and right_left into one comment 
    # because they all have the same Big-O.
    # They are all O(1) this is because the steps need 
    # to perform each rotation is independent of n. The 
    # amount of nodes in the tree does not affect the
    # amount of steps needed to perform a rotation.
    def left(self, node: TreeNode):
        temp = node
        new_root = node.right
        if temp == self._root.left:
            self._root.left = new_root
        elif temp.value < temp.previous.value:
            temp.previous.left = new_root
        else:
            temp.previous.right = new_root
        temp.right = new_root.left
        if new_root.left:
            new_root.left.previous = temp
        new_root.left = temp
        new_root.previous = temp.previous
        temp.previous = new_root
    
    def right(self, node: TreeNode):
        temp = node
        new_root = node.left
        if temp == self._root.left:
            self._root.left = new_root
        elif temp.value < temp.previous.value:
            temp.previous.left = new_root
        else:
            temp.previous.right = new_root
        temp.left = new_root.right
        if new_root.right:
            new_root.right.previous = temp
        new_root.right = temp
        new_root.previous = temp.previous
        temp.previous = new_root
    
    def left_right(self, node: TreeNode):
        self.left(node.left)
        self.right(node)
    
    def right_left(self, node: TreeNode):
        self.right(node.right)
        self.left(node)
    
    def to_list(self, method="breadth"):
        # See _breadth_first for "toArray" pseudo code
        contents = list()
        self._traversals[method](self._root.left, contents)
        return contents
