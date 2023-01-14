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

# ACCESS items
# You can access tuple items by referring to the index number, inside square brackets
print(mix_tuple[1])

# Negative indexing means start from the end
fruit_tuple = ("apple","melon","pear","banana")
print(fruit_tuple[-2])

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items
print(fruit_tuple[1:3]) # from index 1(included) to index 3(not included)

# By leaving out the start value, the range will start at the first item
number_tuple = (1,2,2,3,4,5,3,6)
print(number_tuple[:5]) # from start to index 5(not included)

# By leaving out the end value, the range will go on to the end of the list
print(number_tuple[2:]) # will print from index 2(included) to the end

# Specify negative indexes if you want to start the search from the end of the tuple
print(number_tuple[-5:-2])

# Print each item with loop
[print(x,end=" ") for x in number_tuple]
print()