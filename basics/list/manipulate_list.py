# Loop through list
# You can loop through the list items by using a for loop
list_OS = ["windows 10","windows 7","arch linux","debian","macOS"]
for OS in list_OS:
    print(OS, end="\t")
print()    

# You can also loop through the list items by referring to their index number
list_linux = ["manjaro","ubuntu","mint","kali","fedora"]
for i in range(len(list_linux)): # Use the range() and len() functions to create a suitable iterable
    print(list_linux[i])