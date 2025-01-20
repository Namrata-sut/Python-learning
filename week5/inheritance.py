# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Create a class named Person, with firstname and lastname properties, and a printname method:


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()


# Create a class named Student, which will inherit the properties and methods from the Person class:

# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)
#
#
# x = Student("Mike", "Olsen")
# x.printname()

# super() function that will make the child class inherit all the methods and properties from its parent:


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def printname(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Mike", "Olsen", 2019)
x.printname()

