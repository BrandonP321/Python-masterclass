parrot= "Norwegian Blue"
letter = input("Enter a character: ")

if letter in parrot:
    print(f"{letter} is in {parrot}")
else:
    print("{} is not in {}".format(letter, parrot))  #Showed 2 ways to format on lines 5 and 7