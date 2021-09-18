from .config import DIRECTIONS, VALID_COMMANDS
from .command import Command

class Rover(Command):
    def __init__(self, plateau, rover_landing):
        super().__init__(plateau)
        self.rover_landing = rover_landing
        self.direction_lookup = {}

        for key, val in DIRECTIONS.items():
            self.direction_lookup[val] = key

    def get_command(self, instructions):
        '''
        It will return next command for rover
        :param instructions: list of commands
        :return: None
        '''
        for cmd in instructions:
            yield cmd

    def rover_processing(self, instructions):
        '''
        it will pass command for rover and do process
        :param instructions: list of command
        :return: None
        '''
        for cmd in self.get_command(instructions):
            if cmd in VALID_COMMANDS:
                self.process_commad(cmd)
            else:
                print("Invalid command.")

    def process_commad(self, cmd):
        '''
        it will execute command to rover
        :param cmd: command to rover
        :return: None
        '''
        self.do_command(cmd, self.rover_landing)


    def __str__(self):
        return '{}:{} {} {}'.format(
            self.rover_landing.name,
            self.rover_landing.end_x,
            self.rover_landing.end_y,
            self.direction_lookup[self.rover_landing.end_head]
        )