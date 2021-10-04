print("VÜCUT KİTLE ENDEKSİ HESAPLAMA PROGRAMI")
boy = float(input("Boy m):"))
kilo = int(input("Kilo (kg):"))
endeks  = kilo/(boy*boy)
if endeks < 25:
    print("normal")
elif 25< endeks < 30:
    print("fazla kilolu")
elif 30< endeks < 40:
    print("fazla kilolu")
elif endeks > 40:
    print("obez")
