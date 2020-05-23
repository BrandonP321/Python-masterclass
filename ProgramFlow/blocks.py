name = input('Please enter your name: ')
age = int(input('How old are you {}? '.format(name)))

print()

# if age >= 18:
#     print("That's what's up dawg, you can vote!")
# elif 18-age == 1:
#     print("Why so young dawg?  Come on back in {} year to vote.".format(18-age))
# elif age >= 100:
#     print("Sorry bud, but you're definitely dead")
# else:
#     print("Why so young dawg?  Come on back in {} years to vote.".format(18-age))

if age >= 100:
    print("Sorry bud, but you are definitely dead by now!")
elif 18-age == 1:
    print("Why so young dawg?  Come on back in {} year to vote.".format(18-age))
elif age >= 18:
    print("That's what's up dawg, you can vote!")
else:
    print("Why so young dawg?  Come on back in {} years to vote.".format(18-age))