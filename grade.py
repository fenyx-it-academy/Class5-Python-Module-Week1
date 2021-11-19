# Ders Puani Hesaplama
"""Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, bu derslerin Vize ve Final notlari
 istenecektir. Vize notunun % 40′ı ile Final Notunun %60′
ınin toplamı yil sonu ortalamasini verecektir. Ortalama 50‘den küçükse ekranda “KALDI“,
 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır. Bu yazdirma islemi 4 ders
 icinde yapilacak ve dersler alt alta yazdirilacaktir."""
 
Ad=input("Adiniz:")
Soyad=input("Soyadiniz:")
ONo=input("Ogrenci No:") 

dersler=["1.Dersin","2.Dersin","3.Dersin","4.Dersin"]
for i in dersler : 
 print(i,"Notlarini giriniz")
 Vize,Final=int(input("Vize puani :")),int(input("Final Puan:"))
 ort=(Vize*0.4)+(Final*0.6)

 if ort<50 :
     print(Ad,Soyad,i,"Yilsonu Orta:",int(ort),"Kaldi")
 else:
     print(Ad,Soyad,i,"Yilsonu ort :",int(ort),"Gecti")
    


