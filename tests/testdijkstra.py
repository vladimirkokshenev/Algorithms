import unittest
import sys
sys.path.append('''C:\Git\Algorithms''')
import dijkstra


class TestReadGraphFromFile(unittest.TestCase):

    def test_read_graph_1(self):
        filename = "dijkstraData2.txt"
        G = dijkstra.read_graph_from_file(filename)
        self.assertEqual(G[0], [{'DEST': 1, 'COST': 1}, {'DEST': 7, 'COST': 2}])
        self.assertEqual(G[1], [{'DEST': 0, 'COST': 1}, {'DEST': 2, 'COST': 1}])
        self.assertEqual(G[2], [{'DEST': 1, 'COST': 1}, {'DEST': 3, 'COST': 1}])
        self.assertEqual(G[3], [{'DEST': 2, 'COST': 1}, {'DEST': 4, 'COST': 1}])
        self.assertEqual(G[4], [{'DEST': 3, 'COST': 1}, {'DEST': 5, 'COST': 1}])
        self.assertEqual(G[5], [{'DEST': 4, 'COST': 1}, {'DEST': 6, 'COST': 1}])
        self.assertEqual(G[6], [{'DEST': 5, 'COST': 1}, {'DEST': 7, 'COST': 1}])
        self.assertEqual(G[7], [{'DEST': 6, 'COST': 1}, {'DEST': 0, 'COST': 2}])
        self.assertEqual(len(G), 8)


if __name__ == '__main__':
    unittest.main()