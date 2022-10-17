# different ways of creating a string

import re
string = 'hello'
string1 = "world"
string2 = '''hello world'''
string3 = '''hello 
            world'''

print(string)
print(string1)
print(string2)
print(string3)

# concatenation two strings using + operator

print('concatenated strings', string+' '+string1)

# finding the length of the string
print('length of the string', len(string+' '+string1))

# extract a string using substring

str1 = 'rajkumar'

print('position of "raj:"', str1.index('raj'))
print('position of "r:"', str1.index('r'))

# match a string against a regular expression with matches()
substr = "raj"
substr2 = "raj is a BE graduate"
print(re.match(substr, substr2))

# comparing strings

print(string == string1)
print(string != string2)

#startWith(), endsWith(), strip(), replace(), split()

str2 = 'raj kumar'
print(str2.startswith('r'))
print(str2.endswith('r'))
print(str2.strip('ar'))
print(str2.replace('raj', 'lokesh'))
print(str2.split(' '))
print(str2.split())

# converting integer objects to strings

num = 10
str3 = str(num)
print(str3)
print(type(str3))

# converting upper to lower lower to upper

str4 = 'hello'
str5 = 'world'
print(str4.upper())
print(str5.lower())
