def dec2bin(liczba):
    binarka = ""
    while True:
        if liczba == 1:
            binarka+=str(liczba%2)
            break
        binarka+=str(liczba%2)
        liczba = liczba//2

    return int(binarka[::-1])

liczba1 = int(input("podaj 1 liczbę dziesiętną "))
print(dec2bin(liczba1))
liczba2 = (int(input("podaj 2 liczbę dziesiętną ")))
print(dec2bin(liczba2))
print(dec2bin(liczba1+liczba2))