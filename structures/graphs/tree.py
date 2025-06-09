from structures.graphs.tree_node import TreeNode

class BinarySearchTree():
    def __init__(self):
        self._count: int = 0
        self._root: TreeNode = TreeNode(0)
        self._traversals = {
            "in"   : self._traverse_in_order,
            "pre"  : self._traverse_pre_order,
            "post" : self._traverse_post_order,
        }
    
    def _traverse(self, value, node: TreeNode) -> TreeNode:
        # This is a recursive method that will traverse down the tree until it hits a leaf which will be returned at the end of the recursion
        # It is primarily used for adding new leaves to the tree
        # The parameters are the value to compare and a node which the value will be compared against
        # The original call of this function passes the root in order to traverse all the way down
        # This algorithm is O(log(n)) for a well balanced tree, but it can be O(n) if the tree's depth == n
        node_return: TreeNode = None
        if value < node.value:
            node_return = node if not node.left else self._traverse(value, node.left)
        else:
            node_return = node if not node.right else self._traverse(value, node.right)
        return node_return
    
    def _find_node(self, value, node: TreeNode):
        if node == None:
            return None
        if value == node.value:
            return node
        elif value < node.value:
            return self._find_node(value, node.left)
        else:
            return self._find_node(value, node.right)
    
    def _traverse_in_order(self, node: TreeNode, full_list: list):
        if node.left:
            self._traverse_in_order(node.left, full_list)
        full_list.append(node.value)
        if node.right:
            self._traverse_in_order(node.right, full_list)
    
    def _traverse_pre_order(self, node: TreeNode, full_list: list):
        full_list.append(node.value)
        if node.left:
            self._traverse_pre_order(node.left, full_list)
        if node.right:
            self._traverse_pre_order(node.right, full_list)
    
    def _traverse_post_order(self, node: TreeNode, full_list: list):
        if node.left:
            self._traverse_post_order(node.left, full_list)
        if node.right:
            self._traverse_post_order(node.right, full_list)
        full_list.append(node.value)
    
    def to_list(self, method = "in") -> list:
        if method not in self._traversals:
            raise ValueError(f"method {method} is an invalid list notation")
        full_list = list()
        if not self._is_empty():
            self._traversals[method](self._root.left, full_list)
        return full_list
    
    def to_list_pre(self) -> list:
        return self.to_list(method="pre")
    
    def to_list_post(self) -> list:
        return self.to_list(method="post")
    
    def pre_order_str(self) -> str:
        return str(self.to_list_pre())
    
    def post_order_str(self) -> str:
        return str(self.to_list_post())
    
    def height(self):
        return self._height(self._root.left)
    
    def _height(self, node: TreeNode, current_height = 1, highest_height = 1):
        if not node:
            return current_height - 1
        highest_height = current_height if current_height > highest_height else highest_height
        left_height = current_height
        right_height = current_height
        if node.left:
            left_height = self._height(node.left, current_height + 1, highest_height)
        if node.right:
            right_height = self._height(node.right, current_height + 1, highest_height)
        if left_height > highest_height:
            highest_height = left_height
        if right_height > highest_height:
            highest_height = right_height
        return highest_height
    
    def add(self, value):
        # This method adds a new leaf onto the tree
        # it calls the _traverse method to find the appropriate existing leaf to add the value to
        # This algorithms complexity is the same as the _traverse method, everything this method does in addition to that is contant complexity
        # In other words, this method is O(log(n)) for a balanced tree or O(n) for a tree where its depth equals n
        new_node = TreeNode(value)
        self._count += 1
        if self._is_empty():
            self._root.left = new_node
            return
        parent = self._traverse(value, self._root.left)
        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.previous = parent
    
    def _farthest_left(self, node: TreeNode) -> TreeNode:
        return self._farthest_left(node.left) if node.left else node
    
    # Pseudo code for lab 2
    # Assuming that we have the node to be removed
    # Store the current nodes value so it can be passed up recursively
    # Check if the node is a leaf (no children)
    # If it is remove it from the tree
    # If it is not, check if it has a child
    # If it does determine which side the child is in
    # The child and its sub branches are safe to move up to directly replace the original node
    # If there are 2 branches use recursion to find either a leaf or a node with one child
    # In this recursion the branch with two won't be removed, instead ad
    # different node will and its value will be passed up the recursion chain
    # At the end of all branch permutations return the stored value
    def _remove(self, node_to_remove: TreeNode):
        storage = node_to_remove.value
        if not node_to_remove.left and not node_to_remove.right:
            if node_to_remove.previous.left == node_to_remove:
                node_to_remove.previous.left = None
            else:
                node_to_remove.previous.right = None
            return storage
        
        if node_to_remove.left and not node_to_remove.right:
            child = node_to_remove.left
        elif node_to_remove.right and not node_to_remove.left:
            child = node_to_remove.right
        else:
            child = None
        
        if child:
            if node_to_remove.previous.left == node_to_remove:
                node_to_remove.previous.left = child
            else:
                node_to_remove.previous.right = child
            child.previous = node_to_remove.previous
            return storage
        
        temp = self._farthest_left(node_to_remove.right)
        value = temp.value
        self._remove(temp)
        node_to_remove.value = value
        return storage
    
    def _remove_root(self):
        root_to_remove = self._root.left
        
        if not root_to_remove.left and not root_to_remove.right:
            self._root.left = None
            return
        
        if root_to_remove.left and not root_to_remove.right:
            self._root.left = root_to_remove.left
            root_to_remove.left.previous = None
            return
        elif root_to_remove.right and not root_to_remove.left:
            self._root.left = root_to_remove.right
            root_to_remove.right.previous = None
            return
        
        temp = self._farthest_left(root_to_remove.right)
        value = temp.value
        self._remove(temp)
        root_to_remove.value = value
    
    def remove(self, value):
        if not self.contains(value):
            raise ValueError(f"value {value} is not in the tree")
        node_to_remove = self._find_node(value, self._root.left)
        if node_to_remove == self._root.left:
            self._remove_root()
        else:
            self._remove(node_to_remove)   
        self._count -= 1
    
    def clear(self):
        # This method sets the root to be None and the count to be 0
        # This is everything that needs to happen for the tree to be cleared
        # It is O(1) time complexity
        self._root.left = None
        self._count = 0
    
    def contains(self, value):
        if self._is_empty():
            return False
        thing = self._find_node(value, self._root.left)
        return thing != None
    
    def _is_empty(self):
        return self._root.left == None
    
    def __str__(self):
        values = self.to_list()
        strinj = "[ "
        length = len(values)
        for i in range(length):
            strinj += f"{values[i]}"
            strinj += ", " if i < length - 1 else " "
        strinj += "]"
        return strinj