
# Python allows the else keyword to be used with the "for" loops and "while" loops as well
# The else block appears after the body of the loop
# The statement in the else block will be executed after all iterations are completed
# The program exits the loop only after the else block is executed

for i in range(6):
    print(i)   
    if i==4:
     break  # Here loop is not break down,its completed here,so no else part will be executed
else:
    print("sorry no i")


# for i in range(5):
#     print(i)


# for i in []:
#     print(i)   #if we provide empty list ,then it goes to else part and execute else:
# else:
#     print("sorry no i")

i=0
while i<7:
   print(i)
   i=i+1
            # Here else will be executed
else:
   print("Sorry no i")


for x in range(5):
   print("iteration no {} in for loops".format(x+1))
else:
   print("else block in loop")
print("Out of loop")