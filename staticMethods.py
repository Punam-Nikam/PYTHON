# STATIC METHODS are the methods that are belogs to class rather than instance of class.
# they defined using the @staticmethod decorator and do not have access to the instance of class.
#(i.e.self)They are called on the class itself,not on instance of class. 
# Static methods are often used to create utility functions that dont need access to instance data
#
# class math:
#   @staticmethod
#   def add(a,b):
#       return a+b

# result = math.add(1,2)
# print(result)    # op : 3

class Math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,n):
        self.num=self.num+n

    @staticmethod
    def add(a,b):
        return a+b
    
a=Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
