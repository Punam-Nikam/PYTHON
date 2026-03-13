 # GETTERS AND SETTERS

# class MyClass:
#     def __init__(self,value):
#         self._value=value

#     def show(self):
#         print(f"Value is {self._value}")

#     @property
#     def value(self):
#         return self._value
    
# obj =MyClass(100)
# obj.show()




class MyClass:
    def __init__(self,value):
        self._value=value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def t_value(self):
        return 10*self._value
    
    @t_value.setter
    def t_value(self,new_value):
       self._value=new_value/10
    
obj =MyClass(10)
obj.t_value=67
print(obj.t_value)
obj.show()