iloscMalp = int(input("podaj liczbe ludzi: \n"))
cena = 0
for osoba in range(0,iloscMalp):
    wiek = int(input("podaj wiek kolejnego członka grupy: \n"))
    if wiek<3:
        dodac = 0
    elif wiek>=3 and wiek<=12:
        dodac = 10
    else:
        dodac = 15
    print("cena za tego czlonka:",dodac)
    cena+=dodac

print("suma za całą grupę: ",cena)
