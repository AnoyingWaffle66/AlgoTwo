from structures.graphs.node import Node

class Graph():
    def __init__(self, mapping: list = None):
        self._count = 0
        self._connection_count = 0
        self._nodes = list()
        self.labels = list()
        self.init_nodes(list() if not mapping else mapping)
        # for idx in range(len(self._nodes)):
        #     self.labels.append(idx)
    
    def init_nodes(self, mapping: list) -> list:
        nodes = list()
        for idx in range(len(mapping)):
            self.labels.append(idx)
            self.add_node(idx, mapping[idx])
        return nodes
    
    def add_node(self, idx, connections):
        self._nodes.insert(idx, Node(idx, connections))