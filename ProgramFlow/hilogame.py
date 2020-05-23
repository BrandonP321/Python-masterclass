import random

highest = random.randint(10, 51)
answer = (random.randint(1, highest))
print("*type 0 to quit the game")
print()
print("Attempt 1")

guess = int(input(f"Guess a number between 1 and {highest}: "))
attempt = 0

while guess != answer and guess != 0:
    print(f"Attempt {attempt + 2}")
    if guess > answer:
        guess = int(input("Too high, guess lower: "))
        attempt += 1
    elif guess == "":
        guess = int(input("Oops, try again: "))
    else:
        guess = int(input("Too low, guess higher: "))
        attempt += 1

print()

if guess == 0:
    print("You quit the game :(")
    print(f"The answer was {answer}")

if guess == answer:
    if guess == answer and attempt == 0:
        print("You guessed it right first try!")
        print("Game Over")
    else:
        print(f"You got it right in {attempt + 1} guesses!")
        print("Game Over")