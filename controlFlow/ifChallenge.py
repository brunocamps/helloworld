""""
#Write a small program to ask for a name and an age
#When both values have been entered, check if the person
#is the right age to go on an 18-30 holiday
#If they are, welcome them to the holiday, otherwise print
#a polite message refusing their entry
"""

print("What's your name? ")
name = input()
print("And what's your age, {0}?".format(name))
age = int(input())

if 18 <= age <= 30:
    print("Welcome to the holiday!")
else:
    print("Not on holiday this time!")
