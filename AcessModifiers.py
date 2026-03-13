class Employee:
    def __init__(self):
        self.__name = "Harry"  #__name is private attributr

a=Employee()
# print(a.__name)  #    Cannot be access name directly
#                      this will shhow erroer because name is declared private so 
#                      we write its class with it ,where from it is belonging.
#                       Using employee,it can be access indirectly
print(a._Employee__name)

print(a.__dir__())  # It shows all the attributes/methods