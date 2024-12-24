print("Kİtle indexi")

boy = float(input("Metre cinsinden boy giriniz:"))
kilo = int(input("Kilo girinz:"))

BKI = kilo/(boy*boy)
print("BKI: {}".format(BKI))

if BKI<=18.5:
    print("Zayıf")
elif 18.5<BKI<=25:
    print("Normal")
elif 25<BKI<=30:
    print("Fazla kilolu")
else:
    print("Obez")
