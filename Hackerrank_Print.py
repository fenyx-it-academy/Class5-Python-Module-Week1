n = int(input("Enter a number between 1,150 :"))
for i in range(1,n+1) :
    if  n<1 or n>150:
        print('Please enter a number between 1,150 :')
        break
    else :
        print(i, end="")
    