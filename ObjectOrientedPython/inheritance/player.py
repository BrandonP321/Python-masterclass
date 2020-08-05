class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3  # the '_' tells the programmer that this is an attribute that probably shouldn't be called
        self._level = 1
        self.score = 0

    def get_lives(self):  # getter used to retrieve the value of self.lives
        return self._lives

    def set_lives(self, lives):  # setter used to set the value of attribute self.lives
        if lives < 0:
            return "lives can not be negative"
        else:
            self._lives = lives

    def get_level(self):
        return self._level

    def set_level(self, new_level):
        if new_level <= 0:
            self._level = 0
            self.score = 0
        else:
            self._level = new_level
            self.score = (self._level - 1) * 1000

    lives = property(get_lives, set_lives)
    level = property(get_level, set_level)

    def __str__(self):  # Used for validation to check each value as they are manipulated
        return f"Name: {self.name}, Lives: {self.lives}, Level: {self.level}, Score: {self.score}"
