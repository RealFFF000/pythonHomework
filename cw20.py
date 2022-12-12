a = int(input("podaj liczbę \n"))
c = []
for b in range(a):
    if b !=0:
        if a % b == 0:
            c.append(b)

print("dzielniki to: ",c)
