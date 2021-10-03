
ad = input("adinizi giriniz:")
soyad = input("soyadinizi giriniz:")
ogrenci_numarasi = input("ogrenci numarasini giriniz:")

ders_1 = input("ders adi gir:")
vize = input("vize notunu girin:")
final = input("final notunu girin:")

ders_2 = input("ders adi gir:")
vize_2 = input("vize notunu girin:")
final_2 = input("final notunu girin:")

ders_3 = input("ders adi gir:")
vize_3 = input("vize notunu girin:")
final_3 = input("final notunu girin:")

ders_4 = input("ders adi gir:")
vize_4 = input ("vize notunu girin:")
final_4 = input("final notunu girin: ")

ortalama_1 = (float(vize)*0.4 + float(final)*0.6)
if ortalama_1 >= 50:
    print(ders_1, ":Gecti")
else:
    print(ders_1, ":Kaldi")

ortalama_2 =(float(vize_2)*0.4 + float(final_2)*0.6)
if ortalama_2 >= 50:
    print(ders_2, ":Gecti")
else:
    print(ders_2, ":Kaldi")

ortalama_3 = (float(vize_3)*0.4 + float(final_3)*0.6)
if ortalama_3 >= 50:
    print(ders_3, ":Gecti")
else:
    print(ders_3, ":Kaldi")

ortalama_4 =(float(vize_4)*0.4 + float(final)*0.6)
if ortalama_4 >= 50:
    print(ders_4, ":Gecti")
else:
    print(ders_4, ":Kaldi")

