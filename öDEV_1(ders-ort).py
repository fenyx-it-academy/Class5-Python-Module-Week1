name = input('Ad: ')
surname = input('Soyad : ')
no = input('Ögrenci numarası : ')

Ders_1 = input('1.Dersi giriniz : ')
Ders_1_vize = int(input('Ders 1 vize notunuz : '))
Ders_1_final = int(input('Ders 1 final notunuz : '))

Ders_2 = input('2.Dersi giriniz : ')
Ders_2_vize = int(input('Ders 2 vize notunuz : '))
Ders_2_final = int(input('Ders 2 final notunuz : '))

Ders_3 = input('3.Dersi giriniz : ')
Ders_3_vize = int(input('Ders 3 vize notunuz : '))
Ders_3_final = int(input('Ders 3 final notunuz : '))

Ders_4 = input('4.Dersi giriniz: ')
Ders_4_vize = int(input('Ders 4 vize notunuz : '))
Ders_4_final = int(input('Ders 4 final notunuz : '))

Ders_1_ortalama = (Ders_1_vize * 0.4) + (Ders_1_final * 0.6)
Ders_2_ortalama = (Ders_2_vize * 0.4) + (Ders_2_final * 0.6)
Ders_3_ortalama = (Ders_3_vize * 0.4) + (Ders_3_final * 0.6)
Ders_4_ortalama = (Ders_4_vize * 0.4) + (Ders_4_final * 0.6)


print("{} :{} ".format(Ders_1,Ders_1_ortalama))
print("{} :{} ".format(Ders_2,Ders_2_ortalama))
print("{} :{} ".format(Ders_3,Ders_3_ortalama))
print("{} :{} ".format(Ders_4,Ders_4_ortalama))

Dersler=Ders_1_ortalama,Ders_2_ortalama,Ders_3_ortalama,Ders_4_ortalama
for i in Dersler:
    if i<50:
        print("Kaldınız")
    else: 
        print("Geçtiniz")

    