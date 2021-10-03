
oyuncu_1 = input("adinizi giriniz:")  
oyuncu_2 = input("adinizi giriniz:")
sayac = 0
oyuncu_1_kazanma = 0
oyuncu_2_kazanma = 0

while True:
    sayac += 1
    if sayac == 11:
        break
    oyuncu_1_move = input("Bir secenek girin(tas , kagit , makas):")
    oyuncu_2_move = input("Bir secenek girin(tas , kagit , makas):")
    print(f"\nSiz {oyuncu_1_move} sectiniz.,Siz {oyuncu_2_move} sectiniz")
    
    if oyuncu_1_move == oyuncu_2_move:
        print(f"iki oyuncu da{oyuncu_2_move} secti.El berabere")
    elif oyuncu_1_move == "tas":
        if oyuncu_2_move == "makas":
            print("tas makasi ezer.oyuncu_1 kazandi.")
            oyuncu_1_kazanma += 1
        else:
            print("kagit tasi yener. oyuncu_2 kazandi")
            oyuncu_2_kazanma += 1
    elif oyuncu_1_move == "kagit":
        if oyuncu_2_move == "tas":
            print("kagit tasi yener. oyuncu_1 kazandi")
            oyuncu_1_kazanma += 1
        else:
            print("makas kagidi yener.oyuncu_2 kazandi")
            oyuncu_2_kazanma += 1
    elif oyuncu_1_move == "makas":
        if oyuncu_2_move == "kagit":
            print("makas kagidi yener.oyuncu_1 kazandi.")
            oyuncu_1_kazanma += 1
        else:
            print("tas makasi yener. oyuncu_2 kazandi.")
            oyuncu_2_kazanma += 1
print(oyuncu_1 , oyuncu_1_kazanma , "defa kazandi")
print(oyuncu_2 , oyuncu_2_kazanma , "defa kazandi")
