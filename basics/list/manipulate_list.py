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
    print(list_linux[i])
    
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