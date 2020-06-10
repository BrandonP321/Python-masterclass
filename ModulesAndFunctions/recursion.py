# non-recursive
def fact(n):
    result = 1
    if n > 1:
        for i in range(2, n + 1):
            result *= i
    return result


# recursive
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):  # recursive but not as fast
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fib(n):  # not recursive but faster
    if n == 0:
        result = 0
    if n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for j in range(n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result


for i in range(101):
    print(i, fib(i))
