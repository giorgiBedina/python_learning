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

# ACCESS ITEMS
# List items are indexed and you can access them by referring to the index number
this_list = [45,56,89,41]
print(this_list[0]) # this will print the first item of the list

# Negative indexes
# Negative indexing means start from the end
print(this_list[-1]) # this will print the last item of the list

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items
list_car = ["toyota","nissan","mazda","honda","mitsubishi"] 
print(list_car[1:3]) # The search will start at index 1 (included) and end at index 3 (not included).

# By leaving out the start value, the range will start at the first item
fruit_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruit_list[:4]) # this will print from the start to index 4 (not included)

# By leaving out the end value, the range will go on to the end of the list
print(fruit_list[2:]) # this will print from index 2(included) to the end

# Specify negative indexes if you want to start the search from the end of the list:
print(fruit_list[-3:-1]) # this will print from 3rd item from the end to the end (last item not included)

# check if item exists in the list
if "banana" in fruit_list:
    print(True)