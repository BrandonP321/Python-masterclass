day = "saturday"
temperature = 22
raining = True


if day == "saturday" and temperature > 27 and not raining:
    print("let's go swimming")
else:
    print("Let's stay home")

if day == "saturday" and temperature > 27 or not raining:
    print("let's go swimming")
else:
    print("Let's stay home")

if (day == "saturday" or temperature > 27) and not raining:
    print("let's go swimming")
else:
    print("Let's stay home")

print()

name = input("Please enter your name: ")
if name != "":
    print("Hello {0}".format(name))
else:
    print("Are you the man with no name?")