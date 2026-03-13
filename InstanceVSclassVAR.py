# Instance variable

class Employee:
    conapanyName="Apple"   # This is class variable,it can accessed by instance variable also
    def __init__(self,name):
        self.name=name
        self.salary=0.01    #These are instance variable
    def ShowDetailes(self):
        print(f"The name of the employess is {self.name} in {self.conapanyName} have salary is {self.salary}")

# Employee.ShowDetailes(emp1)
emp1=Employee("Aku")
emp1.salary=0.05    # this is how we change or update instance variable
emp1.ShowDetailes()
emp2=Employee("piku")
emp2.ShowDetailes()