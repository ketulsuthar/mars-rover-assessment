import unittest
from mars_rover import Plateau, RoverLanding, Rover

class TestRover(unittest.TestCase):

    def test_constructor(self):
        plateau = Plateau(5, 5)
        rover_landing = RoverLanding('Rover1', 1, 2, 'N')
        rover = Rover(plateau, rover_landing)

        self.assertEqual(rover.rover_landing, rover_landing)

    def test_rover_processing(self):
        plateau = Plateau(5, 5)
        rover_landing = RoverLanding('Rover1', 1, 2, 'N')
        rover = Rover(plateau, rover_landing)
        rover.rover_processing('LMLMLMLMM')
        expected = 'Rover1:1 3 N'
        self.assertEqual(rover.__str__(), expected)

if __name__ == '__main__':
    unittest.main()