ogrenci = input('Adiniz ve soyadinizi giriniz:')
ogrenci_num = input('ogrenci numaranizi giriniz:')
notlar = {} # bos notlar dict
dersler = []# bos dersler listesi
for i in range(4): # 4 ders adi ve puanlari alamak icin dongu
    ders,*line = input('ders adi,vize ve final notlari bosluklarla ayrarak giriniz:').split()#ders ve notlar girilir
    dersler.append(ders) #dersler listesine girilen dersi ekliyoruz
    puanlar = list(map(float, line))# girdigimiz puanlar list olarak kayitlinir
    notlar[ders] = puanlar# mesela :notlar= {'eng': [50.0, 50.0], 'dil': [6.0, 60.0], 'mat': [80.0, 90.0], 'tarih': [50.0, 90.0]}
print('{}-{}'.format(ogrenci.title(),ogrenci_num))# ogrenci adi ve numarasi yazdirilir
for i in dersler:#ders notlari teker teker yazdirmak icin
    orta = ((notlar[i][0]*0.4)+(notlar[i][1]*0.6))# final hesaplam vize40% + final60%
    if orta >= 50 :#eger ortalama notu 50ye esit yada buyukse
        print('-{}- deki ortalama notunuz <{}>,GECTi'.format(i,orta))# gecti
    else:#eksince
        print('-{}- deki ortalama notunuz <{}>,KALDI'.format(i,orta))# kaldi