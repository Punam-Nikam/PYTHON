
##  READING A FILE

# f=open('myfile.txt','r')
# text=f.read()
# print(text)  #To extract/read and print contents of file

# f.close()

##  WRITING A FILE

f=open('myfile.txt','w')
f.write('Hello World!!')  #After write in file,the already content is deleted and new write content overwritten
f.close()


##  APPENDING 

with open('myfile.txt','a') as f:
    f.write("Hey I am new content :) ")
