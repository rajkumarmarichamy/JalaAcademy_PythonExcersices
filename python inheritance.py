# inheritance
# objective of the program is to write a program to define attributs of humans
# A, B and C are classes
# A is a super class, B is a subclass of A, C is a sub class of B
#A = CommonAtb
#B = Mammmal
#C = Humans

class CommonAtb:

    def __init__(self, name):
        self.name = name

    def walk(self):
        print(self.name, "walks")

    def crawl(self):
        print(self.name, "crawls")


class Mammal(CommonAtb):
    def __init__(self, name):
        self.name = name

    def feedmilk(self):
        print(self.name, "feedsmilk")


class Humans(Mammal):
    def __init__(self, name):
        self.name = name

    def thinks(self):
        print(self.name, 'thinks')


raj = Humans('raj')
raj.thinks()
raj.walk()
