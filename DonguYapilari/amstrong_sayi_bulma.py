print(""""*****************
AMSTRONG SAYI BULMA

******************""")

sayi=input("Sayı giriniz: ")
basamak_sayisi=len(sayi)
sayi=int(sayi)
toplam=0
basamak=0

gecici_sayi=sayi

while(gecici_sayi>0):
    basamak=gecici_sayi % 10
    toplam += basamak ** basamak_sayisi
    gecici_sayi //= 10

if(toplam == sayi):
    print(sayi,"mükemmel sayıdır.")
else:
    print(sayi,"mükemmel sayı değildir.")