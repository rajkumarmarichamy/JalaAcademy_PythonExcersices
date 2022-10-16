# Write a function for arithmetic operators(+,-,*,/)

'''
val1 = input('enter first number here > ')
val2 = input('enter second number here > ')


def add():
    return float(val1) + float(val2)


def sub():
    return float(val1) - float(val2)


def mul():
    return float(val1) * float(val2)


def div():
    return float(val1) / float(val2)


print(f'the addition of two numbers is', add())
print(f'the subraction of two numbers is', sub())
print(f'the multiplication of two numbers is', mul())
print(f'the division of two numbers is', div())
'''

# Write a method for increment and decrement operators(++, --)
# using operators
'''
a = 0
a += 1
a = a+1
print('The value of a is ', a)

# using loop for increment and decrement
print("INCREMENTED FOR LOOP")
a = 0
for i in range(5):
    a += 1
    print(a)

print("DECREMENTED FOR LOOP")
for i in range(4, -1, - 1):
    print(i)
'''
# Write a program to find the two numbers equal or not.

'''
a = input('Enter first number: ')
b = input('Enter second number: ')
if a==b:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")
'''

# Program for relational operators (<,<==, >, >==)

'''
a = int(input('val1>'))
b = int(input('val2>'))

print('val1 is lesser than val2 => ', a < b)
print('val1 is lesser than or equal to val2 => ', a <= b)
print('val1 is greater than val2 => ', a > b)
print('val1 is greater than or equal to val2 => ', a >= b)
print('val1 is equal to  val2 => ', a == b)
print('val1 is not equal to val2 => ', a != b)

# Print the smaller and larger number.

a = float(input('Enter first number: '))
b = float(input('Enter second number: '))
'''

# To print larger number
a = 4
b = 6

if a > b:
    print(a, "is greater ")
else:
    print(b, " is greater ")

# To print samller number
if a < b:
    print(a, "is smaller ")
else:
    print(b, " is smaller ")
