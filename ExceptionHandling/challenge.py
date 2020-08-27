import sys


def getint():
    while True:
        try:
            x = input("First number: ")
            y = input("Second number: ")
            return int(x) / int(y)
        except ZeroDivisionError:
            print("Can't divide by zero\n")
        except TypeError:
            print("Enter integers only\n")
        except EOFError:
            sys.exit(0)  # exits the program with exit code 0
        finally:
            print("The 'finally' clause will always be executed")


print(getint())

try:
    print(int(input("Enter something: ")))
except ValueError:
    print('ValueError')
else:
    print('else')
finally:
    print('finally')
