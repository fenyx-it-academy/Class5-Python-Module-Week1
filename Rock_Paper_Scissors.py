kişi_1 = input("adınızı giriniz : ")
kişi_2 = input("adınızı giriniz : ")
kişi_1skor = 0
kişi_2skor = 0
i = 0

while i < 10:
    girdi_1 = input('{} seçimini yap R, P or S?'.format(kişi_1))
    girdi_2 = input('{} seçimini yap R, P or S?'.format(kişi_2))
    if girdi_1==girdi_2:
        i += 1   
        continue
    elif (girdi_1==('R'or'r')and girdi_2==('S'or's'))or(girdi_1==('S'or's')and girdi_2==('P'or'p'))or(girdi_1==('P'or'p')and girdi_2==('R'or'r')): #and ve or 
        kişi_1skor += 1
    elif (girdi_2==('R'or'r')and girdi_1==('S'or's'))or(girdi_2==('S'or's')and girdi_1==('P'or'p'))or(girdi_2==('P'or'p')and girdi_1==('R'or'r')):
        kişi_2skor += 1   
            
    i += 1
if kişi_1skor > kişi_2skor:
    print("Tebrikler! {} kazandınız. Skorunuz {}!".format(kişi_1, kişi_1skor))
elif kişi_2skor > kişi_1skor:
    print("Tebrikler! {} kazandınız. Skorunuz {}!".format(kişi_2, kişi_2skor))
else:
    print("sonuç berabere")