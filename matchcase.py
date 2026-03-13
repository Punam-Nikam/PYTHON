#matchcase is the new edition of python3 -->like switch statement in c,c++ or java,etc..
x=int(input("Enter value of x"))
match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
   
    # case _ if x!=8:
    #     print("8 is not = ",x)
    case _ if x>=0:
        print("x is positive")
    case _ if x<0:
        print("x is negative")
    case _:  # case _ : is the default case  
        print("x is ",x)
   