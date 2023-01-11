# There are 3 types of numbers : int, float and complex
x = 1    # int, whole numbers 
y = 2.8  # float, decimal numbers
z = 1j   # complex

# int - can be any whole number
x = 154
y = -451    
z = 0

print(x,y,z)

# float - any decimal number
x = 1.25    
y = -52.3456

print(x,y)

# float can also be scientific numbers with an "e" to indicate the power of 10.
numb1 = 3.565e10
numb2 = -45.1e5

print(numb1,numb2)

# complex numbers, the symbol j is used to denote the imaginary unit
x = 5j
y = -2j
z = 4 + 1j

print(x,y,z)

# You can convert from one type to another 
m = 16
n = 20.23
k = 11j

# convert from int to float
a = float(m)
print(a,type(a))

# convert from float to int
b = int(n)
print(n,type(n))

# convert from int to complex
c = complex(x)
print(c,type(c)) 

# random numbers
# first we need to import rundom number library to the code
import random

rand_number1 = random.randint(1,100) # random number from 1 to 100 range

print(rand_number1)