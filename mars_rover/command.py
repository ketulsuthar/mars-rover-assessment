from .config import VALID_COMMANDS
from .config import DIRECTIONS


class Command:

    def __init__(self, plateau):
        self.plateau = plateau

    def move_left(self, current_pos):
        '''
        It will spin rover 90 degrees left
        :param current_pos: Current position of rover
        :return:
        '''
        head = current_pos.end_head - 1
        if head < DIRECTIONS['N']:
            current_pos.end_head = DIRECTIONS['W']
        else:
            current_pos.end_head = head

    def move_right(self, current_pos):
        '''
        It will spin rover 90 degrees right
        :param current_pos: Current position of rover
        :return:
        '''
        head = current_pos.end_head  + 1
        if head > DIRECTIONS['W']:
            current_pos.end_head = DIRECTIONS['N']
        else:
            current_pos.end_head = head

    def move(self, current_pos):
        '''
        It will move rover forward one grid point.
        :param current_pos: Current position of rover
        :return:
        '''
        if self.plateau.validate_move(current_pos):
            if current_pos.end_head == DIRECTIONS['N']:
                current_pos.end_y += 1
            elif current_pos.end_head == DIRECTIONS['E']:
                current_pos.end_x += 1
            elif current_pos.end_head == DIRECTIONS['S']:
                current_pos.end_y -= 1
            elif current_pos.end_head == DIRECTIONS['W']:
                current_pos.end_x -= 1
        else:
            print('Invalid move')

    def do_command(self, command, current_pos):
        if command.upper() == "L":
             self.move_left(current_pos)
        if command.upper() == "R":
            self.move_right(current_pos)
        if command.upper() == "M":
            self.move(current_pos)






