from structures.lists.linked_list import LinkedList
from structures.lists.double_node import DoubleNode

class DoubleLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self._head = DoubleNode()
        self._tail = DoubleNode()
    
    def add(self, value):
        dummy = self.traverse(self._count)
        dummy.next = DoubleNode(value, dummy)
        self._tail.previous = dummy.next
        self._count += 1
    
    def insert(self, value, index):
        dummy = self.traverse(index)
        new_node = DoubleNode(value, dummy)
        self._count += 1
        if(index == 0):
            new_node.next = self._head.next
            self._head.next = new_node
            return
        if (index == self._count - 1):
            self._tail.previous = new_node
            return
        dummy.next.previous = new_node
        new_node.next = dummy.next
        dummy.next = new_node
    
    def remove(self):
        if self._count < 1:
            raise IndexError("List is empty")
        ret = self._head.next.value
        self._head.next = self._head.next.next
        self._head.next.previous = None
        self._count -= 1
        return ret
    
    def removeAt(self, index):
        if index == self._count - 1:
            return self.removeLast()
        dummy = self.traverse(index, -1)
        ret = dummy.next.value
        dummy.next = dummy.next.next #if index < self._count - 1 else self._tail
        dummy.next.previous = dummy
        self._count -= 1
        return ret
    
    def removeLast(self):
        if self._count < 1:
            raise IndexError("List is empty")
