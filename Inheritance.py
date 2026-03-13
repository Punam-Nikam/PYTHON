##  INHERITANCE
# When a class derives from another class

# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id

#     def showDetailes(self):
#         print(f"The name of employee id : {self.id} is {self.name}")

# e=Employee("Shubhi sonawane",200)
# e.showDetailes()
# e1=Employee("Mayuri Thoke",300)
# e1.showDetailes()


class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetailes(self):
        print(f"The name of employee id : {self.id} is {self.name}")

class Programmer(Employee):
    def ShowLang(self):
        print("The default language is Python")

e=Employee("Shubhi sonawane",200)
e.showDetailes()

#e1=Employee("Mayuri Thoke",300)

e1=Programmer("Mayuri Thoke",300)
e1.showDetailes()
e1.ShowLang()