print("""*****************
SAYININ OKUNUŞU
******************""")

onlar=["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
birler=["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]

def okunus(sayi):

    birinci=sayi%10
    ikinci=sayi//10

    return onlar[ikinci]+" "+birler[birinci]

sayi=int(input("Sayı giriniz:"))

print(okunus(sayi))