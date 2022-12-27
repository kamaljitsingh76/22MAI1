# Python3 program to
# demonstrate instantiating
# a class


class Dog:
    # A simple class attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)

    def display(self,x,y):
        self.attr1 = x
        self.attr2 = y
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
# Driver code Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects

Rodger.fun()
Rodger.attr1 = "dog1"
Rodger.display('dog2','dog3')
print(Rodger.attr1)