
print("="*50)
# classes and objects
# class is like a blue print for creating objects or an object constructor

class Myclass:
    x = 5
print(type(Myclass))

print("="*50)
# always start class name with uppercase*
class Person:
    # all classes has a built-in init func which is always executed when class is being initiated
    #  its automatically called when the class is used to create a new object
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # method (function) inside the person object
    def myfunc(self):
        print("Hello my name is " + self.name)

# creating an instance of the person object
p1 = Person("NK",30)
print(p1.name)
p1.myfunc()

print("="*50)

# create a car class and create a new object
class Cars:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
# create a method for cars object
    def myCars(self):
        print("You have a "+ self.brand + " " + self.model + " " + str(self.year) + " car")
# new instance of class i.e create a new object
c1 = Cars("acura","MDX",2015)
# print(c1.year)
# calling method of the object
c1.myCars()