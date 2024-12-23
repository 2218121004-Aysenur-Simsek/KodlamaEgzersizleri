print(""""*****************
SAYININ TAM BÖLENLERİNİ BULMA
******************""")

def tambolenleribulma(sayi):

    tam_bolenler=[1]

    for i in range(2,sayi+1):
        if(sayi % i == 0):
            tam_bolenler.append(i)

    return tam_bolenler

while True:
    sayi=input("Sayı:")

    if(sayi=='q'):
        break
    else:
        sayi=int(sayi)
        print("Tam bölenler:",tambolenleribulma(sayi))