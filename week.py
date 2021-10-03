<!-- * 1-Rock-Paper-Scissors
* Oyuncularin adlarini alip tas - kagit - makas oyunu oynatiniz.
* Oyun 10 el surecektir. 10 el sonunda kazanan belli olacaktir. Skor sonucta gosterilecektir. -->
count=10
player1=input("First player name: ")
player2=input("Second player name: ")
player1_count,player2_count=0,0
while count>0:
    count-=1
    player1_choose=input("Please choose Rock(r) or Paper(p) or Scissors(s)")
    player2_choose=input("Please choose Rock(r) or Paper(p) or Scissors(s)")
    if (player1_choose=='s' and player2_choose=='p') or (player1_choose=='r' and player2_choose=='s') or (player1_choose=='p' and player2_choose=='r'):
        player1_count+=1
        print("{} win \nScore: {} : {}  \n{} : {}".format(player1,player1,player1_count,player2,player2_count))
        print(player1, " : ", player1_choose,' ',player2,' : ', player2_choose)
    elif (player1_choose=='s' and player2_choose=='s') or (player1_choose=='r' and player2_choose=='r') or (player1_choose=='p' and player2_choose=='p'):
        print("Draw Score: {} : {}  \n{} : {}".format(player1,player1_count,player2,player2_count))
        print(player1, " : ", player1_choose,' ',player2,' : ', player2_choose)
    elif (player2_choose=='s' and player1_choose=='p') or (player2_choose=='r' and player1_choose=='s') or (player2_choose=='p' and player1_choose=='r'):
        player2_count+=1
        print("{} win \nScore: {} : {}  \n{} : {}".format(player2,player1,player1_count,player2,player2_count))
        print(player1, " : ", player1_choose,' ',player2,' : ', player2_choose)
    if count==0:
        if player1_count>player2_count:
            print("The game ended.\n{} won \nScore: {} : {}  \n{} : {}".format(player1,player1,player1_count,player2,player2_count))
        elif player1_count==player2_count:
            print("The game ended.\nDraw \nScore: {} : {}  \n{} : {}".format(player1,player1_count,player2,player2_count))
        else:
            print("The game ended.\n{} won \nScore: {} : {}  \n{} : {}".format(player2,player1,player1_count,player2,player2_count))
<!-- * 2- Ders Puani Hesaplama
* Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, bu derslerin Vize ve Final notlari istenecektir.
* Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir.
* Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır.
* Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir. -->
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
<!-- * 3- Beden Kitle Indeksi Hesaplama
* Bir kisinin ağırlığının, boyuna göre normal olup olmadığını gösteren parametreye Beden Kitle İndeksi denir.
* Kısaca insanın kilosunu kişinin boy uzunluğunun karesine bölersek beden kitle indeksi ortaya çıkar.
* Kullanıcıdan kilo ve boy uzunluğunu alip çıkan sonuç 25'in altindaysa NORMAL,
* 25-30 arasında ise FAZLA KİLOLU, 30-40 arasında ise OBEZ,
* 40 ve üzerinde ise AŞIRI ŞİŞMAN şeklinde uyarı yazdiriniz. -->
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

<!-- HackerRank -->
# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b,a-b,a*b,sep='\n')
# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])
# Print Function
if __name__ == '__main__':
    n = int(input())
    print(*[i for i in range(1,n+1)],sep="")
# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{0:.2f}".format(*[(sum(student_marks[i])/len(student_marks[i])) for i in student_marks if i==query_name]))