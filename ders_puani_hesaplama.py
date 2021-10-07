#Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, bu derslerin Vize ve Final notlari istenecektir. 
# Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir. 
# Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır. 
# Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir.
ogrenci_adi_soyadi=input("Lutfen ogrenci adini ve soyadini giriniz: ")
ogrenci_numarasi= input("lutfen ogrencinin numarasi giriniz")
a=0
liste=[] #bos liste olusturdum
while a<4:
    ders=input("lutfen dersin ismini giriniz: ") #ogrenci bilgileri ve notlar sirasiyla girdim
    vize=int(input("lutfen vize notunu giriniz: "))
    final=int(input("lutfen final notunu giriniz: "))
    ortalama=(vize*0.4)+(final*0.6)
    liste.append([ders,ortalama]) #bos listeye ders ve ortalamalari ekledim
    a+=1
for i in liste:
    if i[1]>50.0:
        print(i[0]+"'den","gectiniz.") #sonucu yazdirdim
    else:
        print(i[0]+"'den","kaldiniz.")