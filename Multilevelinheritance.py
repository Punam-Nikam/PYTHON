# Multilevel inheritance is like A -> B -> C
##SYNTAX ==>

# class BaseClass:
#     #Base class code

# class DerievedClass1(BasicClass):
#     #Derive class 1 code

# Class DerievedClass2(DerievedClass1):
#     #derive class 2 code

#Multilevel inheritance is a type of inheritance in oop where a derived class inherits from another derived class.
# This type of inheritance allows you to build a hierarcy of classes where one class builds upon another,leading to a more specialized class.

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def showDetails(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name, species="Dog")
        self.breed=breed

    def showDetails(self):
        Animal.showDetails(self)
        print(f"Breed : {self.breed}")

class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self,name, breed="GoldenRetriever")
        self.color=color
    
    def showDetails(self):
        Dog.showDetails(self)
        print(f"Color : {self.color}")

o=GoldenRetriever("Tommy","Black")
o.showDetails()