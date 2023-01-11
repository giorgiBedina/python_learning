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

# To check if one string contains the second string, we can use "in"
txt = "subscibe to giorgi_bedina"
print("giorgi_bedina" in txt) #this will print true/false if depending on if piewdiepie is in the txt
# or you can use if statement 
# you check check if sting not contains word/character with "not in" 
if "like and subscribe" not in txt: #this will print true/false if depending on if given sentence is in the txt 
    print("like and subscribe to giorgi_bedina")


# loop in string
# because strings are arrays of chararters , you can loop in the string 
# and access each character seperatly
str3 = "kvaradona"
for x in str3: # loop string with for cicle 
    print(x,end='\t')   # and print each character
print()    


# String lenght
# string as ant array has size, lenght
str4 = "Is math related to science?"
print(len(str4))