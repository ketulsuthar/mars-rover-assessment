
from mars_rover import Plateau
from mars_rover import RoverLanding
from mars_rover import  Rover
def main():

    plateau = Plateau(5, 5)
    rover_landing = RoverLanding('Rover1', 1, 2, 'N')
    rover = Rover(plateau, rover_landing)
    rover.rover_processing('LMLMLMLMM')
    print(rover)

    rover_landing = RoverLanding('Rover2', 3, 3, 'E')
    rover = Rover(plateau, rover_landing)
    rover.rover_processing('MMRMMRMRRM')
    print(rover)



if __name__ == '__main__':
    main()
