name = input("Please enter your name: ")
age = int(input(f"Please enter your age, {name}: "))

if 18 <= age <= 30:
    print(f"Congratulations, {name}, you can go on holiday!")
elif age >30:
    print(f"Sorry, {name} but you are {age - 30} years too late for this one :(")
else:
    print(f"Sorry, {name} but you'll be able to go on holiday in {18-age} years.")