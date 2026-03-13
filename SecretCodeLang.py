## Exercise of encoding and decoding secret messages

str=input("Enter message")
coding=True             ###True for encode,and false for decode
if(coding==True):
    if len(str)>=3:
        r1="009"
        r2="001"

        # str= str[1:]+ str[0]
        # str1=r1+str+r2
        
        str= r1+str[1:]+ str[0]+r2  

        # it will remove the first character of the string and appends at the end
        #  and add rand 3 char at start and end
        
        print(str)

    else:
        # str=str[-1]+str[-2]
        str1=str[::-1]
        print(str1)

else:               ## for decode the message
    if len(str)>=3:
        # str= str[1:]+ str[0]
        # str1=r1+str+r2

        
        str=str[3:-3]
        str= str[-1]+ str[:-1]

        # it will remove the first and last 3 random characters and 
        #  and add last char to first position
        
        print(str)

    else:
        # str=str[-1]+str[-2]
        str1=str[::-1]
        print(str1)

