# Booleans represent one of two values: True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean answer
print(9 > 11)
print(9 == 11)
print(9 < 11)

# When you run a condition in an if statement, Python returns True or False
HP_supra = 320
HP_nsx = 290

if HP_supra > HP_nsx:
    print("Supra is faster than NSX")
else:
    print("NSX is faster than Supra")   

# The bool() function allows you to evaluate any value, and give you True or False in return
# For example , let's evaluate number and string
print(bool(16))
print(bool("morning")) 

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones    

bool(False) # False will return false
bool(None) # Nonse will return false
bool(0) # 0 will return false
bool("") # Empty string will return false
bool(()) # Returns false
bool([]) # Returns false
bool({}) # Returns false

# You can create functions that returns a Boolean Value
def myFunction() :
  return True

print(myFunction())