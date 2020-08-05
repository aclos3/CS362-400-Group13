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

    def test1(self):
        endian = conv_endian(234500, 'big')
        self.assertEqual(endian, '')


if __name__ == '__main__':
    unittest.main()
