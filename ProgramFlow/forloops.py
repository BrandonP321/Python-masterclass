# parrot = "Norwegian Blue"
#
# for character in parrot:
#     print(character)

number = '9,223;372:036 854,775;807'
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char
print(seperators)

things = ["bed", "computer", "red", "desk"]
space = ""

for i in things:
    if not "ed" in i:
        space = space + i + " "
print(space)

print()

quote = """Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?"""
capitals = ""

for i in quote:
    if i.isupper():
        capitals = capitals + i
print(capitals)

upperCase = ""

for i in quote:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        upperCase = upperCase + i
print(upperCase)
