my_list = [0, 1, 2, 3, 4, 5, 6]
my_iterator = iter(my_list)

for char in range(len(my_list)):
    print(next(my_iterator))