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

# isinstance() function checks data type

if isinstance(var_int,int):
    print("var_int is whole number(int)")

if isinstance(var_float,int):
    print("var_float is whole number(int)")  
else:
    print("var_float is not whole number(int)")  