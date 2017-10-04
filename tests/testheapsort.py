import unittest
import sys
sys.path.append('''C:\Git\Algorithms''')
import heapsort
import random


# max_heapify(A, i, heap_size)
class TestMaxHeapify(unittest.TestCase):
    """Unit tests for max_heapify(A, i, heap_size) """

    def test_max_heapify_1(self):
        """ Testing max_heapify(A, i, heap_size) """
        A = [5, 6, 1]
        heapsort.max_heapify(A, 0, 2)
        self.assertEqual(A, [6, 5, 1])

    def test_max_heapify_2(self):
        """ Testing max_heapify(A, i, heap_size) """
        A = [3, 6, 1, 4, 5]
        heapsort.max_heapify(A, 0, 4)
        self.assertEqual(A, [6, 5, 1, 4, 3])

    def test_max_heapify_3(self):
        """ Testing max_heapify(A, i, heap_size) """
        A = [3, 6, 1, 4, 5]
        heapsort.max_heapify(A, 0, 3)
        self.assertEqual(A, [6, 4, 1, 3, 5])


# build_max_heap(A)
class TestBuildMaxHeap(unittest.TestCase):
    """Unit tests for build_max_heap(A) """

    def test_max_heapify_1(self):
        """ Testing build_max_heap(A) """
        A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        heapsort.build_max_heap(A)
        self.assertEqual(A, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])


# heapsort(A)
class TestHeaposrt(unittest.TestCase):
    """Unit tests for heapsort(A) """

    def test_quicksort_random(self):
        """ Test heapsort(A) for random 100 element list"""
        for i in range(10):
            A = random.sample(xrange(100), 100)
            B = list(A)
            B.sort()
            heapsort.heapsort(A)
            self.assertEqual(B, A)

if __name__ == '__main__':
    unittest.main()