# Lists are used to store multiple items in a single variable.
footballers = ["messi","mbappe","neymar"]
print(footballers)

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
print(footballers[0]) # This will print the first item on the list , which is messi

# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# Since lists are indexed, lists can have items with the same value
fruits = {"apple","banana","cherry","banana"}

# To determine how many items a list has, use the "len()"" function
print(len(fruits))

# List items can be of any data type
numbers = [1,2,3,4]
colors = ["greed","red","purple"]
objective = [True,False,True]

# list can contain different data types
# Example : a list with strings, integers and boolean value
mylist = [1,"abc",False,2,"def",True]

# From Python's perspective, lists are defined as objects with the data type 'list'
print(type(mylist))