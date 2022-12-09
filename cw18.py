liczby = []
while True:
    a = float(input("Podaj liczbę"))
    liczby.append(a)
    if liczby[liczby.__len__()-1] == 0:
        break
suma = 0
for b in range(0,liczby.__len__()):
    suma += liczby[b]
print(suma)