import unittest
import sys
sys.path.append('''C:\Git\Algorithms''')
import mst


class TestHeaps(unittest.TestCase):
    """  """
    def test_init_1(self):
        a = [10, 5, 0]
        mst_heap = mst.MinHeap(a)
        self.assertEqual(mst_heap.heap, [{"key": 0, "index": 2}, {"key": 5, "index": 1}, {"key": 10, "index": 0}])
        self.assertEqual(mst_heap.heap_position, [2, 1, 0])

        mst_heap.change_key(0, 4)
        self.assertEqual(mst_heap.heap, [{"key": 0, "index": 2}, {"key": 5, "index": 1}, {"key": 4, "index": 0}])
        self.assertEqual(mst_heap.heap_position, [2, 1, 0])

        mst_heap.change_key(1, -1)
        self.assertEqual(mst_heap.heap, [{"key": -1, "index": 1}, {"key": 0, "index": 2}, {"key": 4, "index": 0}])
        self.assertEqual(mst_heap.heap_position, [2, 0, 1])

        min_element = mst_heap.pop()
        self.assertEqual(min_element, {"key": -1, "index": 1})
        self.assertEqual(mst_heap.heap, [{"key": 0, "index": 2}, {"key": 4, "index": 0}])
        self.assertEqual(mst_heap.heap_position, [1, -1, 0])



if __name__ == '__main__':
    unittest.main()