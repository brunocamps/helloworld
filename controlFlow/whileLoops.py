# Two ways of doing loops: for loops and while loops

# for i in range(10):
#     print("i is now {}".format(i))

# i=0 #declare a control variable right now (different than for loop)
# while i < 10:
#     print("i is now {}".format(i))
#     i+=1

# available_exits = ["east", "north east", "south"]
#
# chosen_exit = ""
#
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game over")
#         break
# else:
#     print("Aren't you glad you got our of there!")

import random

highest = 10
answer = random.randint(1, highest)
print(answer)

print("Please guess a number between 1 and {}".format(highest))
guess = 0 #pre initialize variable. Outside of the valid range
while guess != answer:
    guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else: #guess must be greater than number
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")

