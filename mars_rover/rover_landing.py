from .config import DIRECTIONS

class RoverLanding:
    def __init__(self, name, x, y, head='N'):
        self.name = name
        self.start_x = x
        self.start_y = y
        self.end_x = x
        self.end_y = y
        self.start_head = DIRECTIONS[head]
        self.end_head = DIRECTIONS[head]
