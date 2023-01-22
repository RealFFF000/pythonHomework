a = int(input("podaj liczbe a \n"))
b = int(input("podaj liczbe b \n"))
d = []
for c in range(a,b+1):
    print(c,end=" ")
    d.append(c)
for c in range(a,b+1):
    print(d[b-c],end=" ")

