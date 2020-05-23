# jabber = open("original.txt", "r")
#
# for line in jabber:
#     print(line)
#
# jabber.close()

# with open("original.txt", "r") as text:
#     for line in text:
#         if "jabberwock" in line.lower():
#             print(line, end="")

# with open("original.txt", "r") as text:
#     lines = text.readlines()
# print(lines)
# for line in lines:
#     print(line, end="")

# with open("original.txt", "r") as text:
#     for line in text:
#         print(text.readline(), end="")

with open("original.txt", "r") as text:
    final_text = text.read()
print(final_text)