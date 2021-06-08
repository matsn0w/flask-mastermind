from random import randint

class Game:
    def __init__(self, player, doubles = False, colors = 6, position = 4):
        self.__MIN_COLORS = 6
        self.__MAX_COLORS = 10
        self.__MIN_POSITIONS = 4
        self.__MAX_POSITIONS = 10 

        self.player = player
        self.doubles = doubles
        self._colors = colors
        self._position = position

        self.generateCode()

    @property
    def colors(self):
        return self._colors

    @colors.setter
    def colors(self, value):
        if value < self.__MIN_COLORS or value > self.__MAX_COLORS:
            raise ValidationError(f'The amount of colors must be between {self.__MIN_COLORS} and {self.__MAX_COLORS}!')

        pass

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if value < self.__MIN_POSITIONS or value > self.__MAX_POSITIONS:
            raise ValidationError(f'The amount of positions must be between {self.__MIN_POSITIONS} and {self.__MAX_POSITIONS}!')

        pass

    def generateCode(self):
        code = []
        for i in range(self.position): 
            while True:
                number = randint(0, self.colors)

                if self.doubles or not number in code:
                    code.append(number)
                    break

        self.code = code
        



        

class ValidationError(Exception):
    pass
