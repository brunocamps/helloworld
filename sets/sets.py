#Like dictionaries:
#Data is unorderes and found by keys
#Order varies a lot

#Curly braces {} same way you define a dictionary

# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# #for to print them separately
# for animal in farm_animals:
#     print(animal)
#
# print("=" * 40)
#
# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

# empty_set = set()
# empty_set2 = {}
# empty_set.add("a")
# empty_set2.add("a") #will fail

# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)

#Union: function of sets

even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = (4, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

print("even minus squares")
print(sorted(even.difference(squares))
print(sorted(even - squares))

print("squares minus even")
print(squares.difference(even))
print(squares - even)


# squares_tuple = (4, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))

# print(even.union(squares))
# print(len(even.union(squares)))
#
# print(squares.union(even))
#
# print("-" * 40)
# print(even.intersection(squares))
# print(even & squares)
#
# print(squares.intersection(even))
# print(squares & even)

