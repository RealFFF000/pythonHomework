liczba = int(input("podaj liczbe "))
pierwsza = True
for a in range(2,liczba):
    if liczba%a == 0:
        pierwsza = False
        break
    
if pierwsza:
    print("podana liczba jest pierwsza")
else:
    print("podana liczba nie jest pierwsza")