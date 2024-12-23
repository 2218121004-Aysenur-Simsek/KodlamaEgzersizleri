print(""""*****************
FİBONACCİ BULMA

Çıkmak için 'q' ya basınız

******************""")

a=1
b=1

fibonacci=[a,b]
sayi=int(input("Bulmak istediğiniz sayıyı girin:"))
for i in range(sayi):
    a,b = b,a+b
    print("a:",a,"b:",b)
    fibonacci.append(b)

print("Sayının fibonacci değeri: ",fibonacci)