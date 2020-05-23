# farm_animals = {"sheep", "cow", "hen", "pig"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# wild_animals = set(["lion", "tiger", "bear"])
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)
#
# empty_set = set()
# empty_set2 = {}
# empty_set.add("a")
# empty_set2.add("a")
# print(empty_set)
# print(empty_set2)
even = set(range(0, 40, 2))
print(even)
print(len(even))

squares_tuple = 4, 6, 9, 16, 25
squares = set(squares_tuple)
print(squares)
print(len(squares))

print(even.union(squares))
print(even & squares)

even.difference_update(squares)
print(even)


even = set(range(0, 40, 2))
squares = {4, 6, 16}

if squares.issubset(even):
    print("Squares is a subset of even")
if even.issuperset(squares):
    print("Even is a superset of squares")
