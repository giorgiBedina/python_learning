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


# ADD item to the list
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index
GPUs = ["3060","3060 ti","3070 ti","3080"]
GPUs.insert(2,"3070") # This will insert new item to index 2 and move rest to right
print(GPUs)

# To add an item to the end of the list, use the append() method
GPUs.append("3080 ti") # This will add item to the last index
print(GPUs)

# To append elements from another list to the current list, use the extend() method

german_cars = ["bmw","mercedes-benz","vw","audi","porsche"]
italian_cars = ["ferrai","lamborgini","lancia","alfa romeo"]
euro_cars = ["volvo","saab","mini cooper"]
euro_cars.extend(german_cars) # This will add items from german_cars to euro_cars
print(euro_cars)
euro_cars.extend(italian_cars) # This will add items from italian_cars to euro_cars
print(euro_cars)

# Remove item from the list
# The remove() method removes the specified item
engines = ["2jzGTE","k20a2","LS1","RB26DETT", "13B"]
print(engines)
engines.remove("LS1")
print(engines)

# The pop() method removes the specified index
engines.pop(2) # This will remove the item with the index 2
print(engines)

# If you do not specify the index, the pop() method removes the last item
engines.pop() # This will remove the last item from the list
print(engines)

# The del keyword also removes the specified index:
engines = ["2jzGTE","k20a2","LS1","RB26DETT", "13B"]
del engines[0]
print(engines)

# The del keyword can also delete the list completely
del engines # This will remove list entirely, engines list won't be defined any longer

# The clear() method empties the list.
# The list still remains, but it has no content.
engines = ["2jzGTE","k20a2","LS1","RB26DETT", "13B"]
engines.clear() # This will remove items , but the list itself still exists
print(engines) # This will print empty list