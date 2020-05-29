def fullName(first, last):
    greeting = f"Hello there {first}, {last}"
    return greeting

print(fullName('Brandon', 'phillips'))

with open('centered.txt', 'w') as centered_file:
    print("Let's see if this will write to a text file", file=centered_file)