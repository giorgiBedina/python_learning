# SORT list
# Sort List Alphanumerically
# Alphabetically
football_clubs = ["Manchester City", "PSG", "Real Madrid", "Chelsea", "Barcelona", "Arsenal", "Napoli"]
football_clubs.sort() # this will sort clubs alphabetically
print(football_clubs)

# Numerically
numbers = [5,78,2,69,420,45,16,27,77]
numbers.sort() # this will sort clubs numerically
print(numbers)

# To sort descending, use the keyword argument reverse = True
football_clubs.sort(reverse = True) # this will sort clubs alphabetically descending
print(football_clubs)

numbers.sort(reverse = True) # this will sort clubs numerically descending
print(numbers)

# You can also customize your own function by using the keyword argument key = function
def myfunc(n):
    return abs(n - 30) # this will return absolute number from number minus 30
numbers.sort(key = myfunc) # The function will return a number that will be used to sort 
#                            the list (the lowest number first)
print(numbers) 

# By default the sort() method is case sensitive, resulting in all 
# capital letters being sorted before lower case letters
pets = ["Sushi","margo","snoopy","Quackity","Loma"]
pets.sort()
print(pets)

# Perform a case-insensitive sort of the list
pets.sort(key = str.lower)
print(pets)

# The reverse() method reverses the current sorting order of the elements
pets.reverse()
print(pets)
      
# COPY list    
list1 = ["pizza","apple","cheese","fries"]
list2 = None

# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1,
# and changes made in list1 will automatically also be made in list2
# Make a copy of a list with the copy() method
list2 = list1.copy()
print(list2)

#Another way to make a copy is to use the built-in method list()
list2.clear()
list2 = list(list1)
print(list2)

# JOIN lists
# There are several ways to join, or concatenate, two or more lists
# One of the easiest ways are by using the + operator.
join_list1 = ["one","two","three"]
join_list2 = [1,2,3]
join_list3 = join_list1 + join_list2
print(join_list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one
for x in join_list2:
    join_list1.append(x)
print(join_list1)

# Or you can use the extend() method, which purpose is to add elements from one list to another list
join_list1 = ["one","two","three"]
join_list2 = [1,2,3]
join_list1.extend(join_list2)
print(join_list1)   

# LIST METHODS 
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list