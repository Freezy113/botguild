class Bot:
    def __init__(self, position, color):
        self._position = position
        self._color = color

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position

    def currentPosition(self):
        return self._position