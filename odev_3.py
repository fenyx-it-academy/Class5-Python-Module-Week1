print('''Beden Kitle Indeksi hesablama sitemine hos geldiniz!
asagina kilonuzu"KG" ve uzunlugunuzi "Metre" olarak giriniz!''' )
kilo = float(input('agirliginiz giriniz KG = '))#agirligi girilir
uzunluk = float(input('boy uzunlugunuzu giriniz M = '))#uzunlugu girilir
bki = int(kilo/uzunluk**2) #Beden Kitle İndeksi hesaplanir
print("sizin Beden Kitle indeksiniz = {}".format(bki))# bki yazdirilir
if bki < 25: #eger bki 25in altindaysa
    print('NORMAL')
elif 25 <= bki <30:#bki 20 ile 30 arsindaysa
    print('FAZLA KiLOLU')
elif 30 <= bki < 40: #30 ile 40 arasinaysa
    print('OBEZ')
else:#eksince 
    print('AŞIRI ŞİŞMAN')