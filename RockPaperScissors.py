"""1-Rock-Paper-Scissors
Oyuncularin adlarini alip tas - kagit - makas oyunu oynatiniz. Oyun 10 el surecektir.
10 el sonunda kazanan belli olacaktir. Skor sonucta gosterilecektir.
Tas ,makasi;makas,kagidi;kagit,tasi yener."""

tas,kagit,makas=1,2,3
scorea=0    #skorlari sonda sayabilmek icin iki oyuncunun skorlarina sayac.
scoreb=0
for i in range(0,10):                    #10 el ayni islem icin.
 a=int(input("Oyuncu1,Tas icin 1'e,Kagit icin 2'ye,Makas icin 3'e basiniz :"))
 b=int(input("Oyuncu2, Lutfen Tas(1),Kagit(2),Makas(3) tan birini seciniz :"))

 if a>3 or b>3 or a<=0 or b<=0 :               #Oyuncularin uygun degeri girmesi icin yoneltme
    print("Lutfen Tas,Kagit,Makas tan birini seciniz")

 elif (a==1 and b==3) or (a==2 and b==1) or (a==3 and b==2):
    print("Oyuncu1 kazandi")
    scorea+=1
 elif (b==1 and a==3) or (b==2 and a==1) or (b==3 and a==2):
    print("Oyuncu2 kazandi")
    scoreb+=1                     #Oyunculardan kazanan oldugunda baslangicta atadigimiz sayaclarina eklenecek.
                        
 elif (a==b) : 
    print("Berabere")             #Beraberlik sonucu etkilemiyor.
 

if scorea>scoreb :
   print(scorea,scoreb,("MacSonucu, Oyuncu1 kazandi"))
elif scoreb>scorea :
   print(scorea,scoreb,("MacSonucu, Oyuncu2 kazandi"))
else:
   print(scorea,scoreb,("MacSonucu, Berabere"))
#10 el sonunda sayaclari sonuc icin karsilastirdik.Buna gore kazanan belli olacak.



