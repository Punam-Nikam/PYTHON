# Hybrid and hierarchical inheritance in python
# Hybrid inheritance is the combination of multiple inheritance and single inheritance in object oriented programming. 
# It is type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into single derived class.And single inheritance is used to inherits the properties of the derived class into a sub derived class.

# In python ,hybrid inheritance can be implemented by creating a class hierarchy ,in which a base classis inherited by multiple derived class ,and one of the derived class is further inherited by a sub-derived class.
 
### *** HYBRID INHERITANCE *** ###

class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Drive3(Derived1,Derived2):
    pass

### *** HIERARCHICAL INHERITANCE *** ###
class BaseClass:
    pass

class D1(BaseClass):
    pass

class D2(BaseClass):
    pass

class D3(D1):
    pass