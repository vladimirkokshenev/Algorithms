import unittest
import sys
sys.path.append('''C:\Git\Algorithms''')
import mergesort
import random


class TestMergeSort(unittest.TestCase):
    """Unit tests for convert_string_to_big_integer()    """

    def test_msort_1(self):
        """ Testing merge sort for single element list"""
        a = [1]
        self.assertEqual(mergesort.mergesort(a), [1])

    def test_msort_2a(self):
        """ Testing merge sort for sorted 2-element list"""
        a = [1, 2]
        self.assertEqual(mergesort.mergesort(a), [1, 2])

    def test_msort_2a(self):
        """ Testing merge sort for unsorted 2-element list"""
        a = [2, 1]
        self.assertEqual(mergesort.mergesort(a), [1, 2])

    def test_msort_6(self):
        """ Testing merge sort for reversely sorted 6-element array"""
        a = [6, 5, 4, 3, 2, 1]
        self.assertEqual(mergesort.mergesort(a), [1, 2, 3, 4, 5, 6])

    def test_msort_on_random_input(self):
        """10 randmon samples test"""
        for i in range(10):
            a = random.sample(xrange(100), 100)
            b = list(a)
            b.sort()
            self.assertEqual(b, mergesort.mergesort(a))

if __name__ == '__main__':
    unittest.main()
