print(""""*****************
GİRDİLER TOPLAMI

******************""")

toplam=0

while True:
    sayi=input("Toplamak istediğiniz sayıyı girin:")
    if(sayi == "q"):
        print("Çıkış yapılıyor....")
        break
    else:
        sayi = int(sayi)
        toplam += sayi
print("Sayıların toplamı: ",toplam)
