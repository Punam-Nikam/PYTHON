# # MULTIPLE INHERITANCE is the powerful feature in oop that allows a class to inherits attributes and methods from multiple parent classes.
# This can be useful in situations where a class needs to inherits functionality from multiple sources.
# A,B -> C
#SYNTAX ==>>

# Class ChildClass(ParentClass1,ParentsClass2,ParentClass3):
#     #class body


class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"The name is {self.name}")
class Dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"The dance is {self.dance}")    
    
class DancerEmployee(Dancer,Employee):
    def __init__(self,dance, name):
        self.name=name
        self.dance=dance

o=DancerEmployee("Katthak","Shivani")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())