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

    # test a leading zero before decimal
    def test5(self):
        number = conv_num("0.53")
        self.assertEqual(number, 0.53)

    # test a leading zero before integer
    def test6(self):
        number = conv_num("053")
        self.assertEqual(number, 53)

    # test with multiple decimals
    def test7(self):
        number = conv_num("0.5.3")
        self.assertEqual(number, None)

    # test a hex number
    def test8(self):
        number = conv_num("0x53")
        self.assertEqual(number, 83)

    # test a hex number with alpha character
    def test9(self):
        number = conv_num("0x5A")
        self.assertEqual(number, 90)

    # test a negative hex number
    def test10(self):
        number = conv_num("-0x5A")
        self.assertEqual(number, -90)

    # test with negative number in wrong position
    def test11(self):
        number = conv_num("0x-5A")
        self.assertEqual(number, None)

    # test hex without leading 0x
    def test12(self):
        number = conv_num("5a")
        self.assertEqual(number, None)

    # test hex with mixed cases
    def test13(self):
        number = conv_num("0X5a7D")
        self.assertEqual(number, 23165)

    # test hex with a decimal present
    def test14(self):
        number = conv_num("0X5a.7D")
        self.assertEqual(number, 90.48828125)

    # test another decimal number
    # note: This test currently fails!
    def test15(self):
        number = conv_num("5123.7122")
        self.assertEqual(number, 5123.7122)

    # test just '0x'
    def test15(self):
        number = conv_num("0x")
        self.assertEqual(number, None)


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
