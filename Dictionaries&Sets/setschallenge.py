text = input("Enter your text here: ").casefold()
# final_text = set(text)
#
# for char in text:
#     if char in "aeiou" or not char.isalpha():
#         final_text.discard(char)
#
# print(sorted(final_text))

vowels = frozenset("aeiou")
final_set = set(text).difference(vowels)
print(sorted(final_set))