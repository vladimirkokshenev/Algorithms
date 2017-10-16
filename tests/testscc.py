import unittest
import sys
sys.path.append('''C:\Git\Algorithms''')
import scc


# read_graph_from_file(filename)
class TestReadGraphFromFile(unittest.TestCase):

    def test_read_graph_1(self):
        filename = "SCC2.txt"
        G, Grev = scc.read_graph_from_file(filename)
        self.assertEqual(G, [[3], [7], [5], [6], [1], [8], [0], [4, 5], [6, 2]])
        self.assertEqual(Grev, [[6], [4], [8], [0], [7], [2, 7], [3, 8], [1], [5]])


# dfs1(Grev, i, explored_nodes, fintime_nodes, cur_ft)
class TestDFS1(unittest.TestCase):

    def test_dfs1_1(self):
        filename = "SCC2.txt"
        G, Grev = scc.read_graph_from_file(filename)
        n = len(Grev)
        explored_nodes = [False for i in range(n)]
        fintime_nodes = [n for i in range(n)]
        cur_ft = 0

        cur_ft = scc.dfs1(Grev, 8, explored_nodes, fintime_nodes, cur_ft)

        self.assertEqual(cur_ft, 6)
        self.assertEqual(explored_nodes, [False, True, True, False, True, True, False, True, True])
        self.assertEqual(fintime_nodes, [9, 2, 0, 9, 1, 4, 9, 3, 5])

        cur_ft = scc.dfs1(Grev, 6, explored_nodes, fintime_nodes, cur_ft)

        self.assertEqual(cur_ft, 9)
        self.assertEqual(explored_nodes, [True, True, True, True, True, True, True, True, True])
        self.assertEqual(fintime_nodes, [6, 2, 0, 7, 1, 4, 8, 3, 5])


# dfs2(G, i, explored_nodes, scc_membership, leader, scc_size)
class TestDFS2(unittest.TestCase):

    def test_dfs2_1(self):
        filename = "SCC2.txt"
        G, Grev = scc.read_graph_from_file(filename)
        n = len(G)
        explored_nodes = [False for i in range(n)]
        scc_membership = [-1 for i in range(n)]

        scc_size = 0
        scc_size = scc.dfs2(G, 6, explored_nodes, scc_membership, 6, scc_size)

        self.assertEqual(scc_size, 3)
        self.assertEqual(explored_nodes, [True, False, False, True, False, False, True, False, False])
        self.assertEqual(scc_membership, [6, -1, -1, 6, -1, -1, 6, -1, -1])

        scc_size = 0
        scc_size = scc.dfs2(G, 8, explored_nodes, scc_membership, 8, scc_size)

        self.assertEqual(scc_size, 3)
        self.assertEqual(explored_nodes, [True, False, True, True, False, True, True, False, True])
        self.assertEqual(scc_membership, [6, -1, 8, 6, -1, 8, 6, -1, 8])

        scc_size = 0
        scc_size = scc.dfs2(G, 7, explored_nodes, scc_membership, 7, scc_size)

        self.assertEqual(scc_size, 3)
        self.assertEqual(explored_nodes, [True, True, True, True, True, True, True, True, True])
        self.assertEqual(scc_membership, [6, 7, 8, 6, 7, 8, 6, 7, 8])


# dfs1_loop(Grev)
class TestDFS1Loop(unittest.TestCase):

    def test_dfs1_loop_1(self):
        filename = "SCC2.txt"
        G, Grev = scc.read_graph_from_file(filename)
        fintime_nodes = scc.dfs1_loop(Grev)
        self.assertEqual(fintime_nodes, [6, 2, 0, 7, 1, 4, 8, 3, 5])


# def2_loop(G, search_order)
class TestDFS2Loop(unittest.TestCase):

    def test_dfs2_loop_1(self):
        filename = "SCC2.txt"
        G, Grev = scc.read_graph_from_file(filename)
        fintime_nodes = scc.dfs1_loop(Grev)
        search_order = scc.get_search_order_for_second_pass(fintime_nodes)
        scc_sizes, scc_membership = scc.dfs2_loop(G, search_order)

        self.assertEqual(scc_sizes, [3, 3, 3])
        self.assertEqual(scc_membership, [6, 7, 8, 6, 7, 8, 6, 7, 8])


# get_search_order_for_second_pass(fintime_nodes)
class TestGetSearchOrder(unittest.TestCase):

    def test_get_search_order_1(self):
        filename = "SCC2.txt"
        G, Grev = scc.read_graph_from_file(filename)
        fintime_nodes = scc.dfs1_loop(Grev)
        search_order = scc.get_search_order_for_second_pass(fintime_nodes)
        self.assertEqual(search_order, [[6, 8], [3, 7], [0, 6], [8, 5], [5, 4], [7, 3], [1, 2], [4, 1], [2, 0]])


if __name__ == '__main__':
    unittest.main()