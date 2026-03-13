def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
        # 5 * factorial(4) 
        # 5 * 4 * factorial(3)
        # 5 * 4 * 3 * factorial(2)
        # 5 * 4 * 3 * 2 * factorial(1)
        # 5 * 4 * 3 * 2 * 1 ,,,,n==1 then return 1
print(factorial(3))
print(factorial(12))
print(factorial(5))

# fibbonacy series 

def fibbonaci(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        return(n + fibbonaci(n-1))
        
print(fibbonaci(4))
print(fibbonaci(5))
print(fibbonaci(6))
print(fibbonaci(7))
print(fibbonaci(8))
print(fibbonaci(1))