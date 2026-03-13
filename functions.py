#function is the block of code that performs specific task whenever it is called
#Two types of functions:
# 1.Builtin function
# 2.User defined function

# "def" keyword is used to define the function

def calculateMean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
a=9
b=8
calculateMean(a,b)

####

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("second number is greater")

a=17
b=30
isGreater(a,b)


def islesser(a,b):
    pass
### pass is used to continue the function except the block where pass is present,it means the function block will may write after some while,or someone will come to complete it,and you pass from the function block and continue exection of next function


def reminder(i):
    # while(i<=3): 
    for i in range(3):
        print("Hello,Today is 14 julay,you have to complete your task\n Thank You!!!")
        # i+=1
reminder(1)