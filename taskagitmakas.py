print("Taş kağıt makas oyununa hoşgeldiniz")

player_1=input("1.oyuncu Lütfen adınızı giriniz:" )
player_2=input("2.oyuncu Lütfen adınızı giriniz:" )

player_1skor=0
player_2skor=0

tur=1

while tur<11 :
    player_1_answer = input("%s,Taş(T) mi,Kağıt(K) mi,Makas(M) mi?" % player_1)
    player_2_answer = input("%s,Taş(T) mi,Kağıt(K) mi,Makas(M) mi?" % player_2)

    if player_1_answer == player_2_answer:
        print("Berabere!")

    elif player_1_answer == 'T':
        if player_2_answer == 'M':
            print("{},kazandı!".format(player_1))
            tur += 1
            player_1skor += 1
        else:
            print("{},kazandı!".format(player_2))
            tur += 1
            player_2skor += 1

    elif player_1_answer== 'M':
        if player_2_answer == 'K':
            print("{},kazandı!".format(player_1))
            tur += 1
            player_1skor += 1
        else:
            print("{},kazandı!".format(player_2))
            tur += 1
            player_2skor += 1
    elif player_1_answer == 'K':
        if player_2_answer == 'T':
            print("{},kazandı!".format(player_1))
            tur += 1
            player_1skor += 1
        else:
            print("{},kazandı!".format(player_2))
            tur += 1
            player_2skor += 1
    else:
        print("Geçersiz giriş yaptınız!")

else:
    print("Oyun bitti")
    if  player_1skor  >  player_2skor :
        print("{} kazandi. Skor {} - {}".format( player_1, player_1skor, player_2skor))
    elif player_2skor > player_1skor:
        print("{} kazandi. Skor {} - {}".format(player_2, player_2skor, player_1skor))
    else:
        print("Oyun berabere.")   