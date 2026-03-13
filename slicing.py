fruit="Apple"
aplen=len(fruit)
print(aplen)
#we use [] for slicing
# print(fruit[0:5])  #including 0 but not 5
# print(fruit[1:3])  #including 1 but not 3
# print(fruit[:5])   # from 0 to excluding 5
print(fruit[0:-2])   #from 0 to len(fruit)-2 =>> 0 to 5-2 = 3 i.e.  App
print(fruit[2:-1])   #from index 2 to len(fruit)-1 =>> p to 5-1 =4 i.e. pl

print(fruit[-3:-2])  #len(fruit)-3==5-3==>2  apple
                     #len(fruit)-2==5-2==>3  12345 =>>2-3==p
f="mango"                 
print(f[-3:-2]) #==> mango
                #==> 12345 ==>2-3==n
                