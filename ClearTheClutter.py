import os
# os.chdir("data")

# for i in range(0,10):
#     os.mkdir(f"data/Day{i+1}")   #By using os module ,we can make number of files/folder/dir in just seconds
                                 #We dont need to create 10000... number of files manually one at a time

#if we wanna rename all the numbers of directories so we can do as follows 

for i in range(0,10):

    os.rename(f"data/Day{i+1}", f"data/Image{i+1}.jpg")  
    #os.rename(f"data/Tutorial{i+1}", f"data/Tutorial{i+1}.png")  