### Oyuncularin adlarini alip tas - kagit - makas oyunu oynatılacaktır.
### Oyun 10 el surecektir. 10 el sonunda kazanan belli olacaktir. Skor sonucta gosterilecektir.

Oyuncu_1_Skor = 0                                      # Oyuncuların başlangıç skorları gösteriliyor.
Oyuncu_2_Skor = 0

seçenek = ( "Taş", "Kağıt", "Makas" )                  # Oyundaki seçenekler tanımlanıyor.
Taş = seçenek [0]
Kağıt = seçenek [1]
Makas = seçenek [2]

Oyuncu_1 = input ("Lütfen Adınızı Giriniz: ")          #Oyunculardan adları isteniyor.
Oyuncu_2 = input ("Lütfen Adınızı Giriniz: ")


print("Oyuna Hoşgeldiniz" + " " + Oyuncu_1.capitalize() + " ve " + Oyuncu_2.capitalize())  

while (True) :

    seçim_1 = input ( Oyuncu_1.capitalize() + " " + "Taş mı Kağıt mı Makas mı? : " )    # Seçim yapılması isteniyor.  
    seçim_2 = input ( Oyuncu_2.capitalize() + " " + "Taş mı Kağıt mı Makas mı? : " )

    if seçim_1 == Taş:                                                                  # Oyunda seçim bölümleri.
        if seçim_2 == Taş:
            print ("Berabere")
        elif seçim_2 == Kağıt:
            print(Oyuncu_2.capitalize() + " " + "Kazandı")
            Oyuncu_2_Skor += 1
        elif seçim_2 == Makas:
            print(Oyuncu_1.capitalize() + " " + "Kazandı")
            Oyuncu_1_Skor += 1


    if seçim_1 == Kağıt:
        if seçim_2 == Kağıt:
            print ("Berabere")
        elif seçim_2 == Makas:
            print(Oyuncu_2.capitalize() + " " + "Kazandı")
            Oyuncu_2_Skor += 1
        elif seçim_2 == Taş:
            print(Oyuncu_1.capitalize() + " " + "Kazandı")
            Oyuncu_1_Skor += 1


    if seçim_1 == Makas:
        if seçim_2 == Makas:
            print ("Berabere")
        elif seçim_2 == Taş:
            print(Oyuncu_2.capitalize() + " " + "Kazandı")
            Oyuncu_2_Skor += 1
        elif seçim_2 == Kağıt:
            print(Oyuncu_1.capitalize() + " " + "Kazandı")
            Oyuncu_1_Skor += 1

    if Oyuncu_1_Skor == 10 :                                                              # 10 olan kazanıyor.
        print ("Oyunu" + " " + Oyuncu_1.capitalize() + " Kazandı ")
    elif Oyuncu_2_Skor == 10 :
        print ("Oyunu" + " " + Oyuncu_2.capitalize() + " Kazandı ")

        print("Oyunu beğendiniz mi? Eğer beğendiyseniz (E)'ye beğenmediyseniz (H)'ye basınız. ")     # Anket
        cevap = input ()
        if (cevap == "E" ):
            print("İyi eğlenceler ;) ")
        elif (cevap == "H" ):
            print("Bunu duyduğumuza çok üzüldük :( ")
            break