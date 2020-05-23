empty_dict = {}

# while True:
#     new_key = input("What word are you looking for? ")
#     if new_key == "quit":
#         print(empty_dict)
#         print("Cya")
#         break
#     if new_key in empty_dict:
#         print(f"Definition: {empty_dict[new_key]}")
#         print()
#     else:
#         yes_no = input(f"Would you like to add {new_key} to the dictionary? ")
#         if "y" in yes_no:
#             empty_dict[new_key] = input(f"Enter the description for {new_key} ")
#             print(empty_dict)
#             print()
#         else:
#             print()

# while True:
#     new_key = input("What word are you looking for? ")
#     description = empty_dict.get(new_key, input(f"Would you like to add {new_key} to the dictionary? "))
#     if description == "quit":
#         print(empty_dict)
#         print("Bye")
#         break
#     if description not in empty_dict and "y" in description:
#         empty_dict[new_key] = input(f"Enter the description for {new_key}: ")
#         print(empty_dict)
#         print()

while True:
    new_key = input("What word are you looking for? ")
    if new_key == "quit":
        print(empty_dict)
        print("Bye")
        break
    if new_key not in empty_dict:
        yes_no = input(f"Would you like to add {new_key} to the dictionary?")
        if "y" in yes_no:
            empty_dict[new_key] = input(f"Enter the description for {new_key}: ")
    if new_key in empty_dict:
        print(empty_dict[new_key] + '\n')
    else:
        print(f"{empty_dict} \n")
