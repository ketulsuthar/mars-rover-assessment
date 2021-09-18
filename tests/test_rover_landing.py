import unittest
from mars_rover import *

class TestRoverLanding(unittest.TestCase):

    def test_constructor(self):
        rover_landing = RoverLanding("Rover1", 1, 2, 'W')

        self.assertEqual(rover_landing.name, 'Rover1')
        self.assertEqual(rover_landing.start_x, 1)
        self.assertEqual(rover_landing.start_y, 2)
        self.assertEqual(rover_landing.end_x, 1)
        self.assertEqual(rover_landing.end_y, 2)
        self.assertEqual(rover_landing.start_head, 4)
        self.assertEqual(rover_landing.end_head, 4)

if __name__ == '__main__':
    unittest.main()