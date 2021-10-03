### Bir kisinin ağırlığının, boyuna göre normal olup olmadığını gösteren parametreye Beden Kitle İndeksi denir.
### Kısaca insanın kilosunu kişinin boy uzunluğunun karesine bölersek beden kitle indeksi ortaya çıkar.
### Kullanıcıdan kilo ve boy uzunluğunu alip çıkan sonuç 25'in altindaysa NORMAL, 25-30 arasında ise FAZLA KİLOLU,
### 30-40 arasında ise OBEZ, 40 ve üzerinde ise AŞIRI ŞİŞMAN şeklinde uyarı alınacaktır.

Ad = input ("Adınız : ")
Soyad = input ("Soyadınız : ")
print ("Hoşgeldiniz" + " " + Ad.capitalize()  + " " + Soyad.capitalize() )

Kilo = int(input("Lütfen Kilonuzu Giriniz : "))                           # Kilo bilgisi alınıyor.
Boy = float(input("Lütfen Boyunuzu Giriniz (Örn: 1.83) : "))              # Boy bilgisi alınıyor.
Hesaplama = (Kilo / Boy**2)                                               # Bilgilerin hseplanma bölümü.

while (True):  
    print ("Cinsiyetiniz nedir? Kadınsanız (K)'ye, erkekseniz (E)'ye basınız.")                                             # Çıktı
    cevap = input ()
    if (cevap == "K"):
        if Hesaplama < 25:
            print("Normalsiniz" + " " + Ad.capitalize()  + " " + Soyad.capitalize() + " Hanım " )
            break
        elif Hesaplama >= 25 and Hesaplama < 30:
            print("Fazla Kilolusunuz" + " " + Ad.capitalize()  + " " + Soyad.capitalize() + " Hanım " )
            break
        elif Hesaplama >= 30 and Hesaplama < 40:
            print("Obezsiniz" + " " + Ad.capitalize()  + " " + Soyad.capitalize() + " Hanım " )
            break
        elif Hesaplama >= 40:
            print("Aşırı Şişmansınız" + " " + Ad.capitalize()  + " " + Soyad.capitalize() + " Hanım " )
            break

    if (cevap == "E"):
        if Hesaplama < 25:
            print("Normalsiniz" + " " + Ad.capitalize()  + " " + Soyad.capitalize() + " Bey " )
        
        elif Hesaplama >= 25 and Hesaplama < 30:
            print("Fazla Kilolusunuz" + " " + Ad.capitalize()  + " " + Soyad.capitalize() + " Bey " )
        
        elif Hesaplama >= 30 and Hesaplama < 40:
            print("Obezsiniz" + " " + Ad.capitalize()  + " " + Soyad.capitalize() + " Bey " )
        
        elif Hesaplama >= 40:
            print("Aşırı Şişmansınız" + " " + Ad.capitalize()  + " " + Soyad.capitalize() + " Bey " )

    break