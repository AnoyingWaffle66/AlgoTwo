from structures.lists.double_linked_list import DoubleLinkedList as dl

class Queue():
    def __init__(self):
        self.__doubleList = dl()
    
    def get(self, index):
        return self.__doubleList.get(index)
    
    def countains(self, value):
        return self.__doubleList.search(value) != -1
    
    def peek(self):
        return self.__doubleList.get(self.__doubleList._count - 1)
    
    def dequeue(self):
        return self.__doubleList.removeLast()
    
    def enqueue(self, value):
        self.__doubleList.insert(value, 0)
    
    def __str__(self):
        return str(self.__doubleList)