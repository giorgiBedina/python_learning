# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called

# But there are some workarounds
# You can convert the tuple into a list, change the list, and convert the list back into a tuple

my_tuple = ("mustang", "camaro", "corvete")
my_list = list(my_tuple)
my_list[1] = "charger"
my_tuple = tuple(my_list)

print(my_tuple)

# ADD items
# Since tuples are immutable, they do not have a build-in append() method, 
# but there are other ways to add items to a tuple

# Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, 
# add your item(s), and convert it back into a tuple.
my_tuple = ("mustang", "camaro", "corvete")
my_list = list(my_tuple)
my_list.append("chellenger")
my_tuple = tuple(my_list)

print(my_tuple)

# Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many),
# create a new tuple with the item(s), and add it to the existing tuple:
tuple_a = (2,4,6,8)
tuple_b = (10,12,14,16)
tuple_c = tuple_a + tuple_b
print(tuple_c)

# Tuples are unchangeable, so you cannot remove items from it,
# but you can use the same workaround as we used for changing and adding tuple items
this_tuple = ("pewdiepie","mr beast","ksi","t-series")
this_list = list(this_tuple)
this_list.pop(2)
this_tuple = tuple(this_list)

print(this_tuple)

# Or use clear() method
this_tuple = ("pewdiepie","mr beast","ksi","t-series")
this_list = list(this_tuple)
this_list.clear()
this_tuple = tuple(this_list)

print(this_tuple)

# The del keyword can delete the tuple completely
del this_tuple

# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple
car_tuple = ("Civic Type R","AMG GTR","GTR Nissmo","GR Supara","M3")

#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"
(honda,mercedes,nissan,toyota,bmw) = car_tuple

print("honda ",honda)
print("mercedes ",mercedes)
print("nissan ",nissan)
print("toyota ",toyota)
print("bmw ", bmw)

# If the number of variables is less than the number of values,
# you can add an * to the variable name and the values will be assigned to the variable as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# If the asterisk is added to another variable name than the last, Python will assign values to
# the variable until the number of values left matches the number of variables left
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# You can loop through the tuple items by using a for loop
car_tuple = ("Civic Type R","AMG GTR","GTR Nissmo","GR Supara","M3")
for car in car_tuple:
    print(car, end=" ")
print()

# You can also loop through the tuple items by referring to their index number
# Use the range() and len() functions to create a suitable iterable
for i in range(len(car_tuple)):
    print(car_tuple[i])
    
# You can loop through the tuple items by using a while loop
# Use the len() function to determine the length of the tuple,
# then start at 0 and loop your way through the tuple items by referring to their indexes.    
this_tuple = ("pewdiepie","mr beast","ksi","t-series")
i = int(0)
while i < len(this_tuple):
    print(this_tuple[i])
    i = i + 1 # Remember to increase the index by 1 after each iteration

# Join Two Tuples
# To join two or more tuples you can use the + operator
german_cars = ("bmw","mercedes","porsche","VW","audi")
JDM_cars = ("honda","toyota","subaru","mitsubishi")
cars = german_cars + JDM_cars
print(cars)   

# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator
print(JDM_cars * 2)

# Methods
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found