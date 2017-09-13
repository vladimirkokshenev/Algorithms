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

    def test_sum_len1(self):
        """ Testing sum_big_integers() with 2 single digit integers without overflow"""
        a = [1]
        b = [2]
        sum = fastmul.sum_big_integers(a, b)
        self.assertEqual(sum, [3])

    def test_sum_len1overflow(self):
        """ Testing sum_big_integers() with 2 single digit integers with overflow"""
        a = [5]
        b = [6]
        sum = fastmul.sum_big_integers(a, b)
        self.assertEqual(sum, [1, 1])

    def test_sum_len2(self):
        """ Testing sum_big_integers() with 2 double digit integers without overflow"""
        a = [1, 1]
        b = [2, 2]
        sum = fastmul.sum_big_integers(a, b)
        self.assertEqual(sum, [3, 3])

    def test_sum_len2overflow(self):
        """ Testing sum_big_integers() with 2 double digit integers with multiple overflow"""
        a = [9, 9]
        b = [9, 9]
        sum = fastmul.sum_big_integers(a, b)
        self.assertEqual(sum, [1, 9, 8])

    def test_sum_lenmisc(self):
        """ Testing sum_big_integers() with 2 integers of different size with overflow"""
        a = [9, 9]
        b = [2, 9, 9, 9]
        sum = fastmul.sum_big_integers(a, b)
        self.assertEqual(sum, [3, 0, 9, 8])


class TestShift(unittest.TestCase):
    """Unit Tests for shifting big integers"""

    def test_shift_a_n(self):
        """ Test shifting of 3 digit integer for 3 positions"""
        a = [1, 2, 3]
        n = 3
        self.assertEqual(fastmul.shift_big_integer(a, n), [1, 2, 3, 0, 0, 0])


class TestMul(unittest.TestCase):
    """Unit tests for multiplication"""

    def test_mul_x1(self):
        """ Testing mul_big_integers(x, y) with single digit x and without overflow"""
        x = [2]
        y = [2, 2]
        mul = fastmul.mul_big_integers(x, y)
        self.assertEqual(mul, [4, 4])

    def test_mul_x1_overflow(self):
        """ Testing mul_big_integers(x, y) with single digit x and with overflow"""
        x = [9]
        y = [9, 9, 9]
        mul = fastmul.mul_big_integers(x, y)
        self.assertEqual(mul, [8, 9, 9, 1])

    def test_mul_y1(self):
        """ Testing mul_big_integers(x, y) with single digit y and without overflow"""
        x = [2, 2]
        y = [2]
        mul = fastmul.mul_big_integers(x, y)
        self.assertEqual(mul, [4, 4])

    def test_mul_y1_overflow(self):
        """ Testing mul_big_integers(x, y) with single digit y and with overflow"""
        x = [9, 9, 9]
        y = [9]
        mul = fastmul.mul_big_integers(x, y)
        self.assertEqual(mul, [8, 9, 9, 1])

    def test_mul_x2_y2(self):
        """Testing multiplication of 2-digit numbers"""
        x = [3, 7]
        y = [7, 3]
        self.assertEqual(fastmul.mul_big_integers(x, y), [2, 7, 0, 1])

    def test_mul_x4_y4(self):
        """Testing multiplication of 4-digit numbers"""
        x = [1, 2, 3, 4]
        y = [5, 6, 7, 8]
        self.assertEqual(fastmul.mul_big_integers(x, y), [7, 0, 0, 6, 6, 5, 2])

    def test_mul_x6_y3(self):
        """Testing multiplication of 6-digit and 3-digit numbers"""
        x = [1, 2, 3, 4, 5, 6]
        y = [9, 8, 7]
        self.assertEqual(fastmul.mul_big_integers(x, y), [1, 2, 1, 8, 5, 1, 0, 7, 2])

    def test_mul_real_big(self):
        """Test multiplication with really big numbers"""
        a = 2718281828459045235360287471352662497757247093699959574966967627
        b = 3141592653589793238462643383279502884197169399375105820974944592
        a_str = str(a)
        b_str = str(b)
        x = fastmul.convert_string_to_big_integer(a_str)
        y = fastmul.convert_string_to_big_integer(b_str)
        res = fastmul.convert_string_to_big_integer(str(a*b))
        self.assertEqual(fastmul.mul_big_integers(x, y), res)


if __name__ == '__main__':
    unittest.main()
