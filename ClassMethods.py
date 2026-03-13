#
# class Employee:
#     company = "Apple"
#     def show(self):
#         print(f"The name is {self.name} and company is {self.company}")

#     @classmethod        # if not used then company name will be as it is at the last
#     def changeCompany(cls,newCompany):
#         cls.company=newCompany
    

# e1=Employee()
# e1.name="Punam"
# e1.show()
# e1.changeCompany("Tesla")
# e1.show()
# print(Employee.company)

#**

# a="Harry-234-pyth"
# print(a.split("-"))

# op = ['Harry', '234', 'pyth']


    #######  *** CLASS METHODS AS ALTERNATIVE CONSTRUCTIORS IN PYTHON ***  #####

#In OOP the term constructor refers to special type of method that is automatically executed 
# when an object is created from a class.The purpose of constructor is
# to initiate the object's attribute,allowing the object to be fully functional and ready to use.
# However there are times when you may want to create an object in different way,or with different 
# initial values ,than what is provided by the default constructor.
# This is where class methods can be used as aternative constructors

# A class method belongs to the class rather than to an instance of the class.One common use case
# for class methods as alternative constructors is when you want to create an object from data
# that is stored in a different formats , such as strings or dictionary,
# e.g. consider class name "person" has two attributes : "name" and "age" .the default constructor 
# for the class might looks like: 

# class Person:
#     def __init__(self,name,age):
#         self.name=name 
#         self.age=age



## ** SIMPLE ** ##

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name 
#         self.salary=salary

# e1=Employee("Harry",12000)
# print(e1.name)
# print(e1.salary)

# string="John-13000"
# e2=Employee(string.split("-")[0],string.split("-")[1])
# print(e2.name)
# print(e2.salary)


## **** using alternative constructors class methods ****  ##

class Employee:
    def __init__(self,name,salary):
        self.name=name 
        self.salary=salary

    @classmethod        ## classmethod as alternative constructor   #
    def fromstr(cls,string):                                         #
        return cls(string.split("-")[0],string.split("-")[1])         #

e1=Employee("Harry",12000)
print(e1.name)
print(e1.salary)

string="John-13000"
e2=Employee.fromstr(string)
print(e2.name)
print(e2.salary)
