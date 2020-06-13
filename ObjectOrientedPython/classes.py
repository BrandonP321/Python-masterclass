# class Kettle(object):
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#
# fordTaurus = Kettle('Ford', 'Taurus', 2007)
# print(fordTaurus.make)
# print(fordTaurus.model)
# print(fordTaurus.year)
#
# fordTaurus.year = 2008
# print(fordTaurus.year)


class Kettle(object):

    power_source = 'electricity'

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle('kenwood', 8.99)
print(kenwood.make)
print(kenwood.price)

print(kenwood.on)
kenwood.switch_on()
print(kenwood.on)

hamilton = Kettle('Hamilton', 12.75)

Kettle.switch_on(hamilton)
print(hamilton.on)

kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power) will produce error since hamilton doesn't have a data attribute 'power'

print(Kettle.power_source)
print(kenwood.power_source)
hamilton.power_source = 'atomic'
print(hamilton.power_source)
