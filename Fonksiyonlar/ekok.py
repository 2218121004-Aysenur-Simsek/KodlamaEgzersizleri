print("""*****************
EKOK BULMA
******************""")

def ekok(sayi1, sayi2):
    i = 2
    ekok = 1

    while True:
        if sayi1 % i == 0 and sayi2 % i == 0:
            ekok *= i
            sayi1 //= i
            sayi2 //= i
        elif sayi1 % i != 0 and sayi2 % i == 0:
            ekok *= i
            sayi2 //= i
        elif sayi1 % i == 0 and sayi2 % i != 0:
            ekok *= i
            sayi1 //= i
        else:
            i += 1

        if sayi1 == 1 and sayi2 == 1:
            break
    return ekok

sayi1 = int(input("Sayı1:"))
sayi2 = int(input("Sayı2:"))

print(ekok(sayi1, sayi2), "en küçük ortak katıdır")
