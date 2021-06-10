from random import randint

class Game:
    def __init__(self, player, doubles = False, cheats = False, colors = 6, position = 4):
        self.__MIN_COLORS = 6
        self.__MAX_COLORS = 10
        self.__MIN_POSITIONS = 4
        self.__MAX_POSITIONS = 10 

        self._colors = None
        self.colors = colors

        self._positions = None
        self.positions = position

        self.player = player
        self.doubles = doubles
        self.cheats = cheats
        self.results = []
        self.turns = 0

        self.generateCode()

    @property
    def colors(self):
        return self._colors

    @colors.setter
    def colors(self, value):
        if value < self.__MIN_COLORS or value > self.__MAX_COLORS:
            raise ValidationError(f'The amount of colors must be between {self.__MIN_COLORS} and {self.__MAX_COLORS}!')

        self._colors = value

    @property
    def positions(self):
        return self._positions

    @positions.setter
    def positions(self, value):
        if value < self.__MIN_POSITIONS or value > self.__MAX_POSITIONS:
            raise ValidationError(f'The amount of positions must be between {self.__MIN_POSITIONS} and {self.__MAX_POSITIONS}!')

        self._positions = value

    def generateCode(self):
        code = []
        for i in range(self.positions): 
            while True:
                number = randint(1, self.colors)

                if self.doubles or not number in code:
                    code.append(number)
                    break

        self.code = code

    def guess(self, guesses):
        results = []

        for i, num in enumerate(self.code):
            if num == guesses[i]:
                results.append('black')

        for i, num in enumerate(self.code):
            if num in guesses and num != guesses[i]:
                results.append('white')

        self.results.append(results)
        self.turns += 1

    def win(self):
        test = self.results[-1]

        if len(test) < self.positions:
            return False

        for r in test:
            if r != 'black':
                return False

        return True
