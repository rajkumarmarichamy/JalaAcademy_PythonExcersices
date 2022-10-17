# Define a static variable and access that through a class

class Python:
    staticVariable = 9


# access through class
print(Python.staticVariable)

# change with in class
Python.staticVariable = 12
print(Python.staticVariable)

# Access through an instance
instance = Python()
print(instance.staticVariable)

# change with in instance
instance.staticVariable = 13
print(instance.staticVariable)
