fruit = {"orange": "I drink everyday",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small sweet fruit",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favorite",
       "sprouts": "mmmm, lovely",
       "spinach": "can I have some more fruit, please?"}

# print(veg)
#
# veg.update(fruit) #adds all fruit dictionary to veg
# print(veg)

# fruit.update(veg)
# print(fruit)

# print(fruit.update(veg))
# print(fruit)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)

print(veg)
print(fruit)