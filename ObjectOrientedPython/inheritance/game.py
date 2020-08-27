from player import Player
from enemy import Enemy, Troll, Vampire, VampireKing

vamp = Vampire("Kyle")
print(vamp)

while vamp._alive:
    vamp.take_damage(2)
    print(vamp)
    print()

print('*' * 40)

king = VampireKing('George')
print(king)

# brandon = Player('brandon')
# print(brandon)  # all that is needed to call the __str__ method for this class instance
# print(brandon.get_lives())  # gets the value of class attribute 'lives'
# brandon.set_lives(50)  # sets the value of class attribute 'lives' to 50
# print(brandon.get_lives())
#
# print()
#
# parker = Player("Parker")
# print(parker)
# parker.set_level(2)
# print(parker)
# parker.set_level(4)
# print(parker)
# parker.set_level(1)
# print(parker)
