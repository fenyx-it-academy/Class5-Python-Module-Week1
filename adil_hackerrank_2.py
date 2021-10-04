#2 Find the Runner-Up Score!
n = input('scorlari boslukla ayrarak giriniz:')
arr = map(int,n.split())#boslukla ayrarak girdiklerimizi integer olarak arr listesine aliyoruz
siralama = sorted(set(arr))# arr icindeki sayilari tekrarlanmamis halinde siralayip <siralama> ya veriyoruz.
print(siralama[-2])#sirlama listesideki sondan 2. degeri yazdiririz