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