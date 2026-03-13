# # """Decorators""" in python is the fuction which returns modified function(updatable)
# A decorator is the function that takes another function as argumet and returns a new function function that modifies the behaviour of the original function.
# 
##  SYNTAX  ##

# @decorator_function
# def my_function():
#     pass

# def my_function():
#     pass
# my_function=decorator_function(my_function)

def greet(fx):
    def mfx(*args,**kwargs):    #agrs used for take arguments as tuple and kwargs for dictionary
        print("Good morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet      #
def hello():
    print("Hello world")

# @greet
def add(a,b):
    print(a+b)
    

hello()     #
#add(1,2)
greet(add)(1,2)
# greet(hello)() for this # if i dont use @greet

## This will output as  Good morning
                    #   Hello world
                    #   Thanks for using this function

    ## means it will greet hello world function using other function as good morning and thanks wala line

