# Operator overloading =>> is a feature in python that allows developers to redefine the behavior of mathematics and comparison operators for custom data types.this means that you can use the standard mathematical operators(+,-,*,/,etc) and comparison operators(>,<,==,etc) in your own classes,just as you wonder for built-in data types like int,float,and str.

### *** WHY DO WE NEED OPERATOR OVERLOADING *** ### 

# op ovrloding allows us to create more readable and intuitive code,for instance,consider a custom class that represents a point in 2D space you could define a method called 'add' to add two points together,but using the + operator makes the code more concise and readable. 

class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    
    def __add__(self,x):
        return vector(self.i + x.i, self.j + x.j, self.k + x.k)
    
v1=vector(3,5,6)
print(v1)

v2=vector(1,2,9)
print(v2)

print(v1+v2)
print(type(v1+v2))