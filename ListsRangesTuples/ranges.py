# for i in range(0, 10):
#     print(i)
#
# my_list = list(range(0, 10))
# print(my_list)
#
# numbers = ""
# for i in range(0, 10):
#     if i != 9:
#         numbers += f"{str(i)}, "
#     else:
#         numbers += str(i)
# print(numbers)
#
# decimals = range(0, 100)
# print(decimals)
#
# my_range = decimals[3:40:3]
# print(my_range)
#
# for i in my_range:
#     print(i)
#
# for i in range(0, 100)[3:40:3]:
#     print(i)
for i in range(0, 100, -2):
    print(i)
# won't print anything since loop believes the start is 0 and tries to move back -2 but can't
# loop below will print range since the slice is provided after the range
for i in range(0, 100)[::-2]:
    print(i)

back_string = "egaugnal lufrewop yrev a si nohtyp"
print(back_string[::-1])  # prints string in reverse
