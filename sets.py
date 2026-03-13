# In sets repeative entry not allowed ,not contains duplicate items
# set is the collection of well defined objects ,diierent items can be allowed
# they are unchangable ,immutable ,encolsed in { }

s={0,5,18,2,6,3,4}   #it can or cannot be maintaine order of elements
print(s)              #op- {0,2,3,4,5,6,18}

p={19,"cat",8,"dogesh",0,'hello'}
print(p)            #in this case,every time we run the code,
                    #it will show diffrent order of set elemnts
                    #We cannot access them as their index like p[1],p[2],...p[3]


hello =set()
print(type(hello))

for value in p:
    print(value)