# Custom errors
# a=int(input("Enter int between 5 and 9 "))

# if(a<5 or a>9):
#     raise ValueError("Values must be between 5 and 9")


##Defining custum exceptions
    # we can define custum exceptions
    #  by creating a new class that is derieved from the built in exception class
    #  This is useful because sometimes we might want to do something..
    # ..when a particular exception is raised.
    # for ex.. sending an error report to the admin,calling an API,etc

    ####  raise ValueError("Values must be between 5 and 9") ##

str=input("Enter quite")
if(str!="quite"):
    raise NameError("No any other string will run")
else:
    print("good!!")