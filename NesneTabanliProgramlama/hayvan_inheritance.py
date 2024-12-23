print(""""*****************
HAYVANLAR ALEMİ İNHERİTANCE:)
******************""")

class Hayvanlar():
    def __init__(self,isim,yaş,tür):
        self.isim=isim
        self.yaş=yaş
        self.tür=tür
    def __str__(self):
        return "isim:{}\nYaş:{}\nTür:{}".format(self.isim,self.yaş,self.tür)

class Köpek(Hayvanlar):
    def __init__(self,isim,yaş,tür,cins):
        super().__init__(isim,yaş,tür)
        self.cins=cins
    def __str__(self):
        return "isim:{}\nYaş:{}\nTür:{}\nCins:{}".format(self.isim,self.yaş,self.tür,self.cins)

class Kuş(Hayvanlar):
    def __init__(self,isim,yaş,tür,kanat_genişliği):
        super().__init__(isim, yaş, tür)
        self.kanat_genişliği=kanat_genişliği
    def __str__(self):
        return "isim:{}\nYaş:{}\nTür:{}\nKanat Genişliği:{}".format(self.isim,self.yaş,self.tür,self.kanat_genişliği)

class At(Hayvanlar):
    def __init__(self,isim,yaş,tür,hız):
        super().__init__(isim, yaş, tür)
        self.hız=hız
    def __str__(self):
        return "isim:{}\nYaş:{}\nTür:{}\nHız:{}".format(self.isim,self.yaş,self.tür,self.hız)

# Köpek sınıfından bir örnek
köpek1 = Köpek("Karabaş", 5, "Kangal", "Bekçi")
print(köpek1)

# Kuş sınıfından bir örnek
kuş1 = Kuş("Şahin", 3, "Yırtıcı Kuş", "1.5 metre")
print(kuş1)

# At sınıfından bir örnek
at1 = At("Rüzgar", 7, "Arap Atı", "50 km/h")
print(at1)
