import random

highest = random.randint(10, 51)
answer = random.randint(1, highest)
print(f"highest: {highest}")
print(f"answer: {answer}")
guess = int(input(f"Guess a number between 1 and {highest}: "))

# if guess == answer:
#     print("You got it!")
# elif answer < guess <= 10:
#     print("Too high")
# elif 0 < guess < answer:
#     print("Too Low")
# else:
#     print("I said between 1 and 10 dumbass")

if guess == answer:
    print("You got it!")
else:
    if guess < answer:
        print("Guess higher")
    else:
        print("Guess lower")
    guess = int(input())
    if guess == answer:
        print("Second time's a charm!")
    else:
        print("Today's not your lucky day :(")