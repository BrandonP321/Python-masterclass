# empty_list = []
#
# for i in range(1, 7):
#     for j in range(1, 7):
#         empty_list.append(i + j)
# print(sorted(empty_list))
# list_total = len(empty_list)
# print(f"Total possible outcomes: {list_total}")
#
# for k in range(2, 13):
#     print(f"{k:2}: {empty_list.count(k)}; {(empty_list.count(k))/(list_total):.3}")


# Factorial Test

# number = int(input("Please Enter a number: "))
# char_counter = 0
# factorial = 1
#
# for i in range(1, number + 1):
#     factorial = factorial * i
# for char in str(factorial):
#     char_counter += 1
#
#
# print(f"{number}! = {factorial}")
# print(f"There are {char_counter} digits in {number}")

import math

n = int(input("Please enter a number: "))
print()
char_count = 0
factorial = math.factorial(n)
print(f"The factorial of {n} is {factorial}")
for char in str(factorial):
    char_count += 1
print(f"There are {char_count} digits in {n}!")

import random
import math

# one_count = 0
# two_count = 0
# three_count = 0
# four_count = 0
# five_count = 0
# six_count = 0
#
# range_end = 100
#
# for i in range(1, range_end):
#     n = random.randint(1,2)
#     if n == 1:
#         one_count += 1
#     elif n == 2:
#         two_count += 1
#     elif n == 3:
#         three_count += 1
#     elif n == 4:
#         four_count += 1
#     elif n == 5:
#         five_count += 1
#     elif n == 6:
#         six_count += 1
#
# print(one_count/range_end)
# print(two_count/range_end)
# print(three_count/range_end)
# print(four_count/range_end)
# print(five_count/range_end)
# print(six_count/range_end)
# print(one_count + two_count + three_count + four_count + five_count + six_count)

# while True:
#     user = input("Would you like to roll the dice? ")
#     if "y" in user.casefold():
#         print(random.randint(1, 6))
#     if "n" in user.casefold():
#         print("Ok, bye!")
#     else:
#         print("Sorry, please enter yes or no")