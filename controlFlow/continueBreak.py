#31

# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
#
# for item in shopping_list:
#     if item == 'spam':
#         #print("I am ignoring " + item) # to see what's going on
#         continue #stops processing code
#     print("Buy " + item)

meal = ["egg", "bacon", "spam", "sausages"]

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break

if nasty_food_item:
    print("Can't I have anything without spam in it")
