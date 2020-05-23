print("Enter 'quit' when done\n")


while True:
    # ask for card number
    credit_num = input("Number: ")

    # allow user to end program
    if credit_num.casefold() == "quit":
        break

    # if input given isn't numeric re-ask for number
    while not credit_num.isdigit():
        print("\nEnter numbers only please\n")
        credit_num = input("Number: ")
        if credit_num == "quit":
            break

    if credit_num == "quit":
        break
    # reset values to 0
    number_count = 0
    validity = 0

    # Luhn's Algorithm for verifying if card number is valid
    for number in credit_num[-2::-2]:
        for digit in str(int(number) * 2):
            number_count += int(digit)
    for number in credit_num[-1::-2]:
        number_count += int(number)

    # check if number is easily divisible by 10 (Luhn's Algorithm)
    if number_count % 10 == 0:
        validity += 1

    # identify type of card and if number length validates card type
    if int(credit_num[0:2]) in [34, 37] and len(credit_num) == 15:
        card_type = "American Express"
        validity += 1
    elif int(credit_num[0:2]) in [51, 52, 53, 54, 55] and len(credit_num) == 16:
        card_type = "MasterCard"
        validity += 1
    elif int(credit_num[0]) == 4 and len(credit_num) in [13, 16]:
        card_type = "Visa"
        validity += 1

    # print either the card type or invalid
    if validity == 2:
        print(card_type + "\n")
    else:
        print("Invalid\n")
