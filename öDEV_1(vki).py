print("____Height Weight Index____")

Height=int(input("Lütfen Boyunuzu Giriniz:"))
Weight=int(input("Lütfen Kilonuzu Giriniz:"))

HWI=Weight/((Height/100)**2)
print("Vücut kilo indeksiniz:",HWI)

if HWI<25:
    print("Normal")
elif 25<=HWI<30:
    print("Fazla Kilolu")
elif 30<=HWI<40:
    print("Obez")
else:
    print("aşırı şişman")
