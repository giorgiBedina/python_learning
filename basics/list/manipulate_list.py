# Loop through list
# for loop
# You can loop through the list items by using a for loop
list_OS = ["windows 10","windows 7","arch linux","debian","macOS"]
for OS in list_OS:
    print(OS, end="\t")
print()    

# You can also loop through the list items by referring to their index number
list_linux = ["manjaro","ubuntu","mint","kali","fedora"]
for i in range(len(list_linux)): # Use the range() and len() functions to create a suitable iterable
    print(list_linux[i], end="\t")
print()    
    
# while loop
# You can loop through the list items by using a while loop
# Use the len() function to determine the length of the list, then start at 0 and 
# loop your way through the list items by referring to their indexes    
car_gears = ["reverse gear","first gear","second gear","forth gear","fifth gear"]
i = 0
while i < len(car_gears):
    print(car_gears[i],end='\t')
    i = i + 1 # Remember to increase the index by 1 after each iteration
print()    

# List Comprehension
# List Comprehension offers the shortest syntax for looping through lists
phones = ["samsung s10","iphone 10","oneplus 8T","xiaomi mi10"]
for x in phones:
    print(x) #  you can use - [print(x, end=" ") for x in phones] - same code but one line  
print()

# List comprehension offers a shorter syntax when you want to create a new 
# list based on the values of an existing list

old_list = [15,60,47,28,34,9]
new_list = []

for numb in old_list:
    if numb%2 == 0: # if number is even 
        new_list.append(numb) # new list will contain numbers from old list, if they are even 
print(new_list)    
new_list.clear() # clears new_list, it will have no items 

# With list comprehension you can do all that with only one line of code
new_list = [x for x in old_list if x%2 == 0]
print(new_list)
# The Syntax : new_list = [expression for item in iterable if condition == True]
# The condition is optional and can be excluded
new_list.clear() # clear new_list
new_list = [x for x in old_list] # this will copy to old_list to new list
# The iterable can be any iterable object, like a list, tuple, set etc
# You can use the range() function to create an iterable
new_list.clear()
new_list = [x for x in range(7)] # this will insert numbers from 0 to 7(not included)
print(new_list)
# Same example, but with a condition
new_list.clear()
new_list = [x for x in range(100) if x%5 == 0] # this will inserts numbers which can be devided by 5
print(new_list)

# The expression is the current item in the iteration, but it is also the outcome, 
# which you can manipulate before it ends up like a list item in the new list
new_list.clear()
char_list = ['a','b','c','d']
new_list = [x.upper() for x in char_list] # will copy upper chars from old to new list
print(new_list)

# You can set the outcome to whatever you like
windows_list = ["windows xp","windows 7","windows 8","windows 10"]
windows_error = ["error" for x in windows_list] # Set all values in the new list to 'error'
print(windows_error)

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_fruits = [x if x != "banana" else "orange" for x in fruits] # this will change banana with orange 
# x if x != "banana" else "orange" - expression 
# for x in fruits for item in iterable 
print(new_fruits)