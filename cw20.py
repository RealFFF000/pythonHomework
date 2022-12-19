a = int(input("podaj liczbę \n"))
c = []
for b in range(a):
    if b == 0:
        continue
    if a % b == 0:
        c.append(b)
print(c)
