print(""""*****************
MÜKEMMEL SAYILAR
******************""")
def mukemmel(sayi):

    toplam=0

    for i in range(1,sayi):
        if(sayi % i == 0):
            toplam+=i

    return toplam==sayi

for i in range(1,1000):
    if(mukemmel(i)):
        print("Mükemmel sayı",i)


