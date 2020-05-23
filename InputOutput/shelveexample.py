# import shelve
#
# with shelve.open('shelvedFruit') as fruit:
#     fruit['apple'] = "A red, round fruit"
#     fruit['orange'] = "An orange citrus fruit"
#     fruit['pear'] = "An odd shaped apple"
#     print(fruit['pear'])
#
# print(fruit)

# import shelve
#
# fruit = shelve.open('shelvedFruit')
#
#
# fruit['apple'] = "A red, round fruit"
# fruit['orange'] = "An orange citrus fruit"
# fruit['pear'] = "An odd shaped apple"
# print(fruit['pear'])
#
# print(fruit)
# fruit.close()

import shelve

with shelve.open('carsShelve') as cars:
    cars['make'] = "ford"
    cars['model'] = 'taurus'
    cars['year'] = '2007'
    print(f"I drive a {cars['year']} {cars['make']} {cars['model']} ")