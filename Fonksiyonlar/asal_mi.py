print(""""*****************
ASAL MI?
******************""")

def asal_mi(sayi):
    if(sayi ==1):
        return False
    elif(sayi ==2):
        return True
    else:
        for i in range(2,sayi):
            if(sayi % i == 0):
                return False
        return True

while True:
    sayi=input("Sayı:")

    if(sayi=='q'):
        break
    else:
        sayi=int(sayi)
        if(asal_mi(sayi)):
            print(sayi,"Asal sayıdır")
        else:
            print(sayi,"Asal değildir")
