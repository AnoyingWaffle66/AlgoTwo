from structures.lists.linked_list import LinkedList
from structures.lists.double_linked_list import DoubleLinkedList

if __name__ == "__main__":
    thing = DoubleLinkedList()
    thing.add(1)
    thing.add(None)
    print(thing)
    thing.insert(2, 1)
    print(thing)
    print(thing.get(1))
    thing.removeLast()
    print(thing)