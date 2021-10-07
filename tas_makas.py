#Oyuncularin adlarini alip tas-kagit-makas oynatan oyun. Oyun 10 el surup sonunda kazanan belli olacaktir.
oyuncu_1=input("Lutfen birinci oyuncunun ismini giriniz: ") #oyuncu isimleri girmesini istedim.
oyuncu_2=input("Lutfen ikinci oyuncunun ismini giriniz: ")
oyuncu_1_skor=0
oyuncu_2_skor=0
a=0

while a<10: # while dongusu ile 10 el oynamasini sagladim
    o_1_t=input("oyuncu1 tercihin nedir? tas, kagit, makas?: ") #oyuncu1 ve oyuncu2 den tercihlerini aldim
    o_2_t=input("oyuncu2 tercihin nedir? tas, kagit, makas?: ")
    if (o_1_t=="tas" and o_2_t=="makas") or (o_1_t=="kagit" and o_2_t=="tas") or (o_1_t=="makas" and o_2_t=="kagit"):# if ve elif ile kazanan buldum
        oyuncu_1_skor +=1 #kim kazandi ise puanini bir artirdim
    elif (o_1_t=="tas" and o_2_t=="kagit") or (o_1_t=="kagit" and o_2_t=="makas") or(o_1_t=="makas" and o_2_t=="tas"):
        oyuncu_2_skor +=1
    elif (o_1_t=="tas" and o_2_t=="tas") or(o_1_t=="kagit" and o_2_t=="kagit") or (o_1_t=="makas" and o_2_t=="makas"):
        continue
    a +=1    # her bir islemde a yi bir artirdim
if oyuncu_1_skor > oyuncu_2_skor:
    print("Tebrikler",oyuncu_1,"kazandiniz")
elif oyuncu_1_skor < oyuncu_2_skor:
    print("Tebrikler", oyuncu_2,"kazandiniz.")
else:
    print("oyun berabere bitmistir.")