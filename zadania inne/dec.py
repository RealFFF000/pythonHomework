liczba = int(input("podaj liczbę dziesiętną "))
binarka = []

while True:
    if liczba == 1:
        binarka.append(liczba%2)
        break
    binarka.append(liczba%2)
    liczba = liczba//2

for a in range(1,binarka.__len__()+1):
    print(binarka[binarka.__len__()-a],end="")