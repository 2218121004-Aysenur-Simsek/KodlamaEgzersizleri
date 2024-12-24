print(""""*****************
FAKTÖRİYEL BULMA

Çıkmak için 'q' ya basınız

******************""")

while True:
    sayi=input("Sayı girin:")
    if(sayi == "q"):
        print("çıkış yapılıyor...")
        break
    else:
        sayi=int(sayi)

        faktoriyel = 1
        for i in range(1, sayi + 1):
            faktoriyel *= i
        print("{}'nin faktöriyeli: {}".format(sayi,faktoriyel))
