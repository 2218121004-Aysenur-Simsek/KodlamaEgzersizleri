print("Kök Bulma")

"""
denklem =ax^2 + bx +c
delta=b^2-4ac
kök1=(b+delta^1/2)/2a
kök2=(b-delta^1/2)/2a
"""

a=int(input("x2 nin katsayısını girin:"))
b=int(input("x in katsayısını girin:"))
c=int(input("sabit sayıyı girin:"))

delta=b ** 2 - 4 * a * c
print("Delta:",delta)

kok1=(-b+(delta**1/2))/(2*a)
kok2=(-b-(delta**1/2))/(2*a)

print("kök1:{}\nKök2:{}".format(kok1,kok2))

a=int(input("Sayı girin:"))
b=int(input("Sayı girin:"))
c=int(input("Sayı girin:"))

sayilar=[a,b,c,a*b*c]

print("{}*{}*{}:{}".format(sayilar[0],sayilar[1],sayilar[2],sayilar[3]))
