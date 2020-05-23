shoppingList = ["milk", "eggs", "spam", "bread", "rice"]

for item in shoppingList:
    if item == "spam":
        continue
    print("Buy " + item)

print()

for item in shoppingList:
    if item == "spam":
        break
    print("But " + item)