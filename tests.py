import unittest
from task import conv_num, my_datetime, conv_endian


class TestConvNum(unittest.TestCase):

    # test a basic string representing an integer
    def test1(self):
        number = conv_num("523")
        self.assertEqual(number, 523)

    # test a float number
    def test2(self):
        number = conv_num("5.3")
        self.assertEqual(number, 5.3)
    
    # test a float number with leading decimal
    def test3(self):
        number = conv_num(".53")
        self.assertEqual(number, 0.53)
    
    # test a float number with trailing decimal
    def test4(self):
        number = conv_num("53.")
        self.assertEqual(number, 53.0)

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
