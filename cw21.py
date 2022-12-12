liczby = []
parzyste = 0
nieparzyste = 0
while True:
    a = float(input("Podaj liczbę"))
    liczby.append(a)
    if liczby[liczby.__len__()-1] == 0:
        break
for a in range(0,liczby.__len__()):
    if liczby[a] % 2 == 0:
        parzyste+=1
    else:
        nieparzyste+=1

print("podano ",parzyste-1," liczb parzystych i ",nieparzyste," liczb nieparzystych")