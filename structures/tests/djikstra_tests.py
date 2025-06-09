import unittest
from structures.graphs.djikstra import Djikstra as d

class DjikstraTests(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.mapping = [
            [    0, 1000,  1,  0,  0 ],
            [ 1000,    0,  2,  4,  0 ],
            [    1,    2,  0,  0, 16 ],
            [    0,    4,  0,  0, 20 ],
            [    0,    0, 16, 20,  0 ]
        ]
    
    def test_create_map(self):
        djikstra = d(self.mapping)
        expected = [0, 1, 2, 3, 4]
        
        actual = [x for x in range(len(djikstra._graph._nodes))]
        
        self.assertEqual(expected, actual)
    
    def test_find_all_from_node(self):
        djikstra = d(self.mapping)
        expected = [(0,0),(2,3),(0,1),(1,7),(2,17)]
        
        mapping = djikstra.evaluate_shortest_path(0) # evaluate_shortest_path returns a tuple, index 0 is a list of all the nodes and their shortest distances from the given node label, index 1 is the label of the node
        print(mapping)
        
        actual = mapping[0] # [0] the paths that were found ([1] would be the label of the node that the paths were found from)
        
        self.assertEqual(expected, actual)
    
    def test_get_path_to_node_from_node(self):
        djikstra = d(self.mapping)
        expected = [0, 2, 1, 3]
        
        actual = djikstra.get_path(0, 3)
        
        self.assertEqual(expected, actual)
    
    def test_correct_distance(self):
        djikstra = d(self.mapping)
        expected = 17
        
        actual = djikstra.mapping[0][0][4][1]
        
        self.assertEqual(expected, actual)

class DjikstraTestsDeadEnds(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.mapping = [ # This is the dead end example on canvas for reference
            [0,5,0,0,0,0],
            [5,0,6,4,0,3],
            [0,6,0,0,0,0],
            [0,4,0,0,1,0],
            [0,0,0,1,0,2],
            [0,3,0,0,2,0]
        ]
    
    def test_0_to_2_dead_end(self):
        djikstra = d(self.mapping)
        expected = [0, 1, 2]
        
        actual = djikstra.get_path(0, 2)
        
        self.assertEqual(expected, actual)

class DjikstraTestsUnsolvable(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.mapping = [
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
    
    def test_no_solutions(self):
        djikstra = d(self.mapping)
        path = djikstra.get_path(2, 0)
        
        self.assertTrue(-1 in path) # Since values are initialized to (-1,-1) a path with no solution will always have -1 in it, while a path that has a solution will never have -1

if __name__ == "__main__":
    unittest.main()