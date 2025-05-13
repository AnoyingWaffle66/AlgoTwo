from abc import ABC, abstractmethod

class JList(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def add(self, value):
        pass
    
    @abstractmethod
    def insert(self, value, index):
        pass
    
    @abstractmethod
    def get(self, index):
        pass
    
    @abstractmethod
    def remove(self):
        pass
    
    @abstractmethod
    def removeAt(self, index):
        pass
    
    @abstractmethod
    def removeLast(self):
        pass
    
    @abstractmethod
    def clear(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass