from structures.graphs.node import Node
from structures.lists.queue import Queue
from structures.graphs.graph import Graph

class Djikstra():
    def __init__(self, mapping: list = None, verbose: bool = False):
        self._graph = Graph(mapping)
        self.mapping = self.shortest_path(tuple(self._graph.labels))
        if not verbose:
            return
        for map in self.mapping:
            self.print_connections(map[0], map[1])

    def shortest_path(self, labels: tuple):
        paths = list()
        for idx in range(len(labels)):
            paths.append(self.evaluate_shortest_path(labels[idx]))
        return paths
    
    # Big O
    # This method has a complexity of O(n)
    # in the worst case a nodes path of least distance 
    # could pass through every node in the graph once, hence n complexity
    # Ex: 0 -> 4 could be 0 -> 1 -> 2 -> 3 -> 4
    def get_path(self, from_label: int, to_label: int) -> list:
        # this method will extract the pre calculated 
        # shortest path from one label to any other label
        # it will return the path in the form of a list
        path = list()
        mapping = self.mapping[from_label][0]
        loop = True
        idx = to_label
        tracker = 0
        while loop and tracker < len(self.mapping[from_label][0]) - 1:
            idx = mapping[idx][0]
            path.append(idx)
            loop = idx != from_label
            tracker += 1
        path.reverse()
        path.append(to_label)
        return path
    
    
    # pseudo code
    # create a queue
    # enqueue the node that we are starting from
    # while the queue is not empty, process the first item
    # if the nodes attached to the current node aren't in the visited list, enqueue them
    # in the processing of the item, add all its nodes to a list of visited nodes so they aren't enqueued later
    # evaluate the distance for every connected node
    # add the current nodes tracked distance with the weight of the edge connecting the two edges
    # if that distance is less than the current distance on that node, then start tracking that distance instead. Also track the node it came from
    # do the same for the node that we just evaluated but from the currently being processed node
    # after the queue is empty we will have all the nodes will have tracked their distances and the node that updated their shortest path

    # Big O
    # This algorithm is O(n^2)
    # In the worst case every node could 
    # be connected to every other node, so in the 
    # worst case you would have to evaluate the 
    # distance for n nodes n times hence n^2
    def evaluate_shortest_path(self, n1_label):
        # I appologize for this abomination
        queue = Queue()
        visited = list()
        node_paths = list()
        for _ in range(len(self._graph._nodes)):
            node_paths.append((-1, -1))
        queue.enqueue(self._graph._nodes[n1_label])
        node_paths[n1_label] = (n1_label, 0)
        while not queue.is_empty():
            current: Node = queue.dequeue()
            connections = current.get_connections()
            if current.label not in visited:
                visited.append(current.label)
            for idx in range(len(connections)):
                if idx == n1_label or connections[idx] == 0 or idx in visited:
                    continue
                distance = connections[idx]
                if idx not in visited:
                    queue.enqueue(self._graph._nodes[idx])
                total = node_paths[current.label][1] + distance
                if total < node_paths[idx][1] or node_paths[idx][1] == -1:
                    node_paths[idx] = (current.label, total)
                total = node_paths[idx][1] + distance
                if total < node_paths[current.label][1] or node_paths[current.label][1] == -1:
                    node_paths[current.label] = (idx, total)
        # self.print_connections(node_paths, n1_label)
        return (node_paths, n1_label)
    
    def print_connections(self, node_paths, from_node):
        # If you pass in to this method the list of 
        # distances and the node that we found those 
        # distances form it will print all the paths 
        # to each node to the console
        #
        # it is unwieldy to use however given the 
        # structure that the paths are stored in (list of tuples of a list of tuples... idk man)
        for idx in range(len(node_paths)):
            string = ""
            if idx != from_node:
                print(f"{from_node} -> {idx}: distance = {node_paths[idx][1]}")
                back_list = list()
                loop = True
                back_idx = idx
                while loop:
                    back_list.append(back_idx)
                    back_idx = node_paths[back_idx][0]
                    loop = back_idx != from_node
                back_list.reverse()
                for thing in range(len(back_list)):
                    string += f"{back_list[thing]}"
                    string += " -> " if thing != len(back_list) - 1 else ""
                print(f"{from_node} -> {string} \n")
