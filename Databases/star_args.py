# from __future__ import print_function
# allows the following print() to work if using python 2
# print("Hello", "planet", "earth")


def average(*args: int) -> float:
    print(type(args))
    print("args is {}".format(args))  # (3, 4, 5, 1)
    print(*args)  # 3 4 5 1
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


def print_tuple(*args) -> tuple:
    return args


def average_length(*args: str) -> float:
    mean = 0
    for arg in args:
        mean += len(arg)
    return mean / len(args)


def largest(*args: int) -> int:
    sorted_tuple = sorted(args)
    return sorted_tuple[-1]


def reverse(*args: str) -> tuple:
    return args[::-1]


print(average(3, 4, 5, 1))
print(print_tuple("hi", "there", 'friend'))
print(average_length("hi", 'there', 'friend'))
print(largest(3, 6, 1, 39, 839, 929, 3, 0))
print(reverse("Hi", 'there', 'friend'))

words = ["Hi", "there", "friend"]
print(words)
print(*words)

numbers = [1, 3, 4, 2, 3]
print(numbers)
print(*numbers)
