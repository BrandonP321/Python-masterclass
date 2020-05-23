import time
import shelve
import random

played_question = input("Do you have an existing username with us? (y/n)  ")

with shelve.open('typing-leaderboard') as leader:
    username_list = []
    for name in sorted(leader):
        username_list.append(name)

    if 'y' in played_question:
        username = input("Enter your username or 'help' if you forgot it: ")
        if username == 'help':
            for name in sorted(leader):
                print(name)
            find_username = input("\nDid you find your username? (y/n) ")
            if 'y' in find_username:
                username = input("Username:")
                while username not in username_list:
                    username = input("We don't have that username, please enter again: ")
                print(f"\nHi there, {username}")
            else:
                username = input("Please re-enter the username you'd like to use: ")
                print(f"\nHi there, {username}")
        else:
            if username in username_list:
                print(f"\nHi there {username}")
            while username not in username_list:
                username1 = input("looks like you entered something wrong, try "
                                  "again or type 'n' to make a new username: ")
                if username1 == 'n':
                    username = input("Username: ")
                    while username in username_list:
                        username = input("Looks like that one's taken, enter a "
                                         "new username: ")
                    print(f"\nHi there, {username}")
                    break
    else:
        username = input("Enter your new username: ")
        if username in username_list:
            while username in username_list:
                username1 = input("looks like that username is taken, enter a new "
                                  "username or enter 'y' if that is you: ")
                if username1 == 'y':
                    print(f"\nHi there, {username}")
                    break
                else:
                    username = username1
        else:
            print(f"\nHi there, {username}")
    username_list.append(username)

while 'q' not in input("Press enter to play or 'quit' to leave: "):

    if 'y' in input("\nWould you like to see the leaderboard? "):
        with shelve.open('typing-leaderboard') as leader:
            place = 0
            for board in sorted(leader.items(), key=lambda x: x[1], reverse=True):
                place += 1
                print(f"{place:2}. {board[0]} Score: {board[1]}")


    with shelve.open('typing-phrases') as phrases:
        phrase = phrases[str(random.randint(0, 4))]


    word_count = 1
    for i in range(len(phrase) - 1):
        if phrase[i] == " " and phrase[i + 1] == " ":
            continue
        elif phrase[i] == " ":
            word_count += 1

    print("\nYour phrase is: " + phrase + "\n")


    input("Press enter when ready!")

    print("begin typing in")
    time.sleep(2)
    counter = 3
    while counter > 0:
        print(counter)
        counter -= 1
        time.sleep(1)
    print("GO")
    print(phrase)
    start_time = time.time()
    typed = input("")
    end_time = time.time()


    char_count = 0
    for char in phrase:
        char_count += 1


    error_count = 0
    for i in range(len(typed)):
        if i <= len(phrase) - 1 and phrase[i] != typed[i]:
            error_count += 1
        if i > len(phrase) - 1:
            error_count += 1
    if len(typed) < len(phrase):
        error_count += (len(phrase) - len(typed))

    accuracy = int(((char_count - error_count) / char_count) * 100)
    words_per = (word_count * 60) / (end_time - start_time)
    overall = int(words_per * (accuracy / 100))
    print(f"\nWPM: {int(words_per)}")
    print(f"Accuracy: {accuracy}%")
    print(f"Overall score: {overall}\n")

    with shelve.open('typing-leaderboard') as leader:
        in_leader = False
        for name in sorted(leader.keys()):
            if username == name:
                in_leader = True

        if in_leader is True and overall > leader[username]:
            print(f"Congratulations, {username}! You beat your previous "
                  f"high score of {leader[username]}!  Check out the new leaderboard.")
            leader[username] = overall
            place = 0
            for user in sorted(leader.items(), key=lambda x: x[1], reverse=True):
                place += 1
                print(f"{place}. {user[0]} Score: {user[1]}")


        elif in_leader is False:
            print(f"Congratulations on your first game, your score of {overall} "
                  f"has been added to leaderboard, check it out!")
            leader[username] = overall
            place = 0
            for user in sorted(leader.items(), key=lambda x: x[1], reverse=True):
                place += 1
                print(f"{place}. {user[0]} Score: {user[1]}")

        else:
            print(f"Sorry, {username} but it looks like you couldn't beat "
                  f"your high score of {leader[username]} this time.")
    print()
