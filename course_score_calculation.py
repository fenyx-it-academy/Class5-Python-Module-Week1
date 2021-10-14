### Ders puanı hesaplanacak. + ders adı ve vize final notları istenecek. 
### Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir.
### Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır.
### Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir.

Kullancıcı_Adı = input("Adınızı Giriniz: ")                                 # Kullanıcı bilgileri alınıyor...
Kullancıcı_Soyadı = input("Soyadınızı Giriniz: ")
Kullancıcı_No = input("Numaranızı Giriniz: ")
print("Merhaba" + " " + Kullancıcı_Adı.capitalize() + " " + Kullancıcı_Soyadı.capitalize())

Ders_1 = input("Dersinizin Adını Giriniz: ")                                # Ders bilgileri alınıyor...
Ders_1_Vize = int(input ("Vize Notunuzu Giriniz: "))
Ders_1_Final = int(input ("Final Notunuzu Giriniz:"))
Ders_1_Ort = float (0.4*Ders_1_Vize)+(0.6*Ders_1_Final)
Ders_2 = input("Dersinizin Adını Giriniz: ")
Ders_2_Vize = int(input ("Vize Notunuzu Giriniz:"))
Ders_2_Final = int(input ("Final Notunuzu Giriniz:"))
Ders_2_Ort = float (0.4*Ders_2_Vize)+(0.6*Ders_2_Final)
Ders_3 = input("Dersinizin Adını Giriniz: ")
Ders_3_Vize = int(input ("Vize Notunuzu Giriniz:"))
Ders_3_Final = int(input ("Final Notunuzu Giriniz:"))
Ders_3_Ort = float (0.4*Ders_3_Vize)+(0.6*Ders_3_Final)
Ders_4 = input("Dersinizin Adını Giriniz: ")
Ders_4_Vize = int(input ("Vize Notunuzu Giriniz:"))
Ders_4_Final = int(input ("Final Notunuzu Giriniz:"))
Ders_4_Ort = float (0.4*Ders_4_Vize)+(0.6*Ders_4_Final)



while (True):                                                               # Karar bölümü...

    if Ders_1_Ort>=50:
        print( Ders_1.capitalize() + "'den GEÇTİ")
    else:
        print( Ders_1.capitalize() + "'den KALDI")
        

    if Ders_2_Ort>=50:
        print(Ders_2.capitalize() + "'den GEÇTİ")
    else:
        print(Ders_2.capitalize() + "'den KALDI")
        

    if Ders_3_Ort>=50:
        print(Ders_3.capitalize() + "'den GEÇTİ")
    else:
        print(Ders_3.capitalize() + "'den KALDI")
        

    if Ders_4_Ort>=50:
        print(Ders_4.capitalize() + "'den GEÇTİ")
    else:
        print(Ders_4.capitalize() + "'den KALDI")

    break