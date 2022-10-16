# Writting a program to print my name.

print('Raj Kumar')

# writting a multiline comment

print('single line comment')

# writting a multiline comment
# wrirring a multiline comment

print('multi line commments')

# variables with different data types
#int, Boolean, Char, float, double

var_int = 10
print("Type of var_int: ", type(var_int))
var_bool = False
print("Type of var_bool: ", type(var_bool))
var_char = 'a'
print("Type of var_char: ", type(var_char))
var_float = 10.2
print("Type of var_char: ", type(var_float))
var_string = 'Hello'
print("Type of var_string: ", type(var_string))

# Define the local and Global variables with the same name and print both variables and
# understand the scope of the variable


a = 5  # global variable


def f():
    print('Inside f() : ', a)


f()


def g():
    b = 2  # local variable
    print('Inside g() : ', b)


g()


def h():
    global c
    c = 4


h()
print(c)
