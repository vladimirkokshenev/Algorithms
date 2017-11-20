import unittest
import sys
sys.path.append('''C:\Git\Algorithms''')
import clustering


class TestDisjointSet(unittest.TestCase):
    """ Testing disjoint set implementation: order of methods matter! """

    def test_init_1(self):
        dj_set = clustering.DisjointSet(5)
        self.assertEqual(dj_set.parent, [0, 1, 2, 3, 4])
        self.assertEqual(dj_set.rank, [0, 0, 0, 0, 0])
        self.assertEqual(dj_set.size, 5)

    def test_basic_find_1(self):
        dj_set = clustering.DisjointSet(4)
        self.assertEqual(dj_set.parent, [0, 1, 2, 3])
        self.assertEqual(dj_set.rank, [0, 0, 0, 0])
        self.assertEqual(dj_set.size, 4)
        self.assertEqual(dj_set.find(3), 3)

    def test_basic_join_1(self):
        dj_set = clustering.DisjointSet(5)
        dj_set.join(0, 1)
        self.assertEqual(dj_set.parent, [0, 0, 2, 3, 4])
        self.assertEqual(dj_set.rank, [1, 0, 0, 0, 0])
        dj_set.join(2, 3)
        self.assertEqual(dj_set.parent, [0, 0, 2, 2, 4])
        self.assertEqual(dj_set.rank, [1, 0, 1, 0, 0])
        dj_set.join(2, 4)
        self.assertEqual(dj_set.parent, [0, 0, 2, 2, 2])
        self.assertEqual(dj_set.rank, [1, 0, 1, 0, 0])
        dj_set.join(2, 0)
        self.assertEqual(dj_set.parent, [2, 0, 2, 2, 2])
        self.assertEqual(dj_set.rank, [1, 0, 2, 0, 0])
        self.assertEqual(dj_set.parent[1], 0)
        self.assertEqual(dj_set.find(1), 2)
        self.assertEqual(dj_set.parent[1], 2)


class TestGetInt(unittest.TestCase):

    def test_1(self):
        self.assertEqual(clustering.get_int([1, 0, 1, 0, 1]), 21)
        self.assertEqual(clustering.get_int([1]), 1)


class TestGetDistance(unittest.TestCase):

    def test_1(self):
        self.assertEqual(clustering.get_distance(1, 2), 2)
        self.assertEqual(clustering.get_distance(21, 18), 3)



if __name__ == '__main__':
    unittest.main()