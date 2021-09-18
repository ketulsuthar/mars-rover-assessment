import unittest
from mars_rover import *

class TestPlateau(unittest.TestCase):

    def test_constructor(self):
        plateau = Plateau(5, 5)

        self.assertEqual(plateau._x, 5)
        self.assertEqual(plateau._y, 5)

if __name__ == '__main__':
    unittest.main()