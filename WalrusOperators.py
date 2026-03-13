# Walrus operator 
# The walrus operator (:=) allows assignment expressions within an expression.
# It was introduced in Python 3.8.
# Example usage of the walrus operator:
happy=False
print(happy)

print(happy :=  True)

food=list()
while (current_food := input("Enter food item (or 'quit' to stop): ")).lower() != 'quit':
    food.append(current_food)


a=3
print(a+4)
print(b:=a+4)
print(b)