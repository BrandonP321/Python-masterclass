low = 1
high = 1000

print(f"Think of a number between {low} and {high}")
input("Press ENTER to start")

guesses = 1
while low != high:  #set to while true instead of while guess != answer because
                    #we don't need to define answer and we will tell the code
                    #when to break instead of it breaking when the condition is false
    print(f"\tGuessing in the range of {low} to {high}")
    guess = low + (high - low) // 2
    high_low = input(f"My guess is {guess}.  Should I guess higher or lower? "
                     "Enter h, l, or c if my guess was correct.").casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print(f"I got it in {guesses} guesses!")
        break
    else:
        print("Please enter h, l, or c")
    guesses += 1
else:
    print(f"You are thinking of the number {low}")
    print(f"I got it in {guesses} guesses")