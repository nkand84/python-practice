
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
# to modify object property
c1.year = 2017
# print(c1.year)
# calling method of the object
c1.myCars()

print("="*50)
# create a person class with 2 properties and 1 method
class Person:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def myPersonFunc(self):
        print("My name is " + " " + self.fname + " " + self.lname + " " + "and I am " + " " + str(self.age)+ " " + "years old")
p1 = Person("Jack","Doe",30)
p2 = Person("Mary","Williams",28)
p1.myPersonFunc()
p2.myPersonFunc()

print("="*50)
# create a child class that inherits the properties and methods of parent class
# pass the parent class as an arg
# use "pass" if u dont have any properties to be added
class Student(Person):
    pass
s1 = Student("Mike","Doe",20)
s1.myPersonFunc()

# create a cars class
cars_list = []
class Cars:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def myCarsFunc(self):
        print(" This car is " + self.brand)
c1 = Cars("Acura","MDX",2015)
c2 = Cars("Benz","S-class",2010)
c3 = Cars("BMW","x3",2014)
cars_list.append(c1.brand)
cars_list.append(c2.brand)
cars_list.append(c3.brand)
c1.myCarsFunc()
print(cars_list)

