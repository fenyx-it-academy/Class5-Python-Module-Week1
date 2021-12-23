# <!-- * 1-Rock-Paper-Scissors
# * Oyuncularin adlarini alip tas - kagit - makas oyunu oynatiniz.
# * Oyun 10 el surecektir. 10 el sonunda kazanan belli olacaktir. Skor sonucta gosterilecektir. -->
count=10
player1=input("First player name: ")
player2=input("Second player name: ")
player1_count,player2_count=0,0
while count>0:
    count-=1
    player1_choose=input("Please choose Rock(r) or Paper(p) or Scissors(s)")
    player2_choose=input("Please choose Rock(r) or Paper(p) or Scissors(s)")
    if (player1_choose=='s' and player2_choose=='p') or (player1_choose=='r' and player2_choose=='s') or (player1_choose=='p' and player2_choose=='r'):
        player1_count+=1
        print("{} win \nScore: {} : {}  \n{} : {}".format(player1,player1,player1_count,player2,player2_count))
        print(player1, " : ", player1_choose,' ',player2,' : ', player2_choose)
    elif (player1_choose=='s' and player2_choose=='s') or (player1_choose=='r' and player2_choose=='r') or (player1_choose=='p' and player2_choose=='p'):
        print("Draw Score: {} : {}  \n{} : {}".format(player1,player1_count,player2,player2_count))
        print(player1, " : ", player1_choose,' ',player2,' : ', player2_choose)
    elif (player2_choose=='s' and player1_choose=='p') or (player2_choose=='r' and player1_choose=='s') or (player2_choose=='p' and player1_choose=='r'):
        player2_count+=1
        print("{} win \nScore: {} : {}  \n{} : {}".format(player2,player1,player1_count,player2,player2_count))
        print(player1, " : ", player1_choose,' ',player2,' : ', player2_choose)
    if count==0:
        if player1_count>player2_count:
            print("The game ended.\n{} won \nScore: {} : {}  \n{} : {}".format(player1,player1,player1_count,player2,player2_count))
        elif player1_count==player2_count:
            print("The game ended.\nDraw \nScore: {} : {}  \n{} : {}".format(player1,player1_count,player2,player2_count))
        else:
            print("The game ended.\n{} won \nScore: {} : {}  \n{} : {}".format(player2,player1,player1_count,player2,player2_count))
