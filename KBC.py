# KBC bole toh....Koun Babega Crorepati :) !!!! 

questions = [
    ["Which languag was used to create fb ? ","Python","Java","Cpp","php",4],
    ["Which languag was used to create fb ? ","Python","Java","Cpp","php",4],
    ["Which languag was used to create fb ? ","Python","Java","Cpp","php",4],
    ["Which languag was used to create fb ? ","Python","Java","Cpp","php",4],
    ["Which languag was used to create fb ? ","Python","Java","Cpp","php",4],
    ["Which languag was used to create fb ? ","Python","Java","Cpp","php",4],
    ["Which languag was used to create fb ? ","Python","Java","Cpp","php",4],
    ["Which languag was used to create fb ? ","Python","Java","Cpp","php",4],
    ["Which languag was used to create fb ? ","Python","Java","Cpp","php",4],
    ["Which languag was used to create fb ? ","Python","Java","Cpp","php",4],
    ["Which languag was used to create fb ? ","Python","Java","Cpp","php",4],
    ["Which languag was used to create fb ? ","Python","Java","Cpp","php",4],
    ["Which languag was used to create fb ? ","Python","Java","Cpp","php",4],
    ["Which languag was used to create fb ? ","Python","Java","Cpp","php",4],
    ["Which languag was used to create fb ? ","Python","Java","Cpp","php",4],
    ["Which languag was used to create fb ? ","Python","Java","Cpp","php",4],
    ["Which languag was used to create fb ? ","Python","Java","Cpp","php",4],

]

levels=[1000,2000,3000,6000,8000,10000,20000,32000,40000,500000,60000,7000000,900000,1000000]
money = 0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"a. {question[1]}    b. {question[2]}")
    print(f"c. {question[3]}    d. {question[4]}")
    reply = int(input("Enter your answer (1-4) or 0 to quit"))
    if(reply==0):
        money=levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer , You won Rs. {levels[i]}")
        if(i == 4):
            money=10000
        elif(i == 9):
            money=32000
        elif(i == 14):
            money=1000000
    else:
        print("Wrong Answer")
        break

print(f"You take money home is {money}")