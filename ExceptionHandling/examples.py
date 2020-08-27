# x = 8 = 5  # results in an error obviously
# y = x / 0  # 0 division error


def factorial(n):
    # n! can also be defined as n * (n - 1)

    if n == 1:
        return 1
    return n * factorial(n - 1)


try:
    print(factorial(1000))
except RecursionError:
    print("This program can't calculate factorials that large")
except ZeroDivisionError:
    print("You can't divide by zero")

try:
    print(factorial(1000))
except (RecursionError, ZeroDivisionError):
    print("This program can't calculate factorials that large")
