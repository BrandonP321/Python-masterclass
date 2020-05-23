for i in range(1):
    credit_num = input("Number: ")
    numbers = 0

    for digit in credit_num[-2::-2]:
        for numb in str(int(digit) * 2):
            numbers += int(numb)

    for digit in credit_num[-1::-2]:
        numbers += int(digit)

    if numbers % 10 == 0:
        validity = 1
    else:
        validity = 0
        break

    if credit_num[1:3] in ["34", "37"]:
        card_type = "All American Express"
        if len(credit_num) == 15:
            validity = 1
        else:
            validity = 0
            break

    elif credit_num[1:3] in ["51", "52", "53", "54", "55"]:
        card_type = "MasterCard"
        if len(credit_num) == 16:
            validity = 1
        else:
            validity = 0
            break

    elif credit_num[0] == "4":
        card_type = "Visa"
        if len(credit_num) == 13 or len(credit_num) == 16:
            validity = 1
        else:
            validity = 0
            break
    else:
        validity = 0
        break

if validity == 1:
    print(card_type)
elif validity == 0:
    print("Invalid")
else:
    print("Error")