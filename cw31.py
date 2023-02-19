import random

lista = []
for a in range(0,30):
    lista.append(int(random.random()*100))
print(lista)
suma = 0
for a in lista:
    suma+=a
print("suma:",suma)
podpunktg = [lista[0],lista[1],lista[2],lista[lista.__len__()-3],lista[lista.__len__()-2],lista[lista.__len__()-1]]
posortowana = lista
posortowana.sort()
print("największy element",posortowana[posortowana.__len__()-1])
print("najmniejszy element",posortowana[0])

for a in range(0,14):
    print(posortowana[a],end=" ")
print()
for a in posortowana:
    if a in range(0,10):
        print(a,end=" ")
print()
maxc = 0
liczbamaxc = 0
for a in range(0,100):
    c = 0
    for b in posortowana:
        if a == b:
            c+=1
    if maxc < c:
        maxc = c
        liczbamaxc = a    
print(liczbamaxc,"wystęuje",maxc,"razy")

wiekszeod30 = 0
for a in posortowana:
    if a>30:
        wiekszeod30+=1
print("liczb większych od 30 jest",wiekszeod30)
print(podpunktg)