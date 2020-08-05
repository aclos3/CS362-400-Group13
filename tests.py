import unittest
from task import conv_num, my_datetime, conv_endian


class TestConvNum(unittest.TestCase):

    def test1(self):
        number = conv_num(5)
        self.assertEqual(number, 0)


class TestDateTime(unittest.TestCase):

    def test1(self):
        datetime = my_datetime(45000)
        self.assertEqual(datetime, '')


class TestEndian(unittest.TestCase):

    def test_invalid_endianness(self):
        endian = conv_endian(234500, 'nothing')
        self.assertEqual(endian, None)

    def test_positive_big_1(self):
        endian = conv_endian(954786, 'big')
        self.assertEqual(endian, '0E 91 A2')

    def test_positive_big_2(self):
        endian = conv_endian(95478689)
        self.assertEqual(endian, '05 B0 E3 A1')


if __name__ == '__main__':
    unittest.main()
