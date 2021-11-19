#Beden kitle indeksi hesaplama

Height=float(input("Please enter your height in m :"))
Weight=int(input("Please enter your weight in kg :"))
Indx=Weight/(Height**2)
print("Kitle indeksiniz :",int(Indx))
if Indx<25 :
    print("Normal.")
elif  25<=Indx<=30 :
    print("Fazla Kilolu")
elif 30<Indx<=40 :
    print("Obez")
else :
    print("Asiri sisman")
