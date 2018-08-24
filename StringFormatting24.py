#24 - String Formatting

#Display a string and a number in a single statement

age1 = 24
age2 = 20
#print("My age is " + age + " years") #will crash

print("My age is " + str(age1) + " years") #str transforms it into string.

print("My age is {0} years".format(age1)) #inside {} is a replacement field

print("My age is {0} and her age is {1}".format(age1, age2)) #{index} will show equivalent

#Python 2.7 examples

print("My age is %d years" % age1) #Python 2.7 formatting
print("My age is %d %s, %d %s" %(age1, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))

#Specify the precision of a number

print("Pi is approximately %12.50f" % (22 / 7)) #Python 2

print('Pi is approximately {0:12.50}'.format(22 / 7)) #Python 3

#In loops, you use different syntax.
for i in range(1, 12):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))