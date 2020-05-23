# menu = []
# menu.append(["egg", "spam", "bacon"])
# menu.append(["egg", "sausage", "bacon"])
# menu.append(["egg", "spam"])
# menu.append(["egg", "bacon", "spam"])
# menu.append(["egg", "bacon", "sausage", "spam"])
# menu.append(["spam", "bacon", "sausage", "spam"])
# menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
# menu.append(["spam", "egg", "sausage", "spam"])
#
# ingredients = ""
# for meal in menu:
#     if "spam" not in meal:
#         for ingredient in meal:
#             ingredients += f"{ingredient} "
# print(f"Ingredients: {ingredients}")

grocery_list = []
first_item = input("What do you need to buy from the store? ")
if "nothing" in first_item:
    print("Maybe next time :(")
else:
    grocery_list.append(first_item)

while "nothing" not in first_item:
    new_item = input("Anything else: ")
    if new_item == "no":
        print("sounds good")
        break
    else:
        grocery_list.append(new_item)

ingredient_number = 0
if "nothing" in first_item:
    pass
else:
    print(f"Here's what you need to buy:")
    for ingredient in grocery_list:
        ingredient_number += 1
        print(str(ingredient_number) + ". " + ingredient)