import random
import time

class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["Trt"],kanal="trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    def tv_ac(self):
        if(self.tv_durum=="Açık"):
            print("Televizyon zaten açık.")
        else:
            print("Televizyon Açılıyor...")
            self.tv_durum=("Açık")
    def tv_kapat(self):
        if(self.tv_durum=="Kapalı"):
            print("Televizyon zaten kapalı.")
        else:
            print("Televizyon Kapatılıyor...")
            self.tv_durum=("Kapalı")
    def ses_ayarları(self):

        while True:
            cevap=input("Artırmak için '>' azaltmak için '<' çıkmak için 'q' tuşuna basın.")
            if(cevap=="<"):
                if(self.tv_ses!=0):
                    self.tv_ses-=1
                    print("Ses=",self.tv_ses)
            elif(cevap==">"):
                if(self.tv_ses!=31):
                    self.tv_ses+=1
                    print("Ses:",self.tv_ses)
            else:
                print("Ses güncelledi:",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi.")
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("Şuan ki kanal:",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv Durumu:{}\n Tv Sesi:{}\n Kanal Listesi:{}\n Açık Kanal:{}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda = Kumanda()

print(""""*****************
TELEVİZYON UYGULAMASI

1.TV AÇ
2.TV KAPAT
3.SES AYARLARI
4.KANAL EKLE
5.KANAL SAYISI ÖĞRENME
6.RASTGELE KANALA GEÇME
7.TELEVİZYON BİLGİLERİ
ÇIKMAK İÇİN Q YA BASIN

******************""")

while True:
    islem=int(input("İşleminizi girin:"))

    if(islem=='q'):
        print("Program sonlandırılıyor..")
        break
    elif(islem==1):
        kumanda.tv_ac()
    elif (islem == 2):
        kumanda.tv_kapat()
    elif (islem == 3):
        kumanda.ses_ayarları()
    elif (islem == 4):
        kanal_isimleri=input("Kanal isimlerini ',' ile ayırarak giriniz!")
        kanal_listesi=kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (islem == 5):
        print("Kanal sayısı:",len(kumanda))
    elif (islem == 6):
        kumanda.rastgele_kanal()
    elif (islem == 7):
        print(kumanda)
    else:
        print("Geçersiz işlem!")