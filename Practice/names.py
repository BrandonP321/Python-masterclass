def accum(s):
    # your code
    empty_list = []
    for i in range(len(s)):
        letters = (s[i] * (i + 1))
        letters = letters.capitalize()
        empty_list.append(letters)
    return "-".join(empty_list)


print(accum('aBcde'))