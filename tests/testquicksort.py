import unittest
import sys
sys.path.append('''C:\Git\Algorithms''')
import quicksort
import random


class TestChoosePivotFirst(unittest.TestCase):
    """Unit tests for choose_pivot_first()    """

    def test_choose_pivot_first_1(self):
        """ Testing choose_pivot_first() for single element list"""
        a = [1]
        p, i = quicksort.choose_pivot_first(a, 0, 0)
        self.assertEqual(p, 1)
        self.assertEqual(i, 0)

    def test_choose_pivot_first_mult(self):
        """ Testing choose_pivot_first() for multiple element list"""
        a = [1, 2, 3]
        p, i = quicksort.choose_pivot_first(a, 1, 2)
        self.assertEqual(p, 2)
        self.assertEqual(i, 1)


class TestChoosePivotLast(unittest.TestCase):
    """Unit tests for choose_pivot_last()    """

    def test_choose_pivot_last_1or2(self):
        """ Testing choose_pivot_last() for single element list"""
        a = [1]
        p, i = quicksort.choose_pivot_last(a, 0, 0)
        self.assertEqual(p, 1)
        self.assertEqual(i, 0)
        a = [2, 1]
        p, i = quicksort.choose_pivot_last(a, 0, 1)
        self.assertEqual(p, 1)
        self.assertEqual(i, 1)

    def test_choose_pivot_last_mult(self):
        """ Testing choose_pivot_last() for multiple element list"""
        a = [1, 2, 3]
        p, i = quicksort.choose_pivot_last(a, 1, 2)
        self.assertEqual(p, 3)
        self.assertEqual(i, 2)


class TestChoosePivotMedian(unittest.TestCase):
    """Unit tests for choose_pivot_median()    """

    def test_choose_pivot_median_1(self):
        """ Testing choose_pivot_median() for single element list"""
        a = [1]
        p, i = quicksort.choose_pivot_median(a, 0, 0)
        self.assertEqual(p, 1)
        self.assertEqual(i, 0)

    def test_choose_pivot_median_3(self):
        """ Testing choose_pivot_median() for 3 element list"""
        a = [1, 2, 3]
        p, i = quicksort.choose_pivot_median(a, 0, 2)
        self.assertEqual(p, 2)
        self.assertEqual(i, 1)

        a = [1, 3, 2]
        p, i = quicksort.choose_pivot_median(a, 0, 2)
        self.assertEqual(p, 2)
        self.assertEqual(i, 2)

        a = [2, 1, 3]
        p, i = quicksort.choose_pivot_median(a, 0, 2)
        self.assertEqual(p, 2)
        self.assertEqual(i, 0)

        a = [2, 3, 1]
        p, i = quicksort.choose_pivot_median(a, 0, 2)
        self.assertEqual(p, 2)
        self.assertEqual(i, 0)

        a = [3, 1, 2]
        p, i = quicksort.choose_pivot_median(a, 0, 2)
        self.assertEqual(p, 2)
        self.assertEqual(i, 2)

        a = [3, 2, 1]
        p, i = quicksort.choose_pivot_median(a, 0, 2)
        self.assertEqual(p, 2)
        self.assertEqual(i, 1)

    def test_choose_pivot_median_m(self):
        """ Testing choose_pivot_median() for m element list"""
        a = [1, 2, 3, 6, 7, 4, 0, 9]
        p, i = quicksort.choose_pivot_median(a, 4, 7)
        self.assertEqual(p, 7)
        self.assertEqual(i, 4)
        p, i = quicksort.choose_pivot_median(a, 1, 5)
        self.assertEqual(p, 4)
        self.assertEqual(i, 5)


class TestQuickSort(unittest.TestCase):
    """Unit tests for quicksort()    """

    def test_quicksort_3(self):
        """ Testing choose_pivot_first() for 3 element list"""
        a = [1, 2, 3]
        c = quicksort.quicksort(a, 0, 2, quicksort.choose_pivot_first)
        self.assertEqual(a, [1, 2, 3])
        self.assertEqual(c, 3)

        a = [1, 2, 3]
        c = quicksort.quicksort(a, 0, 2, quicksort.choose_pivot_median)
        self.assertEqual(a, [1, 2, 3])
        self.assertEqual(c, 2)

        a = [3, 2, 1]
        c = quicksort.quicksort(a, 0, 2, quicksort.choose_pivot_median)
        self.assertEqual(a, [1, 2, 3])
        self.assertEqual(c, 2)

    def test_quicksort_8(self):
        """ Testing choose_pivot_first() for 8 element list """
        a = [3, 8, 2, 5, 1, 4, 7, 6]
        c = quicksort.quicksort(a, 0, 7, quicksort.choose_pivot_first)
        self.assertEqual(a, [1, 2, 3, 4, 5, 6, 7, 8])

        a = [3, 8, 2, 5, 1, 4, 7, 6]
        c = quicksort.quicksort(a, 0, 7, quicksort.choose_pivot_last)
        self.assertEqual(a, [1, 2, 3, 4, 5, 6, 7, 8])

        a = [3, 8, 2, 5, 1, 4, 7, 6]
        c = quicksort.quicksort(a, 0, 7, quicksort.choose_pivot_median)
        self.assertEqual(a, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_quicksort_random(self):
        """ Test quicksort() for random 100 element list"""
        for i in range(10):
            a = random.sample(xrange(100), 100)
            b = list(a)
            b.sort()
            quicksort.quicksort(a, 0, 99, quicksort.choose_pivot_median)
            self.assertEqual(b, a)

    def test_quicksort_sampledata(self):
        """ Test on sample data counting comparisons """
        fp = open('quicksort.txt')
        a = []
        l = fp.readline()
        while l != "":
            a.append(int(l))
            l = fp.readline()

        b = list(a)
        c = quicksort.quicksort(b, 0, 9999, quicksort.choose_pivot_first)
        self.assertEqual(c, 162085)

        b = list(a)
        c = quicksort.quicksort(b, 0, 9999, quicksort.choose_pivot_last)
        self.assertEqual(c, 164123)

        b = list(a)
        c = quicksort.quicksort(b, 0, 9999, quicksort.choose_pivot_median)
        self.assertEqual(c, 138382)


if __name__ == '__main__':
    unittest.main()