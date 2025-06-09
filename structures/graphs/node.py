class Node():
    def __init__(self, label: int, connections: list):
        self.connections = connections
        self.label = label
        self.set = set([label])
    
    def change_connections(self, idx, distance):
        self.connections[idx] = distance
    
    def get_connections(self) -> list:
        return self.connections