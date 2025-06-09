from structures.lists.double_linked_list import DoubleLinkedList as dl

class Queue():
    def __init__(self):
        self.__doubleList = dl()
    
    def get(self, index):
        # this method takes in an index
        # it will get the value at that index
        # it will throw an IndexError if the index is out of bounds
        # get has a complexity of O(n) because in the worst case it has to traverse the entire list
        return self.__doubleList.get(index)
    
    def countains(self, value):
        # This method is used to check if a value is in the queue
        # It takes in a value to search for in the queue
        # It will return false if the value isn't found and true if it is
        # search/contains has a complexity of O(n) because in the worst case it has to traverse the entire list
        return self.__doubleList.search(value) != -1
    
    def peek(self):
        # This method is used to look at the bottom item on the queue without removing it
        # It will throw an IndexError if the queue is empty
        # peek has a complexity of O(1) because it just looks at the value pointed at by the tail
        return self.__doubleList.get(self.__doubleList._count - 1)
    
    def dequeue(self):
        # This method will remove and return the bottom value of the queue
        # It will throw an IndexError if the queue is empty
        # removeLast/dequeue has a complexity of O(1) because it just moves the tails pointer to a different node
        return self.__doubleList.removeLast()
    
    def enqueue(self, value):
        # This method is used to put a new value in the queue
        # It takes in the value to add to the queue as a parameter
        # enqueue has a complexity of O(1) because it just moves the heads pointer to a different node
        self.__doubleList.insert(value, 0)
    
    def is_empty(self):
        return self.__doubleList._count == 0
    
    def __str__(self):
        # This method will return the queue as a string
        return str(self.__doubleList)