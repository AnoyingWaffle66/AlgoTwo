from structures.lists.node import Node
class DoubleNode(Node):
    def __init__(self, value = 0, previous = None):
        super().__init__(value)
        self.previous = previous