import unittest
import sys
sys.path.append('''C:\Git\Algorithms''')
import kargermincut
import random


# get_edges(G)
class TestGetEdges(unittest.TestCase):
    """Unit tests for get_edges(G) """

    def test_get_edges_1(self):
        """ Testing get_edges(G) """
        G = [[0, [1, 2, 3]], [1, [0, 2]], [2, [0, 1, 3]], [3, [0, 2]]]
        edges = kargermincut.get_edges(G)
        self.assertEqual(edges, [[0, 1], [0, 2], [0, 3], [1, 2], [2, 3]])

    def test_get_edges_2(self):
        """ Testing get_edges(G) """
        G = [[0, [0, 1, 2, 3]], [1, [0, 2]], [2, [0, 1, 3]], [3, [0, 2, 3]]]
        edges = kargermincut.get_edges(G)
        self.assertEqual(edges, [[0, 0], [0, 1], [0, 2], [0, 3], [1, 2], [2, 3], [3, 3]])

    def test_get_edges_3(self):
        """ Testing get_edges(G) """
        G = [[1, [2, 3, 4]], [2, [1, 3]], [3, [1, 2, 4]], [4, [1, 3]]]
        edges = kargermincut.get_edges(G)
        self.assertEqual(edges, [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]])


# remove_self_loops(edges)
class TestRemoveSelfLoops(unittest.TestCase):
    """Unit tests for remove_self_loops(edges) """

    def test_remove_self_loops_1(self):
        """ Testing remove_self_loops(edges) for single element list"""
        G = [[0, [1, 2, 3]], [1, [0, 2]], [2, [0, 1, 3]], [3, [0, 2]]]
        edges = kargermincut.get_edges(G)
        edges = kargermincut.remove_self_loops(edges)
        self.assertEqual(edges, [[0, 1], [0, 2], [0, 3], [1, 2], [2, 3]])

    def test_get_edges_2(self):
        """ Testing remove_self_loops(edges) for single element list"""
        G = [[0, [0, 1, 2, 3]], [1, [0, 2]], [2, [0, 1, 3]], [3, [0, 2, 3]]]
        edges = kargermincut.get_edges(G)
        edges = kargermincut.remove_self_loops(edges)
        self.assertEqual(edges, [[0, 1], [0, 2], [0, 3], [1, 2], [2, 3]])


if __name__ == '__main__':
    unittest.main()