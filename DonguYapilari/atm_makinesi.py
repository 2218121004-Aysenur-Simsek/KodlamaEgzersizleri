print(""""*****************
ATM MAKİNESİ
******************""")

print(""""*****************
ATM MAKİNESİNDE YAPILACAK İŞLEMLER

1.BAKİYE SORGULAMA
2.PARA YATIRMA
3.PARA ÇEKME
PRGRAMDAN ÇIKMAK İÇİN 'q'YA BASIN.
******************""")

bakiye=1000

while True:
    islem=input("yapacağınız işlemi seçin:")
    if(islem == "q"):
        print("Güvenle çıkış yapıyorsunuz,yine bekleriz:)")
        break
    elif(islem == "1"):
        print("Mevcut bakiyeniz: ",bakiye)
    elif(islem == "2"):
        miktar=int(input("yatıracağınız tutarı giriniz"))
        bakiye +=miktar
        print("Mevcut bakiyeniz: ", bakiye)
    elif (islem == "3"):
        miktar = int(input("Çekeceğiniz tutarı giriniz"))
        if(miktar>bakiye):
            print("Yetersiz Bakiye,çekemezsiniz!")
            print("Mevcut bakiyeniz: ", bakiye)
            continue
        bakiye -= miktar
        print("Mevcut bakiyeniz: ", bakiye)
    else:
        print("Geçersiz işlem:")
