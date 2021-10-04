print("""
Merhaba. 
<tas - kagit - makas> oyununa hos geldiniz!
oyun kurallari:
1. oyuncular once ismini girecek.
2.<tas> icin 1 ,<kagit> icin 2 ve <makas> icin 3 girmelisiniz.
3.oyun 10 el surecek ve 10 elin sonunda puanlariniz aciklanacak.
4.eger puanlariniz esitse tekrar oynanyabiliri siniz.
""")
gamer1 = input('oyuncu 1 adinizi girin:')# 1.oyuncunun adi istenir
gamer2 = input('oyuncu 2 adinizi girin:')# 2.oyuncunun adi istenir
print(gamer1,gamer2,'oyuna hos geldiniz',sep=" ") #welkom
print('1=rock'+'2=papier'+'3=mes') #kural

while (True):# puanlar esitse tekrar oynamak icin dongu
    a = 10 # oynama el sayisi
    gamer1_puan = 0 # 1.oyuncunun baslangic puani
    gamer2_puan = 0 #1.oyuncunun baslangic puani
    while a != 0: #  yun icin dongu,10 el bitince bu dongu biter
        for i in range(a): # for dongusu ile kac el oynanyacagi saglanir
            a -= 1 
            print('{}.el'.format(i+1)) #kacinci el oldugu yaziliri
            while True:
                g1 = input('{} giriniz:'.format(gamer1)) # 1.oyuncunun girmesi istenir
                if g1.isdigit():
                    if 1 <= int(g1)<= 3:
                        break
                    else:
                        print('yanlis girdiniz \n''1 = tas','2 = kagit','3 = makas',sep=",")
                        continue
                else:
                    print('yanlis girdiniz \n''1 = tas','2 = kagit','3 = makas',sep=",")
                    continue
            while True:
                g2 = input('{} giriniz:'.format(gamer2)) # 2.oyuncunun girmesi istenir
                if g2.isdigit():
                    if 1 <= int(g2)<= 3:
                        break
                    else:
                        print('yanlis girdiniz \n''1 = tas','2 = kagit','3 = makas',sep=",")
                else:
                    print('yanlis girdiniz \n''1 = tas','2 = kagit','3 = makas',sep=",")
            if g1 == g2: # eger girdikleri esitse asagiaki yazdirilir
                print('{}.elde beraber kaldini'.format(i+1))
            elif (g1 == 1 and g2 == 3) or (g1 == 2 and g2 == 1) or (g1 == 3 and g2 ==2): #bu sartlara uygunsa
                print('{}.elde {} yendi'.format(i+1,gamer1)) # bu yazdirilir
                gamer1_puan += 1 #ve 1 puan eklenir
            else : #eksince
                print('{}.elde {} yendi'.format(i+1,gamer2)) #bu yazdirilir
                gamer2_puan += 1
    if gamer1_puan > gamer2_puan: #son puanlar karslasir 1.oyuncunun buyukse
        print('tebrikler! {} kazandiniz,puaniniz {}'.format(gamer1,gamer1_puan))# bu yazdirilir
        break #oyun biter
    elif gamer1_puan < gamer2_puan: #eger 2. oyuncunun buyukse
        print('tebrikler! {} kazandiniz,puaniıniz {}'.format(gamer2,gamer2_puan))# bu yazdirilir
        break
    else:#eksince
        print('puanlariniz esittir,tekrar denemek istermi siniz?')# bu yazdirilir
        cevap = input("e/h:") #ve tekrar oynamak icin secim verilir
        if cevap == 'e': #secim e se oyun tekran baslar
            continue
        elif cevap == 'h':# secim h se oyun biter
            break