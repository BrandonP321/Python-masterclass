fruit = {"apple": 'a round, red fruit',
         "Orange": "An orange, citrus fruit",
         "Pear": "An odd shaped apple"}

while True:
    guess = input("What fruit are you looking for? ")
    if guess == "quit":
        break
    else:
        fruit.get(guess)
