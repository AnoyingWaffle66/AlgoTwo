class TreeNode():
    def __init__(self, value, previous = None):
        self.value = value
        self.previous: TreeNode = previous
        self.left: TreeNode = None
        self.right: TreeNode = None