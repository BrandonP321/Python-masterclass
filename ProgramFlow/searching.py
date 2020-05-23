shoppingList = ["milk", "eggs", "spam", "bread", "rice"]

item_to_find = input('What item are you looking for? ')
found_at = None

for index in range (len(shoppingList)):
    if shoppingList[index] == item_to_find:
        found_at = index
        break
if found_at == None:
    print(f"item, {item_to_find}, not found")
else:
    print(f"item found at position {found_at}")