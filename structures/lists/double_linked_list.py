from structures.lists.linked_list import LinkedList
from structures.lists.double_node import DoubleNode

class DoubleLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self._head: DoubleNode = DoubleNode()
        self._tail: DoubleNode = DoubleNode()
    
    def add(self, value):
        new_node = DoubleNode(value)
        if self._count == 0:
            self._head.next = new_node
        else:
            dummy = self.traverse(self._count)
            new_node.previous = dummy
            dummy.next = new_node
        self._tail.previous = new_node
        self._count += 1
    
    def insert(self, value, index):
        new_node = DoubleNode(value)
        dummy = self.traverse(index)
        new_node.next = dummy.next
        dummy.next = new_node
        new_node.previous = dummy if index != 0 else None
        if new_node.next:
            new_node.next.previous = new_node
        else:
            self._tail.previous = new_node
        self._count += 1
    
    def remove(self):
        if self._count == 0:
            raise IndexError("List is empty")
        ret = self._head.next.value
        if self._count == 1:
            self._head.next = None
            self._tail.previous = None
        else:
            self._head.next.next.previous = None
            self._head.next = self._head.next.next
        self._count -= 1
        return ret
    
    def removeAt(self, index):
        if index == 0:
            return self.remove()
        if self._count == 0:
            raise IndexError("List is empty")
        dummy = self.traverse(index, -1)
        ret = dummy.next.value
        dummy.next = dummy.next.next
        if dummy.next:
            dummy.next.previous = dummy
        self._count -= 1
        return ret
    
    def removeLast(self):
        if self._count == 0:
            raise IndexError("List is empty")
        ret = None
        if self._count == 1:
            ret = self._head.next.value
            self._head.next = None
            self._tail.previous = None
        else:
            ret = self._tail.previous.value
            self._tail.previous = self._tail.previous.previous
            self._tail.previous.next = None
        self._count -= 1
        return ret