#Lesson 30

# for i in range(1, 20):
#     print("i is now {}".format(i))
#
# number = "9,223,724,443,234,221,436"
#
# #What's going to happen here?
# for i in range(0, len(number)):
#     print(number[i])

# number = "9,223,724,443,234,221,436"
# cleanedNumber = ''
#
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber = cleanedNumber + number[i]
#
# newNumber = int(cleanedNumber)
# print("The number is {}".format(newNumber))

#30

number = "9,223,724,443,234,221,436"
cleanedNumber = ''

for char in number:
    #Extract character from the string
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ["not pinin", "no more", "a stiff", "bereft of lift"]:
    print("This parrot is " + state)

#Worth paying  close attention
for i in range(0, 100, 5):
    print("i is {} ".format(i))

#Pay close attention
for i in range(1, 13):
    for j in range(1, 13):
        print("{1} times {0} is {2}".format(i, j, i*j))
    print("===============")