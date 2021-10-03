boy = float(input("Boy(m):"))
kilo = int(input("Kilo(kg):"))

indeks = kilo/(boy*boy)
if indeks < 25:
    print("NORMAL")
elif 25 <= indeks <= 30:
    print("Fazla kilolu")
elif 30 < indeks < 40:
    print("OBEZ")
else:
    print("Asiri sisman")