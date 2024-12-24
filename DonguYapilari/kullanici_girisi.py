print(""""*****************
KULLANICI GİRİŞİ
******************""")

sys_kullanici_ad="Aysenur"
sys_parola="8020"

giris_hakki=3

while True:
    kullanici_ad = input("Kullanıcı adı girin:")
    kullanici_parola = input("Kullanıcı parola girin:")

    if (sys_kullanici_ad != kullanici_ad and sys_parola == kullanici_parola):
        print("Hatalı Ad")
        giris_hakki-=1
    elif (sys_kullanici_ad == kullanici_ad and sys_parola != kullanici_parola):
        print("Hatalı Parola")
        giris_hakki -= 1
    elif (sys_kullanici_ad != kullanici_ad and sys_parola != kullanici_parola):
        print("Hatalı Ad ve Parola")
        giris_hakki -= 1
    else:
        print("Sisteme Başarılı Giriş Yaptınız.")
        break
    if(giris_hakki==0):
        print("Giriş hakkınız bitti!")
        break
