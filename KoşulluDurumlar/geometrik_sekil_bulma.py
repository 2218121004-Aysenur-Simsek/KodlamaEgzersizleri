print("Şekil bulma")

sekil_tipi=input("Şeklin tipini girin:")

if sekil_tipi == "Dörtgen":
    print("Lütfen kenarları sırası ile giriniz.")
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    d = int(input("Kenar-4:"))
    if(a==b and a==c and a==d):
        print("Kare")
    elif(a==c and b==d):
        print("Dikdörtgen")
    else:
        print("Dörtgen")

elif sekil_tipi=="Üçgen":
    print("Lütfen kenarları sırası ile giriniz.")
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    #abs pythonda mutlak alma işlemini yapar!!!!
    if( abs(a+b) > c or abs(a+c) > b or abs(b+c) >a):
        if(a==b and a==c):
            print("Eşkanar üçgen")
        elif(a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
            print("İkizkenar üçgen")
        else:
            print("Çeşitkenar Üçgen")
    else:
        print("Üçgen belirtmiyor")

else:
    print("Geçersiz Şekil")




