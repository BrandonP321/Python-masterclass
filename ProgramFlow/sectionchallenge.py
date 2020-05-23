options = ["Learn Python", "Learn Java", "Go Swimming", "Have Dinner", "Go to Bed"]

menu = "1. Learn Python\n" \
       "2. Learn Java\n" \
       "3. Go Swimming\n" \
       "4. Have Dinner\n" \
       "5. Go to Bed\n" \
       "0. Exit"

print("Please choose an option from the list below:")
print(menu)

while True:
    choice = int(input("Make your choice: "))

    if choice == 0:
        print("See ya!")
        break
    elif 1 <= choice <= 5:
        print(f"You chose to {options[choice - 1]}")
        print("Choose again")
    else:
        print("You have to choose from the list:")
        print(menu)
