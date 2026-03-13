# string information can be done in python using the format method
# F-string is the new string formatting ,it is also known as string interpolation  or F-String
# f-string can format values from { }

letter="Hey My name is {1} and I am from {0}"
country="India"
name="Punam"

print(letter.format(country,name))
print(f"Hey my name is {name} & im from {country}")

price =499.245001
txt=f"For only {price:.3f} Dollers!"
print(txt)
# print(txt.format(price =499.245001))

print(type(f"{2*30}"))