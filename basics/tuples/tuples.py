# Tuples are used to store multiple items in a single variable
# A tuple is a collection which is ordered and unchangeable
# Tuples are written with round brackets
fruit_tuple = ("apple","melon","pear","banana")

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc
fruit_tuple = ("apple","melon","pear","banana") # apple is index 0, banana is index 3
[print(x, end=" ") for x in fruit_tuple]
print()
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created
# Since tuples are indexed, they can have items with the same value
number_tuple = (1,2,2,3,4,5,3,6)
print(number_tuple)

# To determine how many items a tuple has, use the len() function
print(len(number_tuple))

# To create a tuple with only one item, you have to add a comma after the item,
# otherwise Python will not recognize it as a tuple
football_GOAT = ("MESSI",)
print(type(football_GOAT))

football_GOALS = ("Ronaldo") # not tuple
print(type(football_GOALS))

# Tuple items can be of any data type
int_tuple = (1,2,3,4,5,6)
float_tuple = (1.1,1.3,1.5,1.7)
string_tuple = ("this","is","string","tuple")
boolean_tuple = (True,False,False)

# A tuple can contain different data types
mix_tuple = ("civic",1.6,160,True)
print(type(mix_tuple))