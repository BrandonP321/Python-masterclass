import random


class Enemy(object):

    def __init__(self, name='Enemy', hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._total_hit_points = hit_points
        self._alive = True

    def take_damage(self, amount):
        remaining_points = self._hit_points - amount
        if remaining_points > 0:
            self._hit_points = remaining_points
            print(f"I took {amount} damage points and have {self._hit_points} left.")
        else:
            self._lives -= 1
            if self._lives > 0:
                self._hit_points = self._total_hit_points
                print(f"{self._name} has lost a life")
            else:
                self._alive = False
                print(f"{self._name} is dead")

    def __str__(self):
        return f"Name: {self._name}, Lives: {self._lives}, Hit Points: {self._hit_points}"


class Troll(Enemy):

    # going to call the 'init' method from the superclass to set attribute values for this class
    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)
        # all produce the same result, just different syntax
        # super(Troll, self).__init__(self, name=name, lives=1, hit_points=23) super(Troll, self) is still implied in
        # the first example
        # Enemy.__init__(self, name=name, lives=1, hit_points=23) this is the only one that will work with python 2

    def grunt(self):
        print(f"Me {self._name}.  {self._name} stomp you.")


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodged(self):
        if random.randint(1, 3) == 3:
            print(f"***** {self._name} dodged *****")
            return True
        else:
            return False

    # example of overriding a method
    def take_damage(self, amount):
        if not self.dodged():
            super().take_damage(amount=amount)  # good practice to use 'amount=amount' vs just 'amount'


class VampireKing(Vampire):

    # this will create an object identical to the vampire class
    def __init__(self, name):
        super().__init__(name)
        # not sure why yet but the _hit_points need to be assigned outside of the super method here
        # has something to do with 'lives' and 'hit_points' not being used as parameters for init of vampire class
        self._hit_points = 140

    def take_damage(self, amount):
        super().take_damage(amount // 4)
