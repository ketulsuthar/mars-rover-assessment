import os
import sys
from mars_rover import Plateau
from mars_rover import RoverLanding
from mars_rover import Rover
from mars_rover import FileParser


def main(file_name):
    try:
        file_parser = FileParser(file_name)
        file_parser.parsers()
        plateau = Plateau(file_parser.plateau['x'], file_parser.plateau['y'])
        for rover in file_parser.rovers:
            rover_landing = RoverLanding(
                rover['name'],
                rover['x'],
                rover['y'],
                rover['head'],
            )
            f_rover = Rover(plateau, rover_landing)
            f_rover.rover_processing(rover['command'])
            print(f_rover)

    except Exception as err:
        print(err)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Missing input file.")
    else:
        file_name = sys.argv[1]
        if os.path.exists(file_name):
            main(file_name)
        else:
            print('file does not exist.')
