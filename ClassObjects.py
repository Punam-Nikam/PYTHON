class person:
    name="Pichu"
    occupassion= "Developer" 
    networth:10
    def info(self):
        print(f"{self.name} is a {self.occupassion}")

#  Self ==> self parameter is a reference to the current instance of class,
# and is used to acess variables that belongs to the class

a=person()
b=person()
b.name="achu"
b.occupassion="HR"
print(b.name,"is",b.occupassion)
a.info()