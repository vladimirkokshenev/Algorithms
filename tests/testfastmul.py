import unittest
import sys
sys.path.append('''C:\Git\Algorithms''')
import fastmul


class TestConversion(unittest.TestCase):
    """Unit tests for convert_string_to_big_integer()    """

    def test_single_digit(self):
        """ Testing convert_string_to_big_integer() with single digit string"""
        s = "1"
        self.assertEqual([1], fastmul.convert_string_to_big_integer(s))

    def test_multiple_digits(self):
        """ Testing convert_string_to_big_integer() with single digit string"""
        s = "1234"
        self.assertEqual([1, 2, 3, 4], fastmul.convert_string_to_big_integer(s))


class TestSplit(unittest.TestCase):
    """Unit tests for split_big_integer()    """

    def test_len1(self):
        """ Testing split_big_integer() with single digit list"""
        arg = [1]
        a, b = fastmul.split_big_integer(arg)
        self.assertEqual(a, [])
        self.assertEqual(b, [1])

    def test_len4(self):
        """ Testing split_big_integer() with list of len 4"""
        arg = [1, 2, 3, 4]
        a, b = fastmul.split_big_integer(arg)
        self.assertEqual(a, [1, 2])
        self.assertEqual(b, [3, 4])

    def test_len5(self):
        """ Testing split_big_integer() with list of len 5"""
        arg = [1, 2, 3, 4, 5]
        a, b = fastmul.split_big_integer(arg)
        self.assertEqual(a, [1, 2])
        self.assertEqual(b, [3, 4, 5])

class TestSum(unittest.TestCase):
    """Unit tests for sum_big_integers()    """

    def test_len1(self):
        """ Testing sum_big_integers() with 2 single digit integers without overflow"""
        a = [1]
        b = [2]
        sum = fastmul.sum_big_integers(a, b)
        self.assertEqual(sum, [3])

    def test_len1overflow(self):
        """ Testing sum_big_integers() with 2 single digit integers with overflow"""
        a = [5]
        b = [6]
        sum = fastmul.sum_big_integers(a, b)
        self.assertEqual(sum, [1, 1])

    def test_len2(self):
        """ Testing sum_big_integers() with 2 double digit integers without overflow"""
        a = [1, 1]
        b = [2, 2]
        sum = fastmul.sum_big_integers(a, b)
        self.assertEqual(sum, [3, 3])

    def test_len2overflow(self):
        """ Testing sum_big_integers() with 2 double digit integers with multiple overflow"""
        a = [9, 9]
        b = [9, 9]
        sum = fastmul.sum_big_integers(a, b)
        self.assertEqual(sum, [1, 9, 8])

    def test_lenmisc(self):
        """ Testing sum_big_integers() with 2 integers of different size with overflow"""
        a = [9, 9]
        b = [2, 9, 9, 9]
        sum = fastmul.sum_big_integers(a, b)
        self.assertEqual(sum, [3, 0, 9, 8])

if __name__ == '__main__':
    unittest.main()
