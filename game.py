class Game:
    def __init__(self, player, doubles = False, colors = 6, position = 4):
        self.__MIN_COLORS = 6
        self.__MAX_COLORS = 10
        self.__MIN_POSITIONS = 4
        self.__MAX_POSITIONS = 10 

        self._player = player
        self._doubles = doubles
        self._colors = colors
        self._position = position

    @property
    def _colors(self):
        return self._colors

    @_colors.setter
    def _colors(self, value):
        if (value < self.__MIN_COLORS or value > self.__MAX_COLORS):
            raise Exception(f'The amount of colors must be between {self.__MIN_COLORS} and {self.__MAX_COLORS}!')

        self._colors = value

    @property
    def _position(self):
        return self._position

    @_position.setter
    def _position(self, value):
        if (value < self.__MIN_POSITIONS or value > self.__MAX_POSITIONS):
            raise Exception(f'The amount of positions must be between {self.__MIN_POSITIONS} and {self.__MAX_POSITIONS}!')

        self._position = value
