# Lambda functions are single expressions

# def double(x):
#     return x*2  #instead of this,we can use 

def apple(fx,value):
    return 6+fx(value)

double = lambda x:x*2    #this 
cube=lambda x:x*x*x
avg=lambda x,y,z:(x+y+z)/3

print(double(5))
print(cube(5))
print(avg(2,2,2))
print(apple(lambda x:x*x,2))