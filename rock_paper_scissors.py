print("***Playing Rock_paper_scissors .The players have to choose which options***.\nGame's rools is clear. Rock eats scissors. Paper eats rock. Scissors eats paper.Please follow the instructions.")

player1 = input("Player 1 : ")
player2 = input("Player 2 : ")


gamecounter = int(input("How many game you wanna play ? : ") )


p1point = 0
p2point = 0


gamenumber = 1
while gamecounter > 0 :                                   
    print(f"***Game number {gamenumber} ***")               #it showed game number on terminal.
    gamenumber +=1

    print(player1.upper())
    p1choose = input("Rock : 1\nPaper : 2\nScissors : 3\nYour Choice ? : ")  
    print(player2.upper())
    p2choose = input("Rock : 1\nPaper : 2\nScissors : 3\nYour Choice ? : ")
    
    #Checking player1 winning statuses
    if (p1choose =="1" and p2choose == "3" ) or (p1choose =="2" and p2choose == "1") or (p1choose =="3" and p2choose == "2") :
        p1point += 10 
        gamecounter -= 1 
    #Checking player2 winning statuses
    elif (p2choose =="1" and p1choose == "3" ) or (p2choose =="2" and p1choose == "1") or (p2choose =="3" and p1choose == "2"):
        p2point += 10 
        gamecounter -= 1
    else : 
        print("You chose same option OR Invalid number. Try Again.")
        continue

    
print(f"Results :\n{player1} : {p1point}\n{player2} : {p2point}")