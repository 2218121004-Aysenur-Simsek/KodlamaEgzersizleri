print("Sayı Değiştirme")

a=int(input("Sayı girin:"))
b=int(input("Sayı girin:"))


print("Değiştirilmeden önce a:{},b:{}".format(a,b))

a,b=b,a

print("Değiştirildikten sonra a:{},b:{}".format(a,b))

print("Üçgen Alanı Hesaplama")

a=int(input("ilk dik kenarı girin:"))
b=int(input("ikinci dik kenarı girin:"))
alan=(a*b)/2

print("Üçgenin alanı:",alan)

