print("En büyük sayıyı bulma")

a=int(input("a sayısını girin:"))
b=int(input("b sayısını girin:"))
c=int(input("c sayısıyı girin:"))

if(a>=b and a>=c):
    print("En büyük a:",a)
elif(b>=a and b>=c):
    print("En büyük b:",b)
elif(c>=a and c>=b):
    print("En  büyk c:",c)