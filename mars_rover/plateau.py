

class Plateau():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def validate_move(self, cur_pos):
        # print(cur_pos.end_x,cur_pos.end_y)
        return cur_pos.end_x >= 0 and cur_pos.end_x <= self._x and cur_pos.end_y >= 0 and cur_pos.end_y <= self._y