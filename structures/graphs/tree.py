from structures.graphs.tree_node import TreeNode

class BinarySearchTree():
    def __init__(self):
        self._count: int = 0
        self._root: TreeNode = None
    
    def _traverse(self, value, node: TreeNode) -> TreeNode:
        node_return: TreeNode = None
        if value < node.value:
            node_return = node if not node.left else self._traverse(value, node.left)
        else:
            node_return = node if not node.right else self._traverse(value, node.right)
        return node_return
    
    def _traverse_grab_all_values(self, node: TreeNode, full_list: list):
        if node.left:
            self._traverse_grab_all_values(node.left, full_list)
        full_list.append(node.value)
        if node.right:
            self._traverse_grab_all_values(node.right, full_list)
    
    def to_list(self) -> list:
        full_list = list()
        if not self._is_empty():
            self._traverse_grab_all_values(self._root, full_list)
        return full_list
    
    def add(self, value):
        new_node = TreeNode(value)
        self._count += 1
        if self._is_empty():
            self._root = new_node
            return
        parent = self._traverse(value, self._root)
        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node
    
    def clear(self):
        self = self.__init__()
    
    def _is_empty(self):
        return self._root == None
    
    def __str__(self):
        values = self.to_list()
        strinj = "[ "
        length = len(values)
        for i in range(length):
            strinj += f"{values[i]}"
            strinj += ", " if i < length - 1 else " "
        strinj += "]"
        return strinj