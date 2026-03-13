###  The readlines() method reads a single line from the file.
# If we wanna read multiple lines we can use loop
#The readlines() method reads all the lines of the file and returns them as a list of strings


##  1 : 
### INPUT for the program in myfile.txt 
# Hello World!!Hey I am new content I would also like to acknowledge the c
# whose support and collaboration made this project possible. A special thanks to all, 
# ontributions of my Project partners,
# whose research and work in artificial intelligence and recruitment technology greatly 
# influenced the direction of this project 

#1 program

# f=open('myfile.txt','r')
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line)

##  2 :

###     Input for the program in myfile.txt
###     56,45,78
#       34,67,23
#       78,77,93

# f=open('myfile.txt','r')
# i=0
# while True:
#     i=i+1
#     line=f.readline()
#     if not line:
#         break
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
#     print(f"Marks of students {i} in maths is : {m1}")
#     print(f"Marks of students {i} in java is : {m2}")
#     print(f"Marks of students {i} in py is : {m3}")


## WRITELINES : is the method in python weites a sequence of strings to a file .
# The sequence can be any iterable onject ,such as list/tuple

##  3 :
###         outPUT OF THE PROGRAM IN myfile.txt 
#           line 1
#           line 2
#           line 3
# 

# 3.code

f=open('myfile.txt','w')
lines=['line 1\n','line 2\n','line 3\n']
f.writelines(lines)

