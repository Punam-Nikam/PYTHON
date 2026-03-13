# dictionary is the ordered collection of data items
# dictionary items are key-value pairs that are separated by commas,
# and enclosed within curly braces { } # this is ordered

dict={
    1:"Aku",
    2:"Punu",
    3:"Mau",
    4:"Shubh"
}
print(dict[1])
print(dict[2])

d={"Aku":"Best Friend","Punu":"Bestie"}
print(d["Aku"])

print(d)


info={'name':'punam','age':20,'edu':'graduate'}
print(info)
print(info['name'])     # this is manual way to access value of key 
print(info.get('name')) # this is another way to access value of key,
                        # get is important if we want our program to throw error in case when the # key doesnt exist in your program like,name22 for key name ->it will #print none if key is not exist

print(info.values())

print(info.keys())  #we can print keys in this and next method

# for key in info.keys():
#     print(info[key])

for key in info.keys():
    print(f"The values corresponding to key {key} is {info[key]}")


    ##### Dictionary methods  ###

ep={ 122:45,123:89,234:534,422:542,521:455}
ep1={678:899,543:999}

ep.update(ep1)
print(ep)

# ep.popitem()   #pops(removes) the last element
del ep[122]
print(ep)