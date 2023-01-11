# Strings is array of characters 
# pring string 
print("this is string")
# you can print space and end-line
print("Hello\tworld") # \t prints space
print("first line\nsecond line") # \n prints endline
# in case you don't want endline
print("hey",end="")
print("there")
# modify endline
print("good",end="\t") # endline will be space
print("morning")

# you can assingn string to a variable 
str1 = "string one"
print(str1)

# multiline strings
m_string = """"Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(m_string)

# strings are arreys , therefore you can separate characters from stings
str2 = str("Earth is flat")
print(str2[0]) # this will print first character of the string

# loop in string
# because strings are arrays of chararters , you can loop in the string 
# and access each character seperatly
str3 = "kvaradona"
for x in str3: # loop string with for cicle 
    print(x,end='\t')   # and print each character
print()    
