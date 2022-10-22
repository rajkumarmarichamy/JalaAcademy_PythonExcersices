# Write a program to generate Arithmetic Exception without exception handling

'''print(num=6/0)'''

# Handle the Arithmetic exception using try-catch block

'''try:
    print(num=6/0)
except ArithmeticError:
    print('6')'''

# Write a method which throws exception, Call that method in main class without try block


'''def function():
    print(num=6/0)


try:
    abc = function()
except ArithmeticError:
    print('6')'''

# Write a program with multiple catch blocks
'''name = 'raj'
age = 20
try:
    print(name + age)
    print(num=6/0)

except (TypeError, ArithmeticError) as error:
    print(error)


b = [3, 2, 1]
a = [3, 2, 1]
try:
    a == b
except:
    print("They are not equal")
else:
    print("Both Equal")

print()'''

# Write a program to throw exception with your own message

'''age = 'raj'
try:
    print(age/2)
except:
    print('enter a valid age')'''

# Write a program with finally block

'''try:
    k = 5/0
    print(k)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print('This is always executed')'''

# write a program to generate Arithmetic Exception

'''print(num=6/0)'''

# Write a program to generate FileNotFoundException

'''file1 = open('text1.txt', 'r')'''
