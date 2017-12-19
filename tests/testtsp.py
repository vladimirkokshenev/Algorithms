import unittest
import sys
sys.path.append('''C:\Git\Algorithms''')
import tsp


# read_points(filename)
class TestReadPointsFromFile(unittest.TestCase):

    def test_read_points_base_case(self):
        points = tsp.read_points('tsp1.txt')
        self.assertEqual(points, {1: [0.0, 0.0], 2: [0.0, 1.0], 3: [1.0, 0.0], 4: [1.0, 1.0]})


class TestGetDistances(unittest.TestCase):

    def test_get_distances_base_case(self):
        points = tsp.read_points('tsp1.txt')
        distances = tsp.get_distances(points)
        self.assertEqual(distances[(1, 1)], 0.0)
        self.assertEqual(distances[(1, 2)], 1.0)
        self.assertEqual(distances[(1, 3)], 1.0)
        self.assertAlmostEqual(distances[(1, 4)], 1.4142136)


class TestGetSetMask(unittest.TestCase):

    def test_get_set_mask_1(self):
        self.assertEqual(tsp.get_set_mask(set((1, 2, 3, 5, 7)), 8), 234)


if __name__ == '__main__':
    unittest.main()