"""
Function Programming
Object Oriented Programming
Procedure Oriented Programming



#attribute - data, properties || Variables
#Behaviour -  action defines || methods  - Functions


#methods - also known as functions

#object -
#class - blueprint
#encapsulation
#abstraction
#polmorphism

class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Configuration is :", self.cpu,self.ram)


comp1 = Computer("i5", 16)
com2 = Computer("i7", 32)

#print(type(comp1))

#comp1.config()
#com2.config() #we use mostly this syntax
"""

# 1.Constructor
# 2.Self


# Heap Memory - all objects are stored in the heap memory
"""

class Computer:

    def __init__(self):
        self.age = 30
        self.name = "Datha"

    ##def update(self):
      ##  self.age = 29

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1= Computer()
c1.name = "Prasagnya"
c1.age = 36


print(id(c1))

C2 = Computer()
#C2.age
print(id(C2))

#size of the object?
#####Depends on the no.of variables and size of each variable

#who allocate size to object ?
#ans : Constructor

if c1.compare(C2):
    print("Same")
else:
    print("Not same")


print(c1.name, c1.age)
print(C2.name, C2.age)
"""

# Types of variables
"""
1. Instance Variable
2.Class Variable or static variable
"""
"""
class Car:

    wheels = 4

    def __init__(self):
        self.mil = 10
        self.company = "BMW"


c1 = Car()
c2 = Car()

c1.mil = 5

Car.wheels = 5

#namespace  : it is an area where you create and store object/variable
# --class namespace
# --Object/Instance namespace


print(c1.mil,c1.company,c1.wheels)
print(c2.mil,c2.company,c2.wheels)
"""

# Types of Methods
"""
1.Variables
2.Methods
    1.Instance - Accessor - fetches the values i.e., gets the values and Mutators - sets the values i.,e sets
    2.Class
    3.Static
"""
"""

class Students:
    school = "D's University"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m3 + self.m2 + self.m1) / 3

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class: in abc module")


s1 = Students(4, 2, 3)
s2 = Students(2, 3, 5)

print(s1.avg())
print(s2.avg())
print(Students.getschool())

Students.info()

"""
####################################
#inner class
"""
Class:
Variable
Methods / Functions
"""

"""
class Student:

    def __init__(self, name, rno):
        self.name = name
        self.rno = rno
        self.lap = self.Laptop()

    def show(self):
        print(self.name,self.rno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = "Hp"
            self.CPU = "i7"
            self.ram = 16

        def show(self):
            print(self.CPU,self.ram,self.brand)

s1 = Student("Datha",6)
s2 = Student("Prasagnya",7)

s2.show()

"""

#####################
#inheritence
"""
class A:
    def __init__(self):
        print("in A init")

    def f1(self):
        print("F1 is working")

    def f2(self):
        print("f2 is working")

class B:
    def __init__(self):
        print("in b init")

    def f3(self):
        print("F3 is working")

    def f4(self):
        print("f4 is working")

class c(A,B):

    def __init__(self):
        print("in C init")
        super().__init__()


obj = c()
  
"""

#Polymorphism - poly :  many ; morph : form
#many form

#implementation of polymorphism
#duck typing
#operator overloading
#method overloading
#method overriding

##################### DUCK TYPING ##########################
"""
#Dynamic type

class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self,ide):
        ide.execute()

ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)
"""

#################### OPerator overloading #################

a = 5
b = 6

print(a + b)

print(int.__add__(a,b))

class stu:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

s1 = stu