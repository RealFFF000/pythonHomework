widzowie = int(input("podaj liczbe widzów "))
cena = 0
for _ in range(0,widzowie):    
    a = int(input("podaj wiek widza "))
    if a>3 and a<12:
        print("cena za osobę w wieku",a,"lat to 10 zł")
        cena+=10
    elif a>12:
        print("cena za osobę w wieku",a,"lat to 15 zł")
        cena+=15
    else:
        print("osoby w wieku ponizej 3 lat oglądają bezpłatnie")

print("cena za wszystkie",widzowie,"osób to:",cena,"zł")

