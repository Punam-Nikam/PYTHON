# def average(a=4,b=6):
# def average(a,b):
#     print("The average is ",(a+b)/2)
# # average()    
# average(4,6)

def avg(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("average is : ", sum/len(numbers))


avg(5, 6)


def name(**name):
    print(type(name))
    print("Hello,", name["fname"],name["mname"],name["lname"])

name(mname="Darshan",lname="Raval",fname="Gabbu urf")