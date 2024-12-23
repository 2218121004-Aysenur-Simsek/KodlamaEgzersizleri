print(""""*****************
SAYI TAHMİNİ OYUNU
******************""")

import random
import time

rastgele_sayi=random.randint(1,40)
tahmin_hakki=7

while True:
    tahmin=int(input("tahmin sayi:"))

    if(tahmin>rastgele_sayi):
        print("Bilgiler sorgulanıyor... ")
        time.sleep(1)
        print("Daha düşük bir sayı söyleyin!")
        tahmin_hakki-=1

    elif(tahmin<rastgele_sayi):
        print("Bilgiler sorgulanıyor... ")
        time.sleep(1)
        print("Daha yüksek bir sayı söyleyin!")
        tahmin_hakki-=1

    else:
        print("Bilgiler sorgulanıyor... ")
        time.sleep(1)
        print("Tebrikler!,sayımız ",rastgele_sayi)
        break

    if(tahmin_hakki==0):
        print("Tahmin hakkınız bitti")
        print("Rastgele sayımız:",rastgele_sayi)
        break
