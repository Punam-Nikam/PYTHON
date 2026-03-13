#list is an ordered collection of same or diffrent data items
#Stored multiple items in single variable, enclosed in [] square brackets
#list are changable,mutable.

# marks=[3,5,6,"gabbu",True,7,9,2,1]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])

# print(marks[-3])
# print(marks[len(marks)-3])

# if True in marks:
#     print("Yes")
# else:
#     print("No")

# print(marks[0:7])
# print(marks[1:4])
# print(marks[1:9:3])

# lst = [i*i for i in range(5)]
# print(lst)
# lst = [i*i for i in range(10) if i%2==0]
# print(lst)


#### List Methods   ##

l = [1,3,9,2,72,4,46]
print(l)
# l.sort()
# print(l)
# l.append(18)
# print(l)

l.sort(reversed)
print(l)

# # print(l.index(9))

# # m=l.copy()
# # m[0]=0
# # print(l)

# l.insert(1,776)
# print(l)

# m=[223,644,866]
# l.extend(m)
# print(l)