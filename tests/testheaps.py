import unittest
import sys
sys.path.append('''C:\Git\Algorithms''')
import heaps


class TestHeaps(unittest.TestCase):
    """ I am a lazy evil bastard, decided to unittest by extended example """
    def test_min_max_heaps_1(self):

        filename = "Median.txt"
        h_low = heaps.MaxHeap()
        h_high = heaps.MinHeap()
        sum_med = 0
        fp = open(filename)
        x = fp.readline()

        while x != "":
            x = int(x)

            if len(h_low.data) != 0:

                if x < h_low.maximum():
                    h_low.insert(x)
                else:
                    h_high.insert(x)

                if h_low.heapsize() > h_high.heapsize() + 1:
                    z = h_low.pop()
                    h_high.insert(z)

                if h_high.heapsize() > h_low.heapsize() + 1:
                    z = h_high.pop()
                    h_low.insert(z)
            else:
                h_low.insert(x)

            if h_low.heapsize() >= h_high.heapsize():
                cur_med = h_low.maximum()
            else:
                cur_med = h_high.minimum()
            sum_med += cur_med

            x = fp.readline()

        sum_med = sum_med % 10000
        self.assertEqual(sum_med, 1213)


if __name__ == '__main__':
    unittest.main()