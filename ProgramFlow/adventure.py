availableExits = ["north", "south", "east", "west"]

chosenExit = None
while chosenExit not in availableExits:
    chosenExit = input("Please choose a direction: ").casefold()
    if chosenExit == "quit":
        print("Game over")
        break
if chosenExit != "quit":
    print("Aren't you glad you got out of there!")