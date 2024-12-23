print(""""*****************
MÜKEMMEL SAYI BULMA

******************""")

sayi=int(input("Sayı griniz:"))

i=1
toplam=0

while(i<sayi):
    if(sayi % i == 0):
        toplam+=i
    i+=1

if(toplam == sayi):
    print(sayi ,"Mükemmel sayıdır.")

else:
    print(sayi ,"Mükemmel sayı değildir")