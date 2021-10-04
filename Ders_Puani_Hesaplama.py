
ad = input("adınız:")
soyad = input("soyadınız :")
numara = input ("numaranız:")
i = 0
while  i < 4:
    dersler = input ("ders adı :")
    i += 1
    vize = float(input(' Lütfen vize notunuzu giriniz : '))
    final = float(input('Lütfen final notunuzu giriniz : '))
    ortalama=(float(vize)*0.4)+(float(final)*0.6)
    if(ortalama<50):
        print("Kaldınız")
    else:
        print("Geçtiniz")
        print("\n")
