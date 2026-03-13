#*# SINGLE INHERITANCE 
# it is most common type of inheritance 
# Single inheritance is a type of inheritance where a class inherits properties and behaviours from a single parent class
#Syntax = >>
# class ChildClass(ParentClass):
#    #class body

class Animal:
    def __init__(self,name,species):
        self.name=name 
        self.species=species

    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name, species="Dog")
        self.breed=breed

    def make_sound(self):
       print("Bark")

d=Dog("Dog","Dogesh")
d.make_sound()

a=Animal("Dog","Dog")
a.make_sound()