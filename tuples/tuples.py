#Tuple is an ordered set of data
#Immutable objects
t = "a", "b", "c"
print(t)

print(("a", "b", "c"))

#Both prints are tuples

welcome = "Welcome", "Alice", 1975
bad = "Bad Company" "Bad Company", 1974

print(welcome)
print(welcome[1])

welcome = welcome[0], "Bruno", 1996
print(welcome)

#if you do the following line on bad tuple, it will return an error
#because there are two values inside it, not three

title, artist, year = welcome
print(title)
print(artist)
print(year)

newTuple = "More tuppling", ((1, "pull over"), (2, "right now!"))

print(newTuple)

