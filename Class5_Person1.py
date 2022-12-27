class PersonClass:

    # default constructor
    def __init__(self):
        self.pname = "Adarsh"

    # a method for printing data members
    def print_pname(self):
        print(self.pname)


# creating object of the class
obj = PersonClass()

# calling the instance method using the object obj
obj.print_pname()
