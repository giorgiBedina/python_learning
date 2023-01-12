# You can change item values in list
games = ["Elden ring","Smite","Sea of thieves","BeamNG","Asseto corsa"]
games[1] = "Naruto storm" # This will change index 1 item Smite with Naruto storm
print(games) # This will print changed items

# To change the value of items within a specific range, define a list with the new values, 
# and refer to the range of index numbers where you want to insert the new values
processors = ["celeron","pentium","core i3", "core i5","core i7","core i9"]
processors[2:5] = ["ryzen 3","ryzen 5","ryzen 7"] # This will change list from index 2(included) to 5(not uncluded)
print(processors)

# If you insert more items than you replace, the new items will be inserted where you specified, 
#  and the remaining items will move accordingly
processors = ["celeron","pentium","core i3", "core i5","core i7","core i9"]
processors[2:4] = ["ryzen 3","ryzen 5","ryzen 7"] # This will change list from index 2(included) to 
print(processors) # 4(not uncluded), and add new item to index 4 and move rest to the right

# If you insert less items than you replace, the new items will be inserted where you specified, 
# and the remaining items will move accordingly
processors = ["celeron","pentium","core i3", "core i5","core i7","core i9"]
processors[0:2] = ["athlon"] # This will change list item with index 0 remove item 
print(processors) # with index 1(included),2(not included) and move rest to the left


