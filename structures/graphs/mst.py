from structures.graphs.graph import Graph

class MST():
    def __init__(self, mapping:list, method:str = "kruskal"):
        self.graph = Graph(mapping)
        match method:
            case "kruskal":
                self.kruskal()
            case "prim":
                # self.prim()
                pass
            case _:
                pass
    
    def kruskal(self) -> None:
        # this is a method that can be called without needing data passed in
        # its purpose is to prepare the data for Kruskals algorithm and call the actual function with the formatted data
        conn_list = self.format_connections()
        if len(conn_list) + 1 < len(self.graph._nodes):
            raise ValueError("Minimum spanning tree not possible with this graph")
        self._kruskal(conn_list)
    
    def format_connections(self) -> list:
        # because the connections of the graph aren't an actual connection object they need to be derived from the list of connections that each node owns
        # this method will iterate through the node's connection list and construct a list that holds this type of structure ((node1 label, node2 label), distance)
        # from there python's sort function is called to sort the list by distance
        # by this point the connections are in a form that enables the functionality of Kruskal's algorithm
        nodes = self.graph._nodes
        conn_list = list()
        for node_idx in range(len(nodes)):
            connections = nodes[node_idx].get_connections()
            for idx in range(len(connections)):
                if connections[idx] == 0:
                    continue
                if ((idx, node_idx), connections[idx]) not in conn_list:
                    conn_list.append(((node_idx, idx), connections[idx]))
        conn_list.sort(key=lambda v:v[1])
        return conn_list

    # Pseudo code
    # iterate over the sorted connections
    # connections store two nodes
    # do an intersection of the two nodes individual sets of nodes
    # if that results in the empty set it means they can be connected
    # if that doesn't result in the empty set it means there is a circular reference and the connection should be added to the graph
    # update both nodes stored sets of nodes if they should be connected
    # check if their is one less connection than there are nodes
    # if there are then kruskals is done
    # if not continue interating over the connections
    
    # Big O
    # Krsukals is O(n) where n is the amount of connections in the graph
    # it could be that all the shorter connections cause circular references but the longest node does not
    # this would mean we have to iterate over all connections to find the minimum spanning tree
    def _kruskal(self, conn_list: list) -> None:
        # This algorithm will first generate a new map of n x n populating each slot with a 0
        # After this it iterates through the sorted array of connections
        # it does an intersection between each nodes sets and if it is empty it does a union of their sets
        # it iterates until their is one less connection than there are nodes in the graph
        count = len(self.graph._nodes)
        new_mapping = [[0 for _ in range(count)] for _ in range(count)]
        empty_set = set()
        connections_count = 0
        for idx in range(len(conn_list)):
            node1_idx = conn_list[idx][0][0]
            node2_idx = conn_list[idx][0][1]
            node1 = self.graph._nodes[node1_idx]
            node2 = self.graph._nodes[node2_idx]
            inter = set.intersection(node1.set, node2.set)
            
            if inter != empty_set:
                continue
            
            union = set.union(node1.set, node2.set)
            node1.set = node2.set = union
            new_mapping[node1_idx][node2_idx] = new_mapping[node2_idx][node1_idx] = conn_list[idx][1]
            connections_count += 1
            if connections_count == count - 1:
                break
        self.graph = Graph(new_mapping)
    
    def total_length(self) -> int:
        # this function goes through every weight stored in the graph and sums them
        # it divides it by 2 at the end because nodes are undirected (their weight is stored twice)
        total = 0
        for node in self.graph._nodes:
            for num in node.get_connections():
                total += num
        return total // 2

if __name__ == "__main__":
    mapping = [
        [0, 5, 1, 4, 9, 0, 9, 2, 6, 0, 0, 6, 3, 5, 2],
        [5, 0, 5, 2, 6, 6, 0, 4, 4, 3, 0, 8, 4, 4, 1],
        [1, 5, 0, 6, 5, 4, 0, 5, 1, 5, 7, 7, 5, 0, 3],
        [4, 2, 6, 0, 2, 0, 1, 8, 0, 4, 0, 5, 2, 4, 6],
        [9, 6, 5, 2, 0, 5, 0, 0, 6, 2, 8, 9, 2, 5, 2],
        [0, 6, 4, 0, 5, 0, 2, 7, 7, 2, 6, 2, 2, 3, 5],
        [9, 0, 0, 1, 0, 2, 0, 2, 4, 3, 3, 3, 0, 1, 0],
        [2, 4, 5, 8, 0, 7, 2, 0, 6, 8, 5, 8, 2, 3, 2],
        [6, 4, 1, 0, 6, 7, 4, 6, 0, 7, 6, 7, 7, 4, 4],
        [0, 3, 5, 4, 2, 2, 3, 8, 7, 0, 5, 1, 6, 3, 2],
        [0, 0, 7, 0, 8, 6, 3, 5, 6, 5, 0, 8, 1, 3, 0],
        [6, 8, 7, 5, 9, 2, 3, 8, 7, 1, 8, 0, 8, 7, 6],
        [3, 4, 5, 2, 2, 2, 0, 2, 7, 6, 1, 8, 0, 3, 2],
        [5, 4, 0, 4, 5, 3, 1, 3, 4, 3, 3, 7, 3, 0, 3],
        [2, 1, 3, 6, 2, 5, 0, 2, 4, 2, 0, 6, 2, 3, 0]
    ]
    mst = MST(mapping, None)
    mst.kruskal()
    for connections in mst.graph._nodes:
        print(connections.get_connections())