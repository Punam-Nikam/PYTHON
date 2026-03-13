# snake drinks water == stone s 0
# water distroy gun == paper w 1
# gun kills snake ==sessor g 2
import random

print("WELCOME!! TO THE SNAKE WATER GAME :)")
i=0
while i!=5:
    i+=1 
    computer = random.randint(0,2)
    player=int(input("Enter your choice: 0:Snake,1:Water,2:Gun "))
    print("Player = ",player)
    print("Computer = ",computer)
    if(player==0 and computer==0 or player==1 and computer==1 or player==2 and computer==2):
        print("Draw")
    elif(player==0 and computer==1 or player==1 and computer==2 or player==2 and computer==0):
        print("WIN :)")
    elif(player==1 and computer==0 or player==0 and computer==2 or player==2 and computer==1):
        print("Lose :(")
    else:
        print("Wrong choice!!")

print("The End !!")