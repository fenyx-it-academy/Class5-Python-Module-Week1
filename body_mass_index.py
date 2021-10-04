name = input("Name : ")                 #body_mass_index ==  weight /(lenght**2) (m)
weight = float(input("Your Weight : "))
lenght = float(input("Your Lenght  : "))

body_mass_index = weight/(lenght**2)

if body_mass_index < 25 : 
    print(name.upper()," is Normal size")
elif body_mass_index >= 25 and body_mass_index < 30 : 
    print(name.upper()," is Over weight ")
elif body_mass_index >= 30 and body_mass_index < 40 :
    print(name.upper()," is Obese ")
elif body_mass_index >= 30 and body_mass_index < 40 :
    print(name.upper()," is Too Fat.")