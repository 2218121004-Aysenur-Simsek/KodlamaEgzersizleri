print("En büyük sayıyı bulma")

a=int(input("a sayısını girin:"))
b=int(input("b sayısını girin:"))
c=int(input("c sayısıyı girin:"))

# En büyük sayıyı bulma
if (a >= b and a >= c):
    print("En büyük a:", a)
elif (b >= a and b >= c):
    print("En büyük b:", b)
else:
    print("En büyük c:", c)

# En küçük sayıyı bulma
if (a <= b and a <= c):
    print("En küçük a:", a)
elif (b <= a and b <= c):
    print("En küçük b:", b)
else:
    print("En küçük c:", c)
