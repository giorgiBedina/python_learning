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
new_list = [x for x in old_list if "a" in x]
print(new_list)
# The Syntax : new_list = [expression for item in iterable if condition == True]
