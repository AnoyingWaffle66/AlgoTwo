from structures.lists.j_list import JList
from structures.lists.node import Node

class LinkedList(JList):
    def __init__(self):
        super().__init__()
        self._head = Node()
        self._count = 0
    
    def traverse(self, amount, offset = 0):
        dummy = self._head
        if amount > self._count + offset or amount < 0:
            raise IndexError("Index out of bounds")
        for _ in range(amount):
            dummy = dummy.next
        return dummy
    
    def add(self, value):
        dummy = self.traverse(self._count)
        dummy.next = Node(value)
        self._count += 1
    
    def insert(self, value, index):
        dummy = self.traverse(index)
        new_node = Node(value)
        new_node.next = dummy.next
        dummy.next = new_node
        self._count += 1
    
    def get(self, index):
        dummy = self.traverse(index)
        if not dummy.next:
            raise IndexError("Index doesn't exist")
        return dummy.next.value
    
    def remove(self):
        if not self._head.next:
            raise IndexError("List is empty")
        val = self._head.next.value
        self._head.next = self._head.next.next
        self._count -= 1
        return val
    
    def removeAt(self, index):
        dummy = self.traverse(index)
        val = dummy.next.value
        dummy.next = dummy.next.next
        self._count -= 1
        return val
    
    def removeLast(self):
        dummy = self.traverse(self._count - 1)
        if not dummy:
            return
        val = dummy.next.value
        dummy.next = None
        self._count -= 1
        return val

    def clear(self):
        self._head.next = None
        self._count = 0
    
    def search(self, value):
        dummy = self._head
        for idx in range(self._count):
            dummy = dummy.next
            if dummy.value == value:
                return idx
        return -1
    
    def __str__(self):
        string = "["
        dummy = self._head
        while dummy.next:
            dummy = dummy.next
            string += f" {str(dummy.value)}"
            string += "," if dummy.next else ""
        return string + " ]"