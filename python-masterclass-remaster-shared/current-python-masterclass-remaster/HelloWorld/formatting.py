# for i in range (1,13):
#     print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

number = '9,223;372:036 854,775;807'
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char
print(seperators)

things = ["bed", "computer", "red", "desk"]
space = ""

for i in things:
    if "ed" in i:
        space = space + i + " "
print(space)c