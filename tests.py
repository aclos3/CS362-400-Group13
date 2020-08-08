import unittest
from task import conv_num, my_datetime, conv_endian


class TestConvNum(unittest.TestCase):

    # test a basic string representing an integer
    def test1(self):
        number = conv_num("523")
        self.assertEqual(number, 523)


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

    def test_positive_little_1(self):
        endian = conv_endian(4987673, 'little')
        self.assertEqual(endian, '19 1B 4C')

    def test_positive_little_2(self):
        endian = conv_endian(12, 'little')
        self.assertEqual(endian, '0C')

    def test_negative_big_1(self):
        endian = conv_endian(-954786, 'big')
        self.assertEqual(endian, '-0E 91 A2')

    def test_negative_little_1(self):
        endian = conv_endian(-87458, 'little')
        self.assertEqual(endian, '-A2 55 01')

    def test_zero(self):
        endian = conv_endian(0)
        self.assertEqual(endian, '00')


if __name__ == '__main__':
    unittest.main()
