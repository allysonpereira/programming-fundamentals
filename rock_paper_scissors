#Allyson Sousa Pereira
#Rock, Paper, Scissor

import random

def Maptoitem(player):
    if player == 1:
        item0="Rock"
    elif player == 2:
        item0="Paper"
    else:
        item0="Scissors"
         
    return item0

def printResult(C, P1win, P2win, tieCount):
    print(" ")
    print("You played " +str(C)+ " rounds")
    print("You won "+str(P1win)+" times!")
    print("Computer won "+str(P2win)+" times!")
    print("Ties "+str(tieCount)+" times!")
    
    if P1win>P2win:
        print("You are the winner!")
    elif P1win<P2win:
        print("You lost the game!")
    else:
        print("It's a tie game!")

    

#N=int(input("How many times you want to play?"))
print("Welcome to the game!")
C=0
P1win=0
P2win=0
tieCount=0
playflag=True
while playflag:
    
    Player1=int(input("Pick one from the menu:\n1: Rock \n2: Paper \n3: Scissor \nChoose a Number: "))
    #print(Player1)
    Player2=random.randint(1,3)

    P1 = Maptoitem(Player1)
    P2 = Maptoitem(Player2)



    print("You played " +P1+ " and the computer played "+P2)
    
    if Player1 == Player2:
        print("It's a tie!")
        tieCount += 1
    elif Player1 == 1 and Player2 == 3:
        print("You win!")
        P1win += 1
    elif Player1 == 2 and Player2 == 1:
        print("You win!")
        P1win += 1
    elif Player1 == 3 and Player2 == 2:
        print("You win!")
        P1win += 1
    else:
        print("You lose!")
        P2win += 1

    Q=input("Press anything to play or enter Q to quit: ")
    if Q=="Q" or Q=="q":
        playflag=False
        
    C=C+1

printResult(C, P1win, P2win, tieCount) 


        
