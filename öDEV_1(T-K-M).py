print("____Taş,kağıt,makas oyununa hoşgeldiniz____")
player_1=input("1.oyuncu Lütfen adınızı giriniz:" )
player_2=input("2.oyuncu Lütfen adınızı giriniz:" )

player_1skor=0
player_2skor=0

tur=1

while tur<11 :
    player_1_answer = input("%s,Taş(T),Kağıt(K),Makas(M) hangisini seçmek istersiniz?" % player_1)
    player_2_answer = input("%s,Taş(T),Kağıt(K),Makas(M) hangisini seçmek istersiniz?" % player_2)

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
        print("Geçersiz giriş yaptınız!Lütfen geçerli 3 seçeneğimiz olan T(taş),K(kağıt) veya M(makas) giriniz.")
    
else:
    print("Oyun bitti")
    if  player_1skor  >  player_2skor :
        print("{} kazandi. Skor {} - {}".format(oyuncu_1, oyuncu_1_skor, oyuncu_2_skor))
    elif oyuncu_2_skor > oyuncu_1_skor:
        print("{} kazandi. Skor {} - {}".format(oyuncu_2, oyuncu_2_skor, oyuncu_1_skor))
    else:
        print("Oyun berabere.")   