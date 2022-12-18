a = int(input("podaj liczbę \n"))
for b in range(a):
    if b == 0:
        continue
    if a % b == 0:
        print(b," ", end="")
