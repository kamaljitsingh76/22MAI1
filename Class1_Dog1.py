# Python3 program to
# demonstrate defining
# a class
class Abc:
    a  = 10
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def display(self):
        print(Abc.a)
        print(self.a)
x = Abc(5,12)
x.display()
Abc.a = 40
x.display()

y = Abc(4,3)
y.display()
