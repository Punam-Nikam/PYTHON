#Tuples are immutable,non changable and enclosed in aranthesis ()

tup  = (1,5,4,"green",False)
# print(tup)
print(type(tup),tup)

# t=(1,) #,represents that this is tuple
# print(t)

print(tup[2])
print(tup[-2])
print(tup[1:4])

print(tup[:3])  #automatically 0:3
print(tup[1:])  #till the end of the tuple


   ####   Manipulating tuples ##

countries = ("India","Spain","Paris","America","England","Germany")
temp=list(countries)
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
countries=tuple(temp)
print(countries)

## As tuple is immutable, so we convert it in list,
# made changes, 
# and again convert it into tuple

tuple = (0,1,2,6,4,3,2,1,6,5)
res=tuple.index(3) #index of 3 in the tuple is 5th position i.e.= 5
print('count of 3 in tuple is ',res)