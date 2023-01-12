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

# String modifications
# cut/slice strings
# you can return a range of characters by using the slice syntax.
string1 = "we are going to slice this string"

# specify the start index and the end index, separated by a colon, to return a part of the string.
print(string1[16:21]) # Get the characters from position 16 to position 21(not included)

# slice from the start
print(string1[:6]) # this is going to print characters from start index 0 to index 6(not included)

# slice to the end
print(string1[7:]) # this is going to print characters from start index 7 to the end

# you can use negative indexes to start the slice from the end of the string
string2 = "sushi<3!"
print(string2[-4:-1])

# combine strings with +
a, b = "this is", "amazing"
c = a + " " + b
print(c)

# format strings 
# we can not combine string and numbers together
horspower = 160
# enigne_spec = "b16a2 hp = " + horspower  - this is not possible
# to solve the issue , we can use "format()" method
enigne_spec = "b16a2 hp = {} hp"
print(enigne_spec.format(horspower))

# with "format()" method, you can use multiple numbers of arguments, 
# and place into their respective placeholders
day = 16
month = 11
year = 1999
birthday = "I was born in {}/{}/{}"
print(birthday.format(day,month,year))

# you can use index numbers {0} to be sure arguments are placed in correct placeholders
e_hp = 100
cost = 10
hp = 1000
stmt = """F1 car makes more than {2} hp, from which {0} hp is made by hybrid electric engine. 
This is why F1 engine costs around {1} million dollars."""
print(stmt.format(e_hp,cost,hp))                