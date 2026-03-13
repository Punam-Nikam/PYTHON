#

# def cube(x):
#     return x*x*x

l=[1,2,3,5,4,7,4,6]
# newl = []
# for item in l:
#     newl.append(cube(item))
# print(newl)           

# ##  MAP is used as below imnstaed for above

# newline=list(map(cube,l))
# print(newline)

# newline=list(map(lambda x:x*x*x,l))
# print(newline)

### FILTER ##

# def filter_function(a):
#     return a>4
# neww=list(filter(filter_function,l))
# print(neww)

### REDUCE ##

from functools import reduce
numbers=[1,2,3,4,5]     #op=15,sum of all nos in list
sum=reduce(lambda x,y:x+y,numbers)
print(sum)