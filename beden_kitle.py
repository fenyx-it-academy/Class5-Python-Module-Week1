# Kullanıcıdan kilo ve boy uzunluğunu alip çıkan sonuç 
# 25'in altindaysa NORMAL, 25-30 arasında ise FAZLA KİLOLU, 
# 30-40 arasında ise OBEZ, 40 ve üzerinde ise AŞIRI ŞİŞMAN şeklinde uyarı yazdirma.
kilo=int(input("Lutfen kilonuzu giriniz: "))
boy=int(input("lutfen boyunuzu cm cinsinden giriniz: "))
beden_kitle_index=kilo/((boy**2)/100)
if beden_kitle_index<25:
    print("Normal")
elif 25<beden_kitle_index<20:
    print("Fazla Kilolu")
elif 30<beden_kitle_index<40:
    print("Obez")
elif beden_kitle_index>40:
    print("Asiri Sisman")