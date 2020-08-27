def binary_search(x, find_list):
    list_len = len(find_list)
    low = find_list[0]
    high = find_list[list_len - 1]

    while True:
        guess = low + (high - low) // 2

        if x == find_list[guess]:
            print("found it")
            break
        if x > find_list[guess]:
            low = guess
        if x < find_list[guess]:
            high = guess


empty_list = []
for i in range(10000001):
    empty_list.append(i)

sortedList = sorted(empty_list)

print(sortedList)

# number to find is 767
input("Press enter to continue")

find = 1000000

if find in sortedList:
    print("We found it")

input("press enter to continue")

for j in sortedList:
    if j == find:
        print("found it again")
        break

input("Press enter to continue")

binary_search(find, sortedList)

