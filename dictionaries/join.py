myList = ["a", "b", "c", "d"]

newString = ''

#print the whole myList

print(myList)

#print element from dictionary

print(myList[2])

#print all elements separated by , + space
# for c in myList:
#     newString += c + ", "
# print(newString)
#Problem: too inefficient. There's a comma at the end.
#Creates a variable


#using join method for the job
for c in myList:
    newString = ", ".join(myList)
print(newString)

#You don't even need a for loop

newString2 = ", ".join(myList)
print(newString2)

