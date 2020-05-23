activity = input("What would you like to do today? ")

if activity.casefold() not in "cinema":
    print("But I want to go to the cinema!")
else:
    print("aight")