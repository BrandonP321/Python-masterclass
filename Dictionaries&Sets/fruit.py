fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit"}

veg = {"cabbage": "every child's favorite",
       "sprouts": "mmmm, lovely",
       "spinach": "can I have some more fruit, please"}

print(veg)
veg.update(fruit)
print(veg)
print(veg.update(fruit))
print(fruit)