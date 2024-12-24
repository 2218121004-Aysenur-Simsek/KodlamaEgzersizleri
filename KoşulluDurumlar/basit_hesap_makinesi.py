print(""""**************************

Basit Hesap Makinesi
 
1. Toplama işlemi

2. Çıkarma işlemi

3. Çarpma İşlemi 

4. Bölme İşlemi

***************************""")

a = int(input("Birinci sayıyı Girin."))
b = int(input("İkinci sayıyı Girin."))

islem = int(input("İşlem:"))

if islem==1:
    print("{} ile {} nin toplamı {} dir.".format(a,b,a+b))

elif islem==2:
    print("{} ile {} nin farkı {} dir.".format(a,b,a-b))

elif islem==3:
    print("{} ile {} nin çarpımı {} dir.".format(a,b,a*b))

elif islem==4:
    print("{} ile {} nin bölümü {} dir.".format(a,b,a/b))

else:
    print("Geçersiz işlem!")