print("Harf notu hesaplama")

vize1 = int(input("vize1 notunu giriniz:"))
vize2 = int(input("vize2 notunu giriniz:"))
final = int(input("final notunu giriniz:"))

note = (vize1*3/10)+(vize2*3/10)+(final*4/10)
print("Not:",note)

if note >= 90:
    print("AA")
elif note >= 85:
    print("BA")
elif note >= 80:
    print("BB")
elif note >= 75:
    print("BC")
elif note >= 70:
    print("CC")
elif note >= 65:
    print("CD")
elif note >= 60:
    print("DD")
elif note >= 55:
    print("FD")
else:
    print("FF")