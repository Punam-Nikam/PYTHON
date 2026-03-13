#Strings are immutable
a="!!!punam!!!PUNAM!!!PunAm!!!!"
print(len(a))
print(a.upper())

print(a.lower())
print(a.rstrip("!"))   #trailing(end)! will be removed and all the string we+ill be as it is
print(a.replace("punam","Akkuu"))

pg="introduction to the javascript will be starting from tomorrow"
print(len(pg))
print(pg.capitalize())
print(a.endswith("!!!")) #returns true if endswith !!! ->here true
print(a.count("punam"))  #returns count of word
pg="welcome to the console!!"
print(pg.endswith("to",4,10))   #returns true /false ->here true

str1="She's a very good girl,she is honest"
print(str1.find("is"))  #returns the index position i.e.27
print(str1.find("He"))  #return -1 bcuz He is not present in str1
print(str1.index("he")) #Subsrtring not found error

print(str1.title())        #returns the string as all initial letter capitals
print(str1.swapcase())     #returns with all the small letere as capital and all capitals with small