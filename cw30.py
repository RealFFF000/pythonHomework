def kwotazysku(kwota,oprocentowanie,dlugosc):
    hajs = kwota
    for miesiac in range(0,dlugosc):
        hajs = round(hajs*(1+((oprocentowanie/100)/12)),2)
        print("w",miesiac+1,"miesiącu masz",hajs,"zł")
    print("całkowity zysk z takiej lokaty wynosi",round(hajs-kwota,2))
kwotazysku(float(input("podaj kwotę wpłaconych pieniędzy ")),int(input("podaj oprocentowanie ")),int(input("podaj czas trwania lokaty w miesiącach ")))