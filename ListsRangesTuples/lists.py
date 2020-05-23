# parrot_list = ["non pinin", "no more", "a stiff"]
#
# parrot_list.append("a Norwegian Blue")
# for state in parrot_list:
#     print(f"This parrot is {state}")
#
odd = [1, 3, 5, 7]
even = [2, 4, 6, 8]
# numbers = odd + even
# numbers.sort()
# print(numbers)

numbers = [even, odd]

for number_list in numbers:
    print(number_list)
    for value in number_list:
        print(value)

print(numbers[0][2])