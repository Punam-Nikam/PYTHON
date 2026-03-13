marks=[88,89,90,93,54,67,77,82]

# index=0
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("Harry,Awesome!!")
#     index+=1


### Enumerate function is a built in function in python,that allows yo to loop over sequence(such as list,tuple or string) and get the index and value of each element in the sequence at the same time

# the enumerate function return tuple/list/string /.. containing index and value of each element in the sequence

for index ,mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("Harry,Awesome!!")
    # index+=1   #No need to increment the index now
