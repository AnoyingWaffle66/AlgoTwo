import unittest
from structures.graphs.mst import MST

class KruskalTest(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.mapping = [
            [0, 3, 6,  3,  0],
            [3, 0, 3,  6,  0],
            [6, 3, 0,  4,  0],
            [3, 6, 4,  0, 15],
            [0, 0, 0, 15,  0]
        ]
    
    def test_total_weight(self):
        mst = MST(self.mapping, None) # Passing None causes the MST to be 
        # constructed without calling kruskals in the constructor
        # Dropping the parameter will pass the default "kruskal" to the constructor
        expected = 40
        
        actual = mst.total_length()
        
        self.assertEqual(expected, actual)
    
    def test_kruskal(self):
        mst = MST(self.mapping, None)
        expected = [
            [0, 3, 0,  3,  0],
            [3, 0, 3,  0,  0],
            [0, 3, 0,  0,  0],
            [3, 0, 0,  0, 15],
            [0, 0, 0, 15,  0]
        ]
        
        mst.kruskal()
        
        actual = [node.get_connections() for node in mst.graph._nodes]
        
        self.assertEqual(expected, actual)
    
    def test_unsolvable(self):
        with self.assertRaises(ValueError):
            mst = MST([
                [0, 2, 0, 0],
                [2, 0, 0, 0],
                [0, 0, 0, 3],
                [0, 0, 3, 0]
            ], None)
            mst.kruskal()
    
    def test_format_connections(self):
        mst = MST([
            [0, 1, 2],
            [1, 0, 3],
            [2, 3, 0],
        ], None)
        
        expected = [((0, 1), 1), ((0, 2), 2), ((1, 2), 3)]
        
        actual = mst.format_connections()
        
        self.assertEqual(expected, actual)
    
    def test_no_mapping_passed(self):
        mst = MST(None)
        expected = list()
        
        actual = mst.graph._nodes
        
        self.assertEqual(expected, actual)
    
    def test_no_mapping_passed_length(self):
        mst = MST(None)
        expected = 0
        
        actual = mst.total_length()
        
        self.assertEqual(expected, actual)
    
    def test_no_mapping_passed_format(self):
        mst = MST(None)
        expected = list()
        
        actual = mst.format_connections()
        
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()