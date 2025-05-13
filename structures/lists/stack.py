from structures.lists.linked_list import LinkedList as ll

class Stack():
    def __init__(self):
        self.__list = ll()
    
    def get(self, index):
        return self.__list.get(index)
    
    def contains(self, value):
        return self.__list.search(value) != -1
    
    def peek(self):
        return self.__list.get(0)
    
    def pop(self):
        return self.__list.remove()
    
    def push(self, value):
        self.__list.insert(value, 0)
    
    def __str__(self):
        return self.__list.__str__()
