# In ptyhon the seek() and tell()mdunctions are used to work with file on=bjects and their
# #positions within a file.
#These functions are part of built in IO module ,which provides a consistent interface for reading
# writing to various files like objects,such as files,pipes and in-memory buffers

####    SEEK() FUNCTION ##

#seek() function allows us to move the the current position within a file to a specific point
# The position is specified in bytes
# We can move either forward or backward from the current position

# with open('myfile.txt','r') as f:
#     print(type(f))

#     f.seek(10)  # moves to the 10th byte in the file,then..
    
#     data=f.read(5)  # read next 5 bytes
#     print(data)     #..then prints 5 bytes after 10 bytes ]


    ###     TELL() FUNCTION ##
# the tell() function returns the current position within the file,in bytes .
# this can be useful for keeping track of your location within the file or 
# for seeking to a specific position relative to the current positon

with open('myfile.txt','r') as f:
    #read the first 10 bytes 
    data=f.read(10)
    #save the current position
    current_position=f.tell()
    #seek to the saved position
    f.seek(current_position)


### TRUNCATE() function

with open('sample.txt','w') as f:
    f.write('Well begin is half done!!')
    f.truncate(10)              #IT wll write 10 bytes/chars in file