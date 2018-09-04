#You can't find an element from a dictionary through an index
#you can only find it through its key
#It's a key-value relationship

fruit = {"orange": "I drink everyday",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small sweet fruit",
         "lime": "a sour, green citrus fruit"}

# print(fruit)
# print(fruit["lemon"]) #you can't search though an index, but by its key
# #Reminds of a key-value
#
# fruit["pear"] = "an odd shapped apple"
# print(fruit)


#This updates the key's value.
fruit["pear"] = "great with tequila"
print(fruit)


#Delete an element
# del fruit["lemon"]
# print(fruit)


#Delete everything
# fruit.clear()
# print(fruit)

# print(fruit["tomato"]) #will return an error, because there's no such key
#
# print(fruit)

#while True won't return an error if the key doesn't exist

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key)
#     print(description)

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We don't have a " + dict_key)


# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     fruit.has_key(dict_key)
#
#     print(description)
    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print("We don't have a " + dict_key)
#
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

#DISPLAY an ordered list of keys + value
#KEYS are ordered ALPHABETICALLY


# for snack in fruit:
#     print(fruit[snack])
#
# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print('-' * 40)

#SORT // SORTED are responsible for keys being in order

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])


# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])

#for values, not keys

# for val in fruit.values():
#     print(val)

# for key in fruit:
#     print(fruit[key])
#
# print(fruit.keys())
#
# print(fruit.values())

print(fruit)
print(fruit.items())

f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))

