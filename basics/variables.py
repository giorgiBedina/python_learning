# Viriable types int, float, boolean, string
# int - whole numbers 
# float - decimal numbers
# boolean - true/false
# string - character or array of characters

var_int = 5
var_float = 4.20
var_bool = True
var_string = "This is string"

# Print defined variables

print(var_int,var_float,var_bool,var_string)

# Checking what types are given variables
print(type(var_int),type(var_float),type(var_bool),type(var_string))

# isinstance() function checks data type

if isinstance(var_int,int):
    print("var_int is whole number(int)")

if isinstance(var_float,int):
    print("var_float is whole number(int)")  
else:
    print("var_float is not whole number(int)")  
    
# Specify types of variables when defining 
x = int(3) # x is going to be int 3 , whole number
y = str(3) # y is going to be string 3 , sentence 
z = float(3) # x is going to be float 3.0 , float number

# get the types of variables
print(type(x),type(y),type(z))

# Variables are case sensitive
n = 6
N = 9

# n and N are different variables, N will not owerwrite n
print(n,N)

# Variable can change types
var_change = 5
print(var_change,type(var_change))
var_change = 3.10
print(var_change,type(var_change))
var_change = 'name'
print(var_change,type(var_change))

# You still can change variable type even if it is defined
var_type = int(5)
print(var_type,type(var_type))
var_type = 3.1415
print(var_type,type(var_type))

# Assign multiple values
# You can assign same value to multiple variables 
index = count = number  = 5
print(index,count,number)
# Or you can assign multiple value to multiple variables 
index , count, number  = 2 , 5 , 3
print(index,count,number)

# Unpack the list and extract values into variables
cars = ["civic", "supra", "mustang"]
H, T, F = cars
print(H,T,F) 

# Print variables 
# You can print variables while doing operation 
score_A , score_B = 50, 60
print(score_A + score_B) # Printed summery of A and B scores 
# You can even print different variable types together
score_C = 95
score_value = None
if score_C > 90 :
    score_value = "A"
print(score_C,score_value)    