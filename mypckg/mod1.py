class Point:
    def __init__(self, x, y):  # constructor
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")
