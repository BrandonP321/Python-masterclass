# import time
#
# while 'q' not in input("Press enter to play or 'quit' to leave: "):
#     phrase = "Yo, so I just made this type speed game thing.  It has a few bugs I might work out like the " \
#              "fact that if you accidentally add one wrong letter or space that changes the length of the paragraph then it " \
#              "will mark all of the following letters as being wrong.  Also make sure you hit enter when you're " \
#              "done typing!  P.S. not sure why the paragraph is so awkwardly spread out on the screen but I'll fix that too."
#
#     easy = input("\nIf you want a shorter paragraph to get the gist of this, type 'y' here, otherwise press enter: ")
#     if 'y' in easy:
#         phrase = "Here is an easier phrase for you to see how quickly you can type."
#
#     word_count = 1
#     for i in range(len(phrase) - 1):
#         if phrase[i] == " " and phrase[i + 1] == " ":
#             continue
#         elif phrase[i] == " ":
#             word_count += 1
#
#     print("\nYour phrase is: " + phrase + "\n")
#
#     input("Press enter when ready!")
#
#     print("begin typing in")
#     time.sleep(2)
#     counter = 3
#     while counter > 0:
#         print(counter)
#         counter -= 1
#         time.sleep(1)
#     print("GO")
#     print(phrase)
#     start_time = time.time()
#     typed = input("")
#     end_time = time.time()
#
#     char_count = 0
#     for char in phrase:
#         char_count += 1
#
#     error_count = 0
#     for i in range(len(typed)):
#         if i <= len(phrase) - 1 and phrase[i] != typed[i]:
#             error_count += 1
#         if i > len(phrase) - 1:
#             error_count += 1
#     if len(typed) < len(phrase):
#         error_count += (len(phrase) - len(typed))
#
#
#     accuracy = int(((char_count - error_count) / char_count) * 100)
#
#     words_per = (word_count * 60) / (end_time - start_time)
#     print(f"\nWMP: {int(words_per)}")
#     print(f"Accuracy: {accuracy}%\n")

# import time
# import random
#
# phrase = "Here is your test phrase.  Type as fast as you can."
# phrase_list = phrase.split(" ")
# word_count = 0
# for word in phrase_list:
#     if word == "":
#         continue
#     word_count += 1
# print(word_count)

GUEST_LIST = {
    "Randy": "Germany",
    "Karla": "France",
    "Wendy": "Japan",
    "Norman": "England",
    "Sam": "Argentina"
}

# def censor_string(txt, lst, char):
#     txt = txt.split(" ")
#     count = 0
#     for i in range(len(txt)):
#         if txt[i] in lst:
#             for j in txt[i]:
#                   count += 1
#             txt[i] = char * count
#     txt = " ".join(txt)
#     return txt
#
#
# print(censor_string("My name is brandon.", ['name'], '*'))



def consecutive_combo(lst1, lst2):
    if lst1 == sorted(lst1 + lst2):
        return True
    else:
        return False
print(consecutive_combo([1, 4, 5, 7], [2, 3, 6]))