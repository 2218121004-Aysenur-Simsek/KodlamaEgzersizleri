print(""""*****************
ÜÇE BÖLÜNEBİLEN SAYILAR
******************""")

for i in range(1,101):
    if((i % 3) == 0 and (i % 4) == 0):
        continue
    else:
        print(i)