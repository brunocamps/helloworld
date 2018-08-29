# iterator: object that represents a stream of data
# returns one element at the time

#Strings and lists are iterators

string = "1234567890"

#iterator created from the string. FOR uses that iterator.
# for char in string:
#     print(char)

# my_iterator = iter(string)
# print(my_iterator) #prints memory allocation of iterator
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# #print(next(my_iterator))


#implicitly creating an iterator from the srting
for char in string:
    print(char)

#explicitly shows iterator
for char in iter(string):
    print(char)

#Create a list of items, then create an iterator using the iter() function
#Use a loop to loop "n" times, where n is the number of items in your list
#Each time round the loop, use next() on your list to print the next item

#hint: use the len() function rather than counting the number manually

my_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

my_iterator = iter(my_list)

for i in range(0, len(my_list)):
    next_item = next(my_iterator)
    print(next_item)

print("--------------------")
for i in my_list:
    print(i)