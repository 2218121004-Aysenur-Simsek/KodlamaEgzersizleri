print("""*********************

Kullanıcı Girişi
*********************
""")

sys_kullanici_ad="ayşemnur"
sys_parola="12345"

kullanici_ad=input("Kullanıcı Adı Girin:")
parola=input("Parola Girin:")

if(sys_kullanici_ad != kullanici_ad and sys_parola == parola):
    print("Hatalı Ad")
elif(sys_kullanici_ad == kullanici_ad and sys_parola != parola):
    print("Hatalı Parola")
elif(sys_kullanici_ad != kullanici_ad and sys_parola != parola):
    print("Hatalı Ad ve Parola")

else:
    print("Sisteme Başarılı Giriş")