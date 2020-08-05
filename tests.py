import unittest
from task import conv_num, my_datetime, conv_endian


<<<<<<< Updated upstream
class TestCase(unittest.TestCase):
=======
class TestConvNum(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)


class TestDateTime(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)


class TestEndian(unittest.TestCase):
>>>>>>> Stashed changes

    def test1(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
