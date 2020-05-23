fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "pear": "change me"}
         # "apple": "The second one"}   # reassigns the value of first 'apple' instead of printing a second 'apple' value
# # print(fruit)
# # print(fruit["lemon"])   # prints value of key 'lemon'
# # fruit["pear"] = "an odd shaped apple"   # adds 'pear' to the dictionary
# # print(fruit)
# # fruit.clear()
# # fruit["pear"] = "an odd shaped apple"
# # print(fruit)
# while True:
#     dict_key = input("Please enter a fruit: ")
#     description = fruit.get(dict_key.casefold(), f"We don't have a(n) {dict_key}")
#     if dict_key == "quit":
#         print('bye')
#         break
#     print(description)
#     # if dict_key in fruit:
#     #     print(description)
#     # else:
#     #     if dict_key[0].casefold() in "aeiou":
#     #         print(f"We don't have  an {dict_key}")
#     #     else:
#     #         print(f"We don't have a {dict_key}")
#
# for snack in fruit:
#     print(fruit[snack])    # older python versions printed 'snack' in random orders, prints in order now
print(fruit)
print(fruit.items())
print(tuple(fruit.items()))