#Lesson 28

# age = int(input("How old are you? "))
#
# #if (age>= 16) and (age <= 65):
# # if 16 <= age <= 65:
# #     print("Have a good day at6 work!")
#
# if (age < 16) or (age > 65):
#     print("Enjoy your free time!")
# else:
#     print("Enjoy your day at work!")
#
# # if (some_condition) or (some_weird_function()):
# #     #Do something
#
# #No

x = "false"

# if x:
#     print("x is true")


# #9:34
# print("""False: {0}
# None: {1}
# 0: {2}
# 0.0: {3}
# empty list []: {4}
# empty tuple (): {5}
# empty string '': {6}
# empty string "": {7}
# empty mapping {{}}: {8}
# """.format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))

# x = input("Please enter some text: ")
#
# if x:
#     print("You entered '{}'".format(x))
# else:
#     print("You did not enter anything!")


# print(not False)
# print(not True)

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter not in parrot:
    print("I don't need that letter")
else:
    print("Give me an {}, Bob".format((letter)))