# <!-- * 2- Ders Puani Hesaplama
# * Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, bu derslerin Vize ve Final notlari istenecektir.
# * Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir.
# * Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır.
# * Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir. -->
students_informations=[input("Ogrencinin adi: "),input("Ogrencinin soyadi: "),input("Ogrencinin numarasi: ")]
subject_1=[input("Ders adi: "),int(input("Vize puani: ")),int(input("Final puani: "))]
subject_2=[input("Ders adi: "),int(input("Vize puani: ")),int(input("Final puani: "))]
subject_3=[input("Ders adi: "),int(input("Vize puani: ")),int(input("Final puani: "))]
subject_4=[input("Ders adi: "),int(input("Vize puani: ")),int(input("Final puani: "))]
for i in [subject_1,subject_2,subject_3,subject_4]:
    point=i[1]*0.4+i[2]*0.6
    if point>=50:
        print("{} numarali ogrenci {} dersinden {} puan ile gecti.".format(students_informations[2],i[0],point))
    else:
        print("{} numarali ogrenci {} dersinden {} puan ile kaldi.".format(students_informations[2],i[0],point))