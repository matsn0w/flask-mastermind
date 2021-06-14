from errors.validationerror import ValidationError

class Player():
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name;

    @name.setter
    def name(self, value):
        if value == '' or value == None:
            raise ValidationError('Enter a name!')
        
        self._name = value
