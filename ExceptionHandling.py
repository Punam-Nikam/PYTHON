# Exception handling is the process of responding to unwanted or unexpected events
#  when a computer program runs
# Exception is used to continue the code,by handling interrupt and avoid hault
# Exception handling deals with these events to avoid the program or system crashing and without this process,exceptions would disrupt the normal operation of a program.
# Python has many built in exceptions that are raised when your program encounters an error


# a=input("Enter the number : ")
# print(f"Multiplication table of {a} is : ")

# try: 

#     for i in range(1,11):
#      print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#      #print(e)  #Print(e) means error line
#    print("Invalid input // Sorry some error occured")

# print("some imp lines of code ")
# print("End of the code")

try:
   num=int(input("enter integer"))
except ValueError:
   print("Number entered is not integer")

#### Finally clouse ##

      ## the finally code block is also part of exception handling
      # when we handle exception using try and except block, we can include a finally block at the end
      # The finnaly block is always executed,so its generally used to for doing the concluding tasks 
      ## ..like closing file resources or closing database connection or 
      ## ..may ending program execution with delightful message.

def func():
   try:
      l=[1,2,3,4]
      i=int(input("Enter the index : "))
      print(l[i])
      return 1
   except:
      print("Error occured")
   finally:
      print("I am always executed")

x=func()
print(x)