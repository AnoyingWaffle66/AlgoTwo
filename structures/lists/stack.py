from structures.lists.linked_list import LinkedList as ll

# Chosen method to pseudo code - contains(value)
# call the search method on the linked list that the stack wraps around
# search returns -1 if a value isn't found
# compare the result of the method call to -1 
# a found value will return the index so it should never be -1 if the value exists
# this will result in a true if a value is found and false if a value isn't found

class Stack():
    def __init__(self):
        self._list: ll = ll()
    
    def get(self, index):
        # this method takes in an index
        # it will get the value at that index
        # it will throw an IndexError if the index is out of bounds
        # get has a complexity of O(n) because in the worst case it has to traverse the entire list
        return self._list.get(index)
    
    def contains(self, value):
        # This method is used to check if a value is in the stack
        # It takes in a value to search for in the stack
        # It will return false if the value isn't found and true if it is
        # search/contains has a complexity of O(n) because in the worst case it will go through every value in the list
        return self._list.search(value) != -1
    
    def peek(self):
        # This method is used to look at the top item on the stack without removing it
        # It will throw an IndexError if the stack is empty
        # get/peek has a complexity of O(1) because it just looks at the value the head points to
        return self._list.get(0)
    
    def pop(self):
        # This method will remove and return the top value of the stack
        # It will throw an IndexError if the stack is empty
        # remove/pop has a complexity of O(1) because it just moves the head pointer
        return self._list.remove()
    
    def push(self, value):
        # This method is used to put a new value on the stack
        # It takes in the value to add to the stack as a parameter
        # insert/push has a complexity of O(1) because it just moves the head pointer
        self._list.insert(value, 0)
    
    def __str__(self):
        # This method will return the stack as a string
        return str(self._list)
