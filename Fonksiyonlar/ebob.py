print(""""*****************
EBOB BULMA
******************""")

def ebob(sayi1,sayi2):

    i=1
    ebob=1

    while(i<=sayi1 and i<=sayi2):
        if((sayi1 % i == 0) and (sayi2 % i == 0)):
            ebob=i
        i+=1
    return ebob

sayi1=int(input("Sayı1:"))
sayi2=int(input("Sayı2:"))

print(ebob(sayi1,sayi2),"en büyük ortakbölenidir")