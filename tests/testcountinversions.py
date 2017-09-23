import unittest
import sys
sys.path.append('''C:\Git\Algorithms''')
import countinversions


class TestCountInversions(unittest.TestCase):
    """Unit tests for count_inversions()    """

    def test_count_inversions_len1(self):
        """ Testing count_inversions() for single element list"""
        a = [1]
        c, b = countinversions.count_inversions(a)
        self.assertEqual(c, 0)

    def test_count_inversions_len2(self):
        """ Testing count_inversions() for single element list"""
        a = [1, 2]
        c, b = countinversions.count_inversions(a)
        self.assertEqual(c, 0)

    def test_count_inversions_len2_inversion(self):
        """ Testing count_inversions() for single element list"""
        a = [2, 1]
        c, b = countinversions.count_inversions(a)
        self.assertEqual(c, 1)

    def test_count_inversions_len6_inversion(self):
        """ Testing count_inversions() for single element list"""
        a = [1, 3, 5, 2, 4, 6]
        c, b = countinversions.count_inversions(a)
        self.assertEqual(c, 3)

if __name__ == '__main__':
    unittest.main()
