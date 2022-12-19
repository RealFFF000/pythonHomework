parzyste = 0
nieparzyste = 0
while True:
    a = float(input("Podaj liczbę"))
    if a == 0:
        break
    else:
        if a % 2 == 0:
            parzyste+=1
        else:
            nieparzyste+=1

print(parzyste,nieparzyste)