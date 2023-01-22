def liczbmi(waga,wzrost):
    Bmi = waga/(wzrost*wzrost)
    if Bmi < 20:
        return "Niedowaga"
    elif 20<=Bmi<=25:
        return "Waga prawidłowa"
    elif 20<Bmi<=30:
        return "Nadwaga"
    else:
        return "Otyłość"


print(liczbmi(float(input("podaj wagę\n")),float(input("podaj wzrost\n"))))