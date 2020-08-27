# demo of raising exceptions
class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        # no ()'s means that self.fly is only a reference to aviate, it's not actually calling the method
        self.fly = self.aviate

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin!")

    def aviate(self):
        print("I won the lottery and bought a jet!")


class Mallard(Duck):
    pass


class Flock(object):

    def __init__(self):
        self.flock = []

    # add_duck(self, duck: <type of duck>) -> <return type>:
    def add_duck(self, duck: Duck) -> None:  # causes a hint be raised if a parameter of the wrong type is used
        # assigns attribute 'fly
        fly_method = getattr(duck, 'fly', None)  # getattr(object, 'name', default=None) = object.name, if object.name
#                                                  doesn't exist, the default is returned if provided
        if callable(fly_method):  # checks if fly_method is callable
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, are you sure in'ts not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("Testing exception handler in migrate")  # TODO remove this before release
            except AttributeError as e:
                print('One duck down')
                problem = e
                # raise
        if problem:
            raise problem


if __name__ == '__main__':
    donald = Duck()
    donald.fly()

