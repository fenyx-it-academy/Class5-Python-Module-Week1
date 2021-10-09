# <!-- * 3- Beden Kitle Indeksi Hesaplama
# * Bir kisinin ağırlığının, boyuna göre normal olup olmadığını gösteren parametreye Beden Kitle İndeksi denir.
# * Kısaca insanın kilosunu kişinin boy uzunluğunun karesine bölersek beden kitle indeksi ortaya çıkar.
# * Kullanıcıdan kilo ve boy uzunluğunu alip çıkan sonuç 25'in altindaysa NORMAL,
# * 25-30 arasında ise FAZLA KİLOLU, 30-40 arasında ise OBEZ,
# * 40 ve üzerinde ise AŞIRI ŞİŞMAN şeklinde uyarı yazdiriniz. -->
boy=float(input("Boyunuzu metre cinsinden giriniz: "))
kg=float(input("Kilonuzu giriniz: "))
beden_kitle_endeksi=kg/boy**2
if beden_kitle_endeksi<=25:
    print("Beden kitle endeksiniz : {} \nNORMAL".format(beden_kitle_endeksi))

elif 25<beden_kitle_endeksi<=30:
    print("Beden kitle endeksiniz : {} \nFAZLA KİLOLU".format(beden_kitle_endeksi))
elif 30<beden_kitle_endeksi<=40:
    print("Beden kitle endeksiniz : {} \nOBEZ".format(beden_kitle_endeksi))
else:
    print("Beden kitle endeksiniz : {} \nAŞIRI ŞİŞMAN".format(beden_kitle_endeksi))