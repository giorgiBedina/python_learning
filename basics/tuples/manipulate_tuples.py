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