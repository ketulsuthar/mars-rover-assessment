# python package
import os
import sys
# local package
from .plateau import Plateau
from .rover_landing import RoverLanding
from .rover import Rover
from .file_parser import FileParser


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

