# Constructor is the special method(function) that used to creates and initialises object in a class 
#constructors invokes automatically as soon as object of class is created.

# class person:
#     name="Pichu"
#     occupassion= "Developer" 

#     def info(self):
#         print(f"{self.name} is a {self.occupassion}")

# a=person()
# a.info()

## **

# class person:
#     def __init__(self):
#        print("Hey im a person")


#     def info(self):
#       print(f"{self.name} is a good {self.occupa}")

# a=person()
# b=person()

## **

class person:
    def __init__(self,n,o):
       print("Hey im a person")
       self.name=n
       self.occupa=o

    def info(self):
      print(f"{self.name} is a good {self.occupa}")

a=person("Harry","Developer")
b=person("Divya","Hr")
a.info()
b.info()
